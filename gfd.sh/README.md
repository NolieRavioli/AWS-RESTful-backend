# [gfd.sh](https://gfd.sh/)(external link)

### Table of Contents
- [gfd.sh](#gfdsh-external-link)
  - [Introduction](#introduction)
  - [Architecture Overview](#architecture-overview)
  - [Lambda Functions Detail](#lambda-functions-detail)
  - [Frontend Implementation](#frontend-implementation)
  - [Example Workflow](#example-workflow)
  - [Challenges & Solutions](#challenges--solutions)
    - [My Journey From DynamoDB to RDS to Timestream and Self-hosting with a backup.](#my-journey-from-dynamodb-to-rds-to-timestream-and-self-hosting-with-a-backup)
  - [Conclusion](#conclusion)

## Introduction

The "temp" endpoint is part of my AWS-powered serverless ecosystem, designed to provide a responsive, interactive, and informative web-based graphical interface for viewing real-time and historical sensor data. The setup leverages AWS API Gateway integrated with two distinct AWS Lambda functions, each performing specialized tasks. The goal was to build a scalable, easily maintainable, and entirely serverless application that efficiently visualizes environmental data like temperature and humidity.

## Architecture Overview

The "temp" endpoint consists of:

- **AWS API Gateway** configured with proxy integration (`proxy+`)
- Two **AWS Lambda Functions**:
  1. **Data Processing Lambda**: Fetches, processes, and aggregates data from the external database and external APIs.
  2. **Data Serving Lambda**: Serves processed data as JSON via API Gateway to the frontend.
- Frontend: HTML/JavaScript page using Chart.js for visualizing data retrieved from the Data Serving Lambda.

### AWS API Gateway Proxy Integration (`proxy+`)

API Gateway’s `proxy+` integration routes all incoming HTTP requests directly to Lambda functions without detailed manual mapping. This integration forwards the entire request payload, headers, query strings, and path parameters directly to Lambda, simplifying configuration.

#### Importance of Proxy Integration:
- **Flexibility**: Automatically forwards complex or changing HTTP requests to Lambda.
- **Reduced Configuration Overhead**: No need to manually map every endpoint and request attribute individually.
- **Complete Data Integrity**: Entire request preserved, ensuring Lambda functions can comprehensively process requests.

### Endpoint Mapping and HTTP Methods

The temp endpoint supports multiple HTTP methods:

- **GET Method**: The frontend JavaScript fetches temperature and humidity data as JSON.
- **POST Method**: Future extensions could allow data submission or sensor configuration.

### Lambda Integration Passthrough

Setting API Gateway to passthrough mode (`Lambda Proxy Integration`) ensures the Lambda functions receive the complete HTTP request context unaltered:

- **Full request body and metadata are passed directly to Lambda.**
- **Critical for maintaining request integrity, especially in complex scenarios.**

## Lambda Functions Detail

### 1. Data Processing Lambda

This function handles retrieving and transforming raw sensor data:

- Queries databases or external endpoints to retrieve sensor data.
- Transforms and formats timestamps, temperature, humidity, battery, and signal strength into structured JSON.
- Performs aggregation logic to calculate total entries, recent entries, battery status, and signal strength for each sensor channel.

#### Tasks Performed:
- **Timestamp processing**: Converts UTC timestamps to local time zones.
- **Battery and Signal Strength Checks**: Identifies low battery statuses and evaluates signal reliability.
- **Aggregation and Filtering**: Summarizes data to optimize payload size and enhance readability.

### 2. Data Serving Lambda

After processing data, this Lambda function serves JSON responses for frontend consumption:

- Receives requests from API Gateway.
- Fetches pre-processed data from intermediate storage or directly invokes the Data Processing Lambda.
- Ensures quick response times to maintain frontend performance.

#### Tasks Performed:
- **Serving JSON Payloads**: Provides structured data suitable for frontend charts.
- **Error Handling**: Returns meaningful errors if data processing encounters issues.
- **Performance Optimization**: Caches results for faster subsequent retrievals when feasible.

## Frontend Implementation

The frontend HTML utilizes the Chart.js library to render dynamic, interactive graphs based on JSON data retrieved from the Lambda functions:

- Fetches data asynchronously from the API Gateway URL linked to the "temp" endpoint.
- Allows users to toggle between different sensor channels and data types (Temperature and Humidity).
- Provides zooming and panning functionality through integration with chartjs-plugin-zoom.

### Key Frontend Features:

- **Dynamic Data Rendering**: Continuously updates charts based on Lambda responses.
- **Interactive Controls**: Allows toggling of sensor data visibility and temperature units (Celsius/Fahrenheit).
- **Responsive Design**: Automatically scales and fits within various display sizes and devices.

## Example Workflow

1. **Frontend Request**: The HTML/JS page issues a `fetch()` request to the API Gateway endpoint.
2. **API Gateway**: Receives the request and forwards it via proxy integration to the Data Serving Lambda.
3. **Data Serving Lambda**: Retrieves and returns processed sensor data as JSON.
4. **Frontend Rendering**: The JavaScript on the frontend processes the JSON data and renders interactive graphs using Chart.js.

## Challenges & Solutions

- **Challenge**: Handling large data payloads within Lambda’s constraints.
  - **Solution**: Aggregating and summarizing data to reduce payload size without sacrificing detail.

- **Challenge**: Maintaining data integrity through complex request structures.
  - **Solution**: Leveraging API Gateway’s proxy+ integration and Lambda integration passthrough to maintain request fidelity.

- **Challenge**: Providing a responsive user experience despite Lambda's cold-start latency.
  - **Solution**: Implementing lightweight JSON responses and using frontend caching or asynchronous loading.

### My Journey From DynamoDB to RDS to Timestream and Self-hosting with a backup.

I started this project by initially storing 12-byte sensor data in **Amazon DynamoDB**. The convenience of a cloud-hosted NoSQL database was appealing. However, I quickly discovered that DynamoDB was storing my tiny 94-bit data points in 1KB increments—leading to storage bloat. It cost me about 2 cents per day, but I was uneasy about the overhead. 

Next, I experimented with **Amazon RDS** (MySQL/Postgres) for more direct control over schema and data structure. While it solved the overhead issue, RDS’s free tier eventually expires, and I was worried about incurring monthly charges for a project that only stores a handful of bytes daily.

Then I moved on to **Amazon Timestream**, hoping its time-series optimizations would make sense for small, frequent sensor updates. Unfortunately, Timestream enforces a billing floor of 100GB-month—even if you only store a few MB of data—leading to an unexpectedly high daily cost. That was a deal-breaker for my near-$0 budget.

In the end, I realized that **Amazon S3** is the perfect, nearly free archival solution for once-a-day backups. I can push tiny daily files, pay just fractions of a cent per month in storage, and rely on S3 for reliable, long-term backups. Meanwhile, for live data, I switched to a self-hosted approach: a lightweight service on my own Ubuntu server writing raw sensor data to a .bin file. Once per day, that file gets uploaded to S3. If my server goes down, I can always fall back on S3 data through my AWS Lambda.

All these iterations taught me valuable lessons about how each AWS service fits particular use cases. For extremely small daily writes, S3 is virtually free. DynamoDB is great for serverless key-value at scale, but not as lean for 12-byte items. RDS and Timestream are powerful but can be expensive at minimal data volumes.

In the end, I combined the best of both worlds: **self-hosting** for real-time data retrieval and **S3** for cheap cloud storage. This synergy keeps my system cost near zero while ensuring the data is always backed up in the cloud. I’m excited to keep exploring serverless tech and optimizing this architecture!


## Conclusion

The implementation of the "temp" endpoint showcases an effective use of AWS serverless technology to achieve a robust, scalable, and interactive data visualization tool. By combining AWS API Gateway's powerful integration features and the computational flexibility of AWS Lambda functions, the project delivers real-time environmental monitoring efficiently within the AWS Free Tier, ensuring both performance and cost-effectiveness.

