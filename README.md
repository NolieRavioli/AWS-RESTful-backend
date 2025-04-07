# AWS-RESTful-backend

A comprehensive document describing how my RESTful, free, AWS-powered websites works using serverless architecture.  

Educational documentation of development process, complete with source code.

### Table of Contents
- AWS-RESTful-backend
  - [Intro](#intro)
  - [Architecture Overview](#architecture-overview)
  - [How It Works](#how-it-works)
- [nolanpeet.us](#nolanpeetus-external-link)
  - [Intro](https://github.com/NolieRavioli/AWS-RESTful-backend/tree/main/website-nolanpeet_us#intro)
  - [Serverless Architecture](https://github.com/NolieRavioli/AWS-RESTful-backend/tree/main/website-nolanpeet_us#serverless-architecture)
  - [Issues with Truly Serverless Solutions](https://github.com/NolieRavioli/AWS-RESTful-backend/tree/main/website-nolanpeet_us#issues-with-truly-serverless-solutions)
  - [API Gateway](https://github.com/NolieRavioli/AWS-RESTful-backend/tree/main/website-nolanpeet_us#issues-with-truly-serverless-solutions)
- [gfd.sh](#gfdsh-external-link)
  - [introduction](https://github.com/NolieRavioli/AWS-RESTful-backend/tree/main/gfd.sh#introduction)
  - [Architecture Overview](https://github.com/NolieRavioli/AWS-RESTful-backend/tree/main/gfd.sh#architecture-overview)
  - [Lambda Functions Detail](https://github.com/NolieRavioli/AWS-RESTful-backend/tree/main/gfd.sh#lambda-functions-detail)
  - [Frontend Implementation](https://github.com/NolieRavioli/AWS-RESTful-backend/tree/main/gfd.sh#frontend-implementation)
  - [Example Workflow](https://github.com/NolieRavioli/AWS-RESTful-backend/tree/main/gfd.sh#example-workflow)
  - [Challenges & Solutions](https://github.com/NolieRavioli/AWS-RESTful-backend/tree/main/gfd.sh#challenges--solutions)
    - [My Journey From DynamoDB to RDS to Timestream and Self-hosting with a backup.](https://github.com/NolieRavioli/AWS-RESTful-backend/tree/main/gfd.sh#my-journey-from-dynamodb-to-rds-to-timestream-and-self-hosting-with-a-backup)
  - [Conclusion](https://github.com/NolieRavioli/AWS-RESTful-backend/tree/main/gfd.sh#my-journey-from-dynamodb-to-rds-to-timestream-and-self-hosting-with-a-backup)

## Intro

This project was built using AWS Free Tier Lambda and API Gateway to create a interface that aggregates content from internal Lambda functions and external sources. The goal was to create a no-cost data hosting solution starting with gfd.sh as a cloud-based endpoint for tempurature data. nolanpeet.us is a portfolio website framework that attempts to create a serverless portfolio without external references. I did a lot of html by hand for the finished product, but Amazon Q is so exciting. I like to use ChatGPT to code but this was my first experience having an integrated assistant inside the coding environment (I use IDLE mostly).

---
## Architecture Overview

- **Serverless Architecture:**  
  Uses AWS Lambda to run code on-demand without provisioning servers.

- **API Gateway Integration:**  
  Exposes RESTful endpoints and manages HTTP request routing using API Gateway’s AWS Lambda integration. Flexible endpoint mapping for GET, POST, other methods.

- **Load Balancing:**  
  Distributes requests across internal functions and external endpoints for speed as well as high availability and reliability.

- **Logging & Monitoring:**  
  Integrates with AWS CloudWatch for monitoring and troubleshooting of both API Gateway and Lambda functions.

## How It Works

1. **Request Reception:**  
   When a user sends an HTTP request, API Gateway receives it and triggers an associated AWS Lambda function. The entire request—including headers, query strings, and body—is passed directly to Lambda.

2. **Request Processing:**  
   The Lambda function processes the request through custom load-balancing logic.

3. **Endpoint Mapping & HTTP Methods:**  
   API Gateway is configured to handle HTTP methods:
   - **GET:** Retrieves data from external sources.
   - **POST:** Submits data or triggers specific actions.
   - Additional methods (PUT, DELETE, etc.) can be mapped similarly.
   
   This mapping lets the same URL support multiple operations and endpoints, with the Lambda function interpreting and processing each method accordingly.

4. **Lambda Integration Passthrough:**  
   A critical part of this setup is the **integration passthrough** setting. With passthrough enabled, API Gateway delivers the complete, unmodified request payload to the Lambda function. This lets Lambda process complex requests.

5. **Response Aggregation:**  
   After processing, the Lambda function forwards the request to the selected external endpoint, gathers the response, and sends it back to API Gateway. Finally, API Gateway returns the response to the user in the correct format.
--
## [nolanpeet.us](https://nolanpeet.us) (external link)  
[[Source Code](https://github.com/NolieRavioli/AWS-RESTful-backend/tree/main/website-nolanpeet_us)]

This website was designed to serve as a functional model of my knowledge base and custom framework. The inherent challenges of building a serverless website using AWS Lambda functions was a really interesting
opportunity to explore the limits and capabilities of serverless architecture. My goal was to create a serverless "blog" where I can showcase updates and portfolio items, all while avoiding an over-reliance on external resources.

I spent a ton of time hand-coding HTML and CSS for the webpage. It was cool  This project was especially exciting because of Amazon Q. I like to use ChatGPT to code but this was my first experience having an integrated assistant 
inside the coding environment (I use IDLE). It felt really nice to tab complete whole codeblocks with just a single line to nucleate from. Also, if I forget how to do a specific function I can just comment what I want to be done in
pseudo-code or plaintext and have the integrated assistant help me remember syntax!

## [gfd.sh](https://gfd.sh/)(external link)
[[Source Code](https://github.com/NolieRavioli/AWS-RESTful-backend/tree/main/gfd.sh)]

### My Journey From DynamoDB to RDS to Timestream and Self-hosting with a backup.

I started this project by initially storing 12-byte sensor data in **Amazon DynamoDB**. The convenience of a cloud-hosted NoSQL database was appealing. However, I quickly discovered that DynamoDB was storing my tiny 94-bit data points in 1KB increments—leading to storage bloat. It cost me about 2 cents per day, but I was uneasy about the overhead. 

Next, I experimented with **Amazon RDS** (MySQL/Postgres) for more direct control over schema and data structure. While it solved the overhead issue, RDS’s free tier eventually expires, and I was worried about incurring monthly charges for a project that only stores a handful of bytes daily.

Then I moved on to **Amazon Timestream**, hoping its time-series optimizations would make sense for small, frequent sensor updates. Unfortunately, Timestream enforces a billing floor of 100GB-month—even if you only store a few MB of data—leading to an unexpectedly high daily cost. That was a deal-breaker for my near-$0 budget.

In the end, I realized that **Amazon S3** is the perfect, nearly free archival solution for once-a-day backups. I can push tiny daily files, pay just fractions of a cent per month in storage, and rely on S3 for reliable, long-term backups. Meanwhile, for live data, I switched to a self-hosted approach: a lightweight service on my own Ubuntu server writing raw sensor data to a .bin file. Once per day, that file gets uploaded to S3. If my server goes down, I can always fall back on S3 data through my AWS Lambda.

All these iterations taught me valuable lessons about how each AWS service fits particular use cases. For extremely small daily writes, S3 is virtually free. DynamoDB is great for serverless key-value at scale, but not as lean for 12-byte items. RDS and Timestream are powerful but can be expensive at minimal data volumes.

In the end, I combined the best of both worlds: **self-hosting** for real-time data retrieval and **S3** for cheap cloud storage. This synergy keeps my system cost near zero while ensuring the data is always backed up in the cloud. I’m excited to keep exploring serverless tech and optimizing this architecture!
