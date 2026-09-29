import boto3
import uuid
import datetime

dynamodb = boto3.resource("dynamodb")

# 🔥 UPDATED TABLE NAMES
table_analysis = dynamodb.Table("ReviewAnalysis1")
table_summary = dynamodb.Table("ReviewSummaries1")

comprehend = boto3.client("comprehend")


def lambda_handler(event, context):

    # 1️⃣ Get all reviews from new table
    reviews = table_analysis.scan()
    items = reviews.get("Items", [])

    texts = [item.get("ReviewText", "") for item in items]

    if not texts:
        return {"message": "No reviews found in ReviewAnalysis1"}

    # Combine text (max 4500 chars for Comprehend)
    combined_text = " ".join(texts)[:4500]

    # 2️⃣ Extract key phrases using Comprehend
    summary = comprehend.detect_key_phrases(
        Text=combined_text,
        LanguageCode="en"
    )
    key_phrases = [kp["Text"] for kp in summary["KeyPhrases"]]

    # 3️⃣ INSERT 50 SUMMARY ITEMS INTO ReviewSummaries1
    results = []
    for i in range(50):

        item = {
            "SummaryID": str(uuid.uuid4()),
            "ProductID": "ALL",
            "CreatedAt": str(datetime.datetime.utcnow()),
            "ReviewCount": len(texts),
            "SummaryText": f"Summary batch #{i+1}",
            "TopKeyPhrases": key_phrases[:10]  # top 10 phrases
        }

        table_summary.put_item(Item=item)
        results.append(item["SummaryID"])

    return {
        "message": "50 summaries created successfully in ReviewSummaries1",
        "SummaryIDs": results
    }