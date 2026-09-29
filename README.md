🚀 Sentiment Insights
An AWS-Powered Customer Review Analysis & Summarization System

Transform raw customer reviews into actionable insights using a fully serverless, scalable NLP pipeline built on AWS Lambda, Comprehend, DynamoDB, SageMaker & QuickSight.

📌 Overview

This project is an end-to-end AI-powered system that automatically:

✅ Ingests customer reviews from Amazon S3
✅ Performs NLP using Amazon Comprehend
✅ Stores enriched results in DynamoDB
✅ Generates AI summaries using SageMaker JumpStart
✅ Visualizes insights in Amazon QuickSight

It is designed for e-commerce, customer experience analytics, cloud engineering, and AI/ML automation.

🏗️ Architecture

## 🏗️ System Architecture

Below is the architecture diagram representing the full workflow:

![Architecture Diagram](https://raw.githubusercontent.com/15912315/Sentiment-Insights.-An-AWS-Powered-Customer-Review-Analysis-and-Summarization-System/main/architectureimage)

📁 User Uploads CSV → S3 Bucket  
      ⬇  
⚡ Lambda (process-reviews-lambda)  
      → Comprehend (Sentiment, Key Phrases, Entities)  
      → DynamoDB (ReviewAnalysis1)  
      ⬇  
⚡ Lambda (generate-summary-lambda)  
      → SageMaker Endpoint (JumpStart Summarization)  
      → DynamoDB (ReviewSummaries1)  
      ⬇  
📊 Amazon QuickSight Dashboard  
## 📊 Published Dashboard – QuickSight Output

Below is the published dashboard diagram representing the final visualization output of the sentiment analysis pipeline:

🎯 Key Features
🔍 1. Automated NLP Processing

Sentiment Classification

Key Phrase Extraction

Entity Recognition

Language Detection

🧠 2. AI-Powered Text Summaries

Using SageMaker JumpStart transformer model to generate concise summaries like:

“Customers appreciate fast delivery but commonly report product quality issues…”

📊 3. Interactive Visualization

QuickSight dashboard includes:

Overall Sentiment (Positive / Negative / Mixed)

Sentiment by Country

Rating vs Sentiment

Top Keywords

Most common complaints

AI-Generated Summary Panel

⚡ 4. Fully Serverless

No infrastructure to manage — auto-scaling, event-driven, and low-cost.

🧰 Technologies Used
Service	Purpose
Amazon S3	Store raw CSV review files
AWS Lambda	Serverless compute for pipelines
Amazon Comprehend	NLP: sentiment, key phrases, entities
DynamoDB	NoSQL storage for structured reviews
SageMaker JumpStart	HuggingFace summarization model
QuickSight	BI dashboard for insights
IAM	Secure access control
📂 Project Structure
├── lambda/
│   ├── process-reviews-lambda.py
│   └── generate-summary-lambda.py
├── s3-datasets/
│   └── reviews_1000.csv
├── dynamodb/
│   ├── ReviewAnalysis1
│   └── ReviewSummaries1
├── quicksight/
│   └── dashboard-assets
└── README.md

🔧 Setup Instructions
1️⃣ Upload CSV to S3

Upload your dataset, e.g.

eCommerce_Reviews_500new.csv
eCommerce_Reviews_1000.csv

2️⃣ Lambda Trigger

S3 event triggers first Lambda

Lambda parses CSV → sends text to Comprehend

3️⃣ DynamoDB Tables

ReviewAnalysis1

ReviewSummaries1

4️⃣ Deploy SageMaker Endpoint

From JumpStart:
"Text Summarization – HuggingFace DistilBART / T5"

5️⃣ Generate Summary

Run the second Lambda → stores summary in DynamoDB

6️⃣ Visualize in QuickSight

Connect DynamoDB via Data Source → Dataset → Visualization

🧪 Example Output
Sentiment Classification
Review	Sentiment
“Great product! Love it.”	Positive
“Terrible quality, very disappointed.”	Negative
“Fast delivery but packaging was bad.”	Mixed
AI-Generated Summary
Most customers appreciated the fast delivery service, though concerns were frequently raised about product durability and packaging quality. Customer support received positive mentions, while delayed replacements were common complaints.

📊 Sample Dashboard Preview

✔ Donut chart for sentiment
✔ Bar chart for rating distribution
✔ Geographical sentiment map
✔ Keyword cloud from Comprehend
✔ AI summary text box

🚀 Future Improvements

Integration with Amazon Bedrock (advanced LLMs)

Multilingual review analysis

Product recommendation engine

Real-time streaming pipeline using Kinesis

Review spam detection using custom ML

🏁 Conclusion

This project demonstrates the power of a serverless, scalable, AI-driven pipeline capable of processing thousands of customer reviews automatically.
It delivers actionable insights, reduces manual work, and enables data-driven decision making for product, support, and marketing teams.

👨‍💻 Author

Ritesh Kumar Verma
Cloud & AI Engineer
📧 Email | 🔗 LinkedIn | 🧠 GitHub
