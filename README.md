# AWS-RESTful-backend

A comprehensive document describing how my RESTful, free, AWS-powered websites works using serverless architecture.  

Educational documentation of development process, complete with source code.

### README.md Table of Contents
#### AWS-RESTful-backend
<ol type='1'>
<a href="#intro"><li>Intro</li></a>
<a href="#architecture-overview"><li>Architecture Overview</li></a>
<a href="#design-process"><li>Design Process</li></a>
<ol>
<ol>
<a href="#scope"><li>Scope</li></a>
<a href="#requirements"><li>Requirements</li></a>
</ol>
</ol>
<ol>
<a href="#analysis"><li>Analysis</li></a>
<a href="#development"><li>Development</li></a>
<ol>
<a href="#design-specification"><li>Design Specification</li></a>
<a href="#prototype-and-testing-loop"><li>Prototype and Testing Loop</li></a>
<a href="#challenges-and-drawbacks-encountered"><li>Challenges and Drawbacks Encountered</li></a>
<a href="#additional-features-implemented-during-development"><li>Additional Features Implemented During Development</li></a>
</ol>
<a href="#implementation"><li>Implementation</li></a>
<ol>
<a href="#support-and-maintenance"><li>Support and Maintenance</li></a>
<a href="#evaluation"><li>Evaluation</li></a>
</ol>
</ol>
<a href="#how-it-works"><li>How It Works</li></a>
<ol type="">
<a href="#1-request-reception"><li>Request Reception</li></a>
<a href="#2-request-processing"><li>Request Processing</li></a>
<a href="#3-endpoint-mapping--http-methods"><li>Endpoint Mapping & HTTP Methods</li></a>
<a href="#4-response-aggregation"><li>Response Aggregation</li></a>
</ol>
</ol>


#### [nolanpeet.us](#nolanpeetus-external-link)
<ol type='1'>
<a href="https://github.com/NolieRavioli/AWS-RESTful-backend/tree/main/website-nolanpeet_us#intro"><li>Intro</li></a>
<a href="https://github.com/NolieRavioli/AWS-RESTful-backend/tree/main/website-nolanpeet_us#serverless-architecture"><li>Serverless Architecture</li></a>
<a href="https://github.com/NolieRavioli/AWS-RESTful-backend/tree/main/website-nolanpeet_us#issues-with-truly-serverless-solutions"><li>Issues with Truly Serverless Solutions</li></a>
<a href="https://github.com/NolieRavioli/AWS-RESTful-backend/tree/main/website-nolanpeet_us#api-gateway"><li>API Gateway</li></a>
</ol>


#### [gfd.sh](#gfdsh-external-link)
<ol type='1'>
  <a href="https://github.com/NolieRavioli/AWS-RESTful-backend/tree/main/gfd.sh#introduction"><li>Introduction</li></a>
  <a href="https://github.com/NolieRavioli/AWS-RESTful-backend/tree/main/gfd.sh#architecture-overview"><li>Architecture Overview</li></a>
  <ol>
    <a href="https://github.com/NolieRavioli/AWS-RESTful-backend/tree/main/gfd.sh#aws-api-gateway-proxy-integration-proxy"><li>AWS API Gateway Proxy Integration (proxy+)</li></a>
    <ol>
      <a href="https://github.com/NolieRavioli/AWS-RESTful-backend/tree/main/gfd.sh#importance-of-proxy-integration"><li>Importance of Proxy Integration:</li></a>
    </ol>
    <a href="https://github.com/NolieRavioli/AWS-RESTful-backend/tree/main/gfd.sh#endpoint-mapping-and-http-methods"><li>Endpoint Mapping and HTTP Methods</li></a>
    <a href="https://github.com/NolieRavioli/AWS-RESTful-backend/tree/main/gfd.sh#lambda-integration-passthrough"><li>Lambda Integration Passthrough</li></a>
  </ol>
  <a href="https://github.com/NolieRavioli/AWS-RESTful-backend/tree/main/gfd.sh#lambda-functions-detail"><li>Lambda Functions Detail</li></a>
  <ol>
    <a href="https://github.com/NolieRavioli/AWS-RESTful-backend/tree/main/gfd.sh#1-data-processing-lambda"><li>1. Data Processing Lambda</li></a>
    <ol>
      <a href="https://github.com/NolieRavioli/AWS-RESTful-backend/tree/main/gfd.sh#tasks-performed"><li>Tasks Performed:</li></a>
    </ol>
    <a href="https://github.com/NolieRavioli/AWS-RESTful-backend/tree/main/gfd.sh#2-data-serving-lambda"><li>2. Data Serving Lambda</li></a>
    <ol>
      <a href="https://github.com/NolieRavioli/AWS-RESTful-backend/tree/main/gfd.sh#tasks-performed-1"><li>Tasks Performed:</li></a>
    </ol>
  </ol>
  <a href="https://github.com/NolieRavioli/AWS-RESTful-backend/tree/main/gfd.sh#frontend-implementation"><li>Frontend Implementation</li></a>
  <ol>
    <a href="https://github.com/NolieRavioli/AWS-RESTful-backend/tree/main/gfd.sh#key-frontend-features"><li>Key Frontend Features:</li></a>
  </ol>
  <a href="https://github.com/NolieRavioli/AWS-RESTful-backend/tree/main/gfd.sh#example-workflow"><li>Example Workflow</li></a>
  <a href="https://github.com/NolieRavioli/AWS-RESTful-backend/tree/main/gfd.sh#challenges--solutions"><li>Challenges & Solutions</li></a>
  <ol>
    <a href="https://github.com/NolieRavioli/AWS-RESTful-backend/tree/main/gfd.sh#my-journey-from-dynamodb-to-rds-to-timestream-and-self-hosting-with-a-backup"><li>My Journey From DynamoDB to RDS to Timestream and Self-hosting with a backup.</li></a>
  </ol>
  <a href="https://github.com/NolieRavioli/AWS-RESTful-backend/tree/main/gfd.sh#conclusion"><li>Conclusion</li></a>
</ol>

---

## Intro

This project was built using AWS Free Tier Lambda and API Gateway to create a interface that aggregates content from internal Lambda functions and external sources. The goal was to create a no-cost data hosting solution starting with gfd.sh as a cloud-based endpoint for tempurature data. nolanpeet.us is a portfolio website framework that attempts to create a serverless portfolio without external references. I did a lot of html by hand for the finished product, but Amazon Q is so exciting. I like to use ChatGPT to code but this was my first experience having an integrated assistant inside the coding environment (I use IDLE mostly).

## Architecture Overview

- **Serverless Architecture:** Uses AWS Lambda to run code on-demand without provisioning servers.

- **API Gateway Integration:** Exposes RESTful endpoints and manages HTTP request routing using API Gateway’s AWS Lambda integration. Flexible endpoint mapping for GET, POST.

- **Load Balancing:** Distributes requests across internal functions and external endpoints for speed as well as high availability and reliability.

- **Logging & Monitoring:** Integrates with AWS CloudWatch for monitoring and troubleshooting of both API Gateway and Lambda functions.

## Design Process

This project was incremental and iterative, and is built on top of [NolieRavioli/rpi-cabinMonitor](https://github.com/NolieRavioli/rpi-cabinMonitor) which itself was in extremely active stages of incremental and iterative development using agile methodologies to define the project scope early in development, using iterative design and prototyping/testing to acheive project requirements while simultaniously introducing new ideas and functionality to the framework. 

The initial planning phase consisted of PRE-prototyping and testing with early versions of [NolieRavioli/rpi-cabinMonitor](https://github.com/NolieRavioli/rpi-cabinMonitor) and xampp with PHP endpoints. Once the proof-of-concept was successfully validated locally, a clearer and more defined project scope was established for migration to AWS. This deliberate planning step significantly streamlined the transition to the cloud, helping identify early challenges, potential risks, and key architectural requirements. By carefully validating assumptions during pre-prototyping, the subsequent cloud migration remained both focused and adaptable.

#### Scope:

1) Develop a lightweight RESTful backend using AWS API Gateway and AWS Lambda.
2) Facilitate requests to external resources and aggregate responses dynamically.
3) Ensure easy scalability and minimal management overhead.

#### Requirements:

1) Fully managed AWS resources with minimal server management.
2) Efficient handling of various HTTP methods (GET, POST).
3) Cost-effective and within the AWS Free Tier (or very minimal cost).
4) Simple integration with external APIs and data sources.

### Analysis:

Initially, my goal was simple: to explore AWS by building a minimal RESTful backend. The primary intent was educational, aimed at understanding cloud architecture fundamentals, API integration, and serverless infrastructure.

- **Cost Overruns:** AWS costs can quickly spiral if services aren't configured optimally. Mitigated by frequent checks and strict configuration monitoring.
- **Complexity and Learning Curve:** As a beginner, AWS felt somewhat overwhelming with configuration. Mitigated by iterative prototyping of lambda functions, API gateway endpoints, and many rounds of reconfigurations.
- **Security Risks:** Exposing endpoints can lead to potential vulnerabilities. Addressed by lambda function source code authentication.

### Development

Throughout numerous rounds of prototyping and iteration on AWS, the Development process continuously evolved, guided by ongoing evaluation and new functionality requirements emerging from hands-on experience. Crucially, a strong initial scope enabled sustained emphasis on efficient cost management—a primary concern for cloud projects—while maintaining flexibility to incorporate innovative ideas and improvements.

This project evolved significantly from initial experimentation to its current robust state. The following subsections outline the comprehensive journey—from early conception to current implementation.

#### Design Specification:

- AWS API Gateway integrated directly with AWS Lambda.
- Lambda functions were developed in Python.
- Each Lambda function maintained statelessness, processing individual requests separately to maximize scalability.

#### Prototype and Testing Loop:

The approach was strongly iterative:

1) Prototype initial Lambda functions:
    - Basic functionality tested (echo endpoints, simple data retrieval).

2) Integrated API Gateway:
    - Simple integration tests performed, including passthrough mode for payloads.

3) External API Integration:
    - Added complexity, external calls, and dynamic data aggregation.
    - Performed thorough manual testing, later adding automated testing with tools like Postman and AWS SAM CLI for rapid local prototyping.

#### Challenges and Drawbacks Encountered:

- **Cold Starts in AWS Lambda:** Initially, slow response times due to Lambda cold starts were noticeable. Explored methods to keep Lambda warm and optimize function code for faster execution.
- **Complex Payload Processing:** Handling integration passthrough involved initially unclear mapping of request parameters. Extensive debugging helped refine request templates for consistency.

#### Additional Features Implemented During Development:

- Robust error handling and clear logging for debugging.
- Integrated AWS CloudWatch for log monitoring and metrics tracking.
- Environment variables for flexible configuration without code redeployment and security.

### Implementation:

The implementation phase was characterized by regular evaluation and iterative refinements.

#### Support and Maintenance:

- Regular checks for AWS resource limits to avoid service disruptions.
- Continuous updates based on AWS best practices and evolving project requirements.
- Automated alerting configured through AWS CloudWatch alarms for proactive monitoring.

#### Evaluation:

- Constant monitoring of response times, error rates, and resource utilization.
- Analysis of CloudWatch metrics to refine performance and cost efficiency continuously.
- Regular feedback loops from users (initially myself and then collaborators), informing improvements.

## How It Works

### 1. Request Reception:
When a user sends an HTTP request, API Gateway receives it and triggers an associated AWS Lambda function. The entire request—including headers, query strings, and body—is passed directly to Lambda.

### 2. Request Processing:
The Lambda function processes the request through custom load-balancing logic.

### 3. Endpoint Mapping & HTTP Methods:
API Gateway is configured to handle HTTP methods:

- GET: Retrieves data from external sources.
- POST: Submits data or triggers specific actions.

Additional methods (PUT, DELETE, etc.) can be mapped similarly.  
This mapping lets the same URL support multiple operations and endpoints, with the Lambda function interpreting and processing each method accordingly.

#### Lambda Integration Passthrough:
A critical part of this setup is the integration passthrough setting. With passthrough enabled, API Gateway delivers the complete, unmodified request payload to the Lambda function. This lets Lambda process complex requests without additional processing by API Gateway. This is something that I forgot about more than once, I must admit.

### 4. Response Aggregation:
After processing, the Lambda function forwards the request to the selected external endpoint, gathers the response, and sends it back to API Gateway. Finally, API Gateway returns the response to the user in the correct format.

---

## [nolanpeet.us](https://nolanpeet.us) (external link)  
[[Source Code](https://github.com/NolieRavioli/AWS-RESTful-backend/tree/main/website-nolanpeet_us)] (github)

This website was designed to serve as a functional model of my knowledge base and custom framework. The inherent challenges of building a serverless website using AWS Lambda functions was a really interesting
opportunity to explore the limits and capabilities of serverless architecture. My goal was to create a serverless "blog" where I can showcase updates and portfolio items, all while avoiding an over-reliance on external resources.

I spent a ton of time hand-coding HTML and CSS for the webpage. It was cool  This project was especially exciting because of Amazon Q. I like to use ChatGPT to code but this was my first experience having an integrated assistant 
inside the coding environment (I use IDLE). It felt really nice to tab complete whole codeblocks with just a single line to nucleate from. Also, if I forget how to do a specific function I can just comment what I want to be done in
pseudo-code or plaintext and have the integrated assistant help me remember syntax!

## [gfd.sh](https://gfd.sh/) (external link)
[[Source Code](https://github.com/NolieRavioli/AWS-RESTful-backend/tree/main/gfd.sh)] (github)

### My Journey From DynamoDB to RDS to Timestream and Self-hosting with a backup.

I started this project by initially storing 12-byte sensor data in **Amazon DynamoDB**. The convenience of a cloud-hosted NoSQL database was appealing. However, I quickly discovered that DynamoDB was storing my tiny 94-bit data points in 1KB increments—leading to storage bloat. It cost me about 2 cents per day, but I was uneasy about the overhead. 

Next, I experimented with **Amazon RDS** (MySQL/Postgres) for more direct control over schema and data structure. While it solved the overhead issue, RDS’s free tier eventually expires, and I was worried about incurring monthly charges for a project that only stores a handful of bytes daily.

Then I moved on to **Amazon Timestream**, hoping its time-series optimizations would make sense for small, frequent sensor updates. Unfortunately, Timestream enforces a billing floor of 100GB-month—even if you only store a few MB of data—leading to an unexpectedly high daily cost. That was a deal-breaker for my near-$0 budget.

In the end, I realized that **Amazon S3** is the perfect, nearly free archival solution for once-a-day backups. I can push tiny daily files, pay just fractions of a cent per month in storage, and rely on S3 for reliable, long-term backups. Meanwhile, for live data, I switched to a self-hosted approach: a lightweight service on my own Ubuntu server writing raw sensor data to a .bin file. Once per day, that file gets uploaded to S3. If my server goes down, I can always fall back on S3 data through my AWS Lambda.

All these iterations taught me valuable lessons about how each AWS service fits particular use cases. For extremely small daily writes, S3 is virtually free. DynamoDB is great for serverless key-value at scale, but not as lean for 12-byte items. RDS and Timestream are powerful but can be expensive at minimal data volumes.

In the end, I combined the best of both worlds: **self-hosting** for real-time data retrieval and **S3** for cheap cloud storage. This synergy keeps my system cost near zero while ensuring the data is always backed up in the cloud. I’m excited to keep exploring serverless tech and optimizing this architecture!
