# AWS-RESTful-backend
A document of how my restful, free, aws-powered load-balancer works.

## Intro

Using AWS Free Tier Lambda and API Gateway, I created an interface for serving content from across the internet through a single cloud integration. This project demonstrates how to leverage serverless architecture to build a scalable and cost-effective load balancer.

## Features

- **Serverless Architecture:** Utilizes AWS Lambda for compute and API Gateway for exposing RESTful endpoints.
- **Load Balancing:** Distributes requests across multiple endpoints to ensure high availability.
- **Costless:** Designed to work within the AWS Free Tier. 
- **Scalable:** Easily adapts to varying levels of incoming traffic.
- **API Gateway:** Acts as the entry point for incoming HTTP requests.
- **AWS Lambda:** Processes the requests and routes them to the appropriate external endpoints.
- **External Endpoints:** The actual sources of content/data which are aggregated by the Lambda function.

## How It Works

1. **Request Reception:**  
   When a user sends an HTTP request, API Gateway receives it and triggers a corresponding AWS Lambda function.

2. **Request Processing:**  
   The Lambda function evaluates the request, applies load balancing logic, and determines which external endpoint should handle the request.

3. **Response Aggregation:**  
   The Lambda function forwards the request to the selected external endpoint, retrieves the response, and sends it back through API Gateway to the user.

## [nolanpeet.us](https://nolanpeet.us) (external link)
[[Source Code](https://github.com/NolieRavioli/AWS-RESTful-backend/tree/main/website-nolanpeet_us)]
This website was designed to serve as a functional model of my knowledge base and custom framework. The inherent challenges of building a serverless website using AWS Lambda functions was a really interesting
opportunity to explore the limits and capabilities of serverless architecture. My goal was to create a serverless "blog" where I can showcase updates and portfolio items, all while avoiding an over-reliance on external resources.

I spent a ton of time hand-coding HTML and CSS for the webpage. It was cool  This project was especially exciting because of Amazon Q. I like to use ChatGPT to code but this was my first experience having an integrated assistant 
inside the coding environment (I use IDLE). It felt really nice to tab complete whole codeblocks with just a single line to nucleate from. Also, if I forget how to do a specific function I can just comment what I want to be done in
psydo-code or plaintext and have the integrated assistant help me remember syntax!
