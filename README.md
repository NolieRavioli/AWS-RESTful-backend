# AWS-RESTful-backend

A comprehensive document describing how my RESTful, free, AWS-powered load-balancer works using serverless architecture.

## Intro

This project was built using AWS Free Tier Lambda and API Gateway to create a unique interface that aggregates content from various external sources. The goal was to build a scalable, cost-effective load balancer that also serves as a "blog" for portfolio updates—all without relying on traditional server hosting. By leveraging AWS services, I was able to overcome challenges like data persistence and dynamic routing. This project also marked my first experience integrating an AI coding assistant (ChatGPT) directly within my coding environment (IDLE), streamlining development with rapid prototyping and code generation.

## Features

- **Serverless Architecture:**  
  Uses AWS Lambda to run code on-demand without provisioning servers, allowing the system to scale automatically.

- **API Gateway Integration:**  
  Exposes RESTful endpoints and manages HTTP request routing using API Gateway’s proxy+ integration, enabling flexible endpoint mapping for GET, POST, and other methods.

- **Load Balancing:**  
  Distributes requests across multiple external endpoints to ensure high availability and reliability.

- **Cost-Efficiency:**  
  Designed to operate entirely within the AWS Free Tier, making it ideal for low-traffic or experimental applications.

- **Scalability:**  
  Automatically adapts to varying levels of incoming traffic thanks to the elasticity of AWS Lambda and API Gateway.

- **Detailed Logging & Monitoring:**  
  Integrates with AWS CloudWatch for real-time monitoring and troubleshooting of both API Gateway and Lambda functions.

## How It Works

1. **Request Reception:**  
   When a user sends an HTTP request, API Gateway receives it and triggers an associated AWS Lambda function. The proxy+ configuration ensures that the entire request—including headers, query strings, and body—is passed directly to Lambda.

2. **Request Processing:**  
   The Lambda function processes the request by applying custom load-balancing logic. It determines which external endpoint should handle the request based on parameters in the incoming payload.

3. **Endpoint Mapping & HTTP Methods:**  
   API Gateway is configured to handle multiple HTTP methods:
   - **GET:** Retrieves data from external sources.
   - **POST:** Submits data or triggers specific actions.
   - Additional methods (PUT, DELETE, etc.) can be mapped similarly.
   
   This mapping ensures that the same URL can support multiple operations, with the Lambda function interpreting and processing each method accordingly.

4. **Lambda Integration Passthrough:**  
   A critical part of this setup is the integration passthrough setting. With passthrough enabled, API Gateway delivers the complete, unmodified request payload to the Lambda function. This is essential for preserving data integrity and ensuring that Lambda can process complex requests accurately. Without proper passthrough, you risk losing vital information needed for routing and processing.

5. **Response Aggregation:**  
   After processing, the Lambda function forwards the request to the selected external endpoint, gathers the response, and sends it back to API Gateway. Finally, API Gateway returns the response to the user in the correct format.

## API Gateway & Lambda Integration Details

### Proxy+ Integration

- **What It Is:**  
  Proxy+ integration in API Gateway allows all aspects of an HTTP request to be forwarded to Lambda without needing to map each element individually. This simplifies the configuration and provides flexibility when handling dynamic requests.

- **Why It’s Important:**  
  It minimizes configuration overhead and ensures that any changes in the request format are automatically passed to Lambda, allowing your backend logic to remain adaptable and responsive to different types of requests.

### Endpoint Mapping (GET, POST, etc.)

- **Multiple HTTP Methods:**  
  API Gateway is configured to handle various HTTP methods through endpoint mapping. This means:
  - **GET requests** are typically used to retrieve data.
  - **POST requests** can submit data or trigger specific actions.
  - Additional methods like **PUT**, **PATCH**, or **DELETE** can be configured to support full CRUD operations.
  
- **Custom Mapping:**  
  This setup enables a single API endpoint to serve multiple functions, with the Lambda function determining the correct action based on the method and parameters provided.

### Lambda Integration Passthrough

- **Critical Setting:**  
  The passthrough behavior is a key setting in the integration between API Gateway and Lambda. It ensures that the entire HTTP request—including any headers, query parameters, and the request body—is transmitted to Lambda without alteration.
  
- **Benefits:**  
  - **Data Integrity:** Ensures that no critical information is lost or modified during the request handling process.
  - **Simplicity:** Reduces the need for complex mapping configurations in API Gateway.
  - **Flexibility:** Allows the Lambda function to handle various types of requests and perform context-aware processing.

## [nolanpeet.us](https://nolanpeet.us) (external link)  
[[Source Code](https://github.com/NolieRavioli/AWS-RESTful-backend/tree/main/website-nolanpeet_us)]

This website was conceived as a functional model of my knowledge base and custom framework. I faced the challenge of building a serverless "blog" where I could display updates and portfolio items without an over-reliance on external resources. I spent a significant amount of time hand-coding HTML and CSS to achieve a polished design, and integrating AWS Lambda functions pushed the envelope on what’s possible with serverless computing.

Notably, this project was enriched by using Amazon Q and having ChatGPT integrated directly within my coding environment (IDLE). The AI assistant made it possible to quickly generate code blocks, recall syntax, and even complete entire functions from simple pseudo-code instructions. This seamless integration has boosted my productivity and enhanced my understanding of both serverless architecture and modern development workflows.

## Conclusion

This project serves as an in-depth exploration into the power and challenges of serverless architecture. By combining AWS Lambda, API Gateway, and custom load-balancing logic, I built a system that is both scalable and cost-effective. Key takeaways include the critical nature of API Gateway’s proxy+ integration, the flexibility afforded by endpoint mapping for different HTTP methods, and the importance of enabling Lambda integration passthrough to maintain data integrity. As I continue to refine this architecture, I look forward to further leveraging serverless technologies to build innovative, resilient web applications.

---

## [gfd.sh](https://gfd.sh/)(external link), My Journey From DynamoDB to RDS to Timestream and Self-hosting with a backup.

I started this project by initially storing 12-byte sensor data in **Amazon DynamoDB**. The convenience of a cloud-hosted NoSQL database was appealing. However, I quickly discovered that DynamoDB was storing my tiny 94-bit data points in 1KB increments—leading to storage bloat. It cost me about 2 cents per day, but I was uneasy about the overhead. 

Next, I experimented with **Amazon RDS** (MySQL/Postgres) for more direct control over schema and data structure. While it solved the overhead issue, RDS’s free tier eventually expires, and I was worried about incurring monthly charges for a project that only stores a handful of bytes daily.

Then I moved on to **Amazon Timestream**, hoping its time-series optimizations would make sense for small, frequent sensor updates. Unfortunately, Timestream enforces a billing floor of 100GB-month—even if you only store a few MB of data—leading to an unexpectedly high daily cost. That was a deal-breaker for my near-$0 budget.

In the end, I realized that **Amazon S3** is the perfect, nearly free archival solution for once-a-day backups. I can push tiny daily files, pay just fractions of a cent per month in storage, and rely on S3 for reliable, long-term backups. Meanwhile, for live data, I switched to a self-hosted approach: a lightweight service on my own Ubuntu server writing raw sensor data to a .bin file. Once per day, that file gets uploaded to S3. If my server goes down, I can always fall back on S3 data through my AWS Lambda.

All these iterations taught me valuable lessons about how each AWS service fits particular use cases. For extremely small daily writes, S3 is virtually free. DynamoDB is great for serverless key-value at scale, but not as lean for 12-byte items. RDS and Timestream are powerful but can be expensive at minimal data volumes.

In the end, I combined the best of both worlds: **self-hosting** for real-time data retrieval and **S3** for cheap cloud storage. This synergy keeps my system cost near zero while ensuring the data is always backed up in the cloud. I’m excited to keep exploring serverless tech and optimizing this architecture!
