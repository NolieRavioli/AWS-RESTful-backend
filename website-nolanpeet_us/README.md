# [nolanpeet.us](https://nolanpeet.us) (external link)  

### Table of Contents
<ol type='1'>
  <a href="#intro"><li>Intro</li></a>
  <a href="#serverless-architecture"><li>Serverless Architecture</li></a>
  <a href="#issues-with-truly-serverless-solutions"><li>Issues with Truly Serverless Solutions</li></a>
  <a href="#api-gateway"><li>API Gateway</li></a>
</ol>

## Intro

This website was designed to serve as a functional model of my knowledge base and custom framework. The inherent challenges of building a serverless website using AWS Lambda functions was a really interesting
opportunity to explore the limits and capabilities of serverless architecture. My goal was to create a serverless "blog" where I can showcase updates and portfolio items, all while avoiding an over-reliance on external resources.

I spent a ton of time hand-coding HTML and CSS for the webpage. It was cool  This project was especially exciting because of Amazon Q. I like to use ChatGPT to code but this was my first experience having an integrated assistant 
inside the coding environment (I use IDLE). It felt really nice to tab complete whole codeblocks with just a single line to nucleate from. Also, if I forget how to do a specific function I can just comment what I want to be done in
pseudo-code or plaintext and have the integrated assistant help me remember syntax!

## Serverless Architecture

Embarking on this project, I was eager to understand what "RESTful" applications and serverless architecture truly entailed. The experience turned abstract concepts into tangible components—each AWS service played a distinct role in the system. 
For instance, API Gateway handles incoming HTTP requests, while Lambda functions execute the backend logic on demand.

Here is the main logic happening in the python code. This is what serves my pages:
```
if http_method == "GET":
    # Process GET as before
    path = event["path"]
    if path != '/':
        path_parts = path.split('/')
        if path[0] == '/':
            path_parts = path_parts[1:]
        file_path = os.path.join(os.path.dirname(__file__), "www", *path_parts, "index.html")
    else:
        file_path = os.path.join(os.path.dirname(__file__), "www", "index.html")
  
    try:
        with open(file_path, "r") as f:
            html_content = f.read()
        return {
            "statusCode": 200,
            "headers": { "Content-Type": "text/html" },
            "body": html_content
        }
    except FileNotFoundError:
        return {
            "statusCode": 404,
            "headers": {"Content-Type": "text/plain"},
            "body": "404 Not Found"
        }
```
This architecture not only reduces the overhead of maintaining a traditional server but also scales dynamically based on traffic. The project has been a practical lesson in balancing the trade-offs between resource limitations, performance, and cost, 
particularly when operating within the boundaries of the AWS Free Tier.

## Issues with Truly Serverless Solutions

While the allure of serverless architecture is strong, it comes with its own set of challenges—chief among them being data persistence. In a traditional blog or content management 
system, you'd rely on a persistent database to store messages and content. However, AWS Lambda functions are ephemeral and don't support writing to local storage persistently.
To work around this, I developed a serverless sub-function that cleans and formats bbcode-esque messages into HTML code suitable for static webpages. This approach simulates a dynamic content management experience without 
relying on a conventional database. However, it also highlights the limitations of current serverless platforms. In the future, I’d like to explore integrating other AWS services such as DynamoDB or S3 to provide a more robust 
and truly serverless persistence layer while maintaining the cost-effectiveness of the free tier.

## API Gateway

API Gateway is the crucial component that connects my custom domain to the AWS backend. It handles the routing of HTTP requests to the appropriate Lambda functions, ensuring that each user request is processed efficiently. 
One of the standout features of API Gateway is its ability to integrate with custom domains using DNS authentication—this involves verifying ownership via TXT records and linking via CNAME entries.
By leveraging API Gateway, I’ve been able to provide a secure and professional endpoint for my serverless application, masking the underlying complexity of AWS services. Additionally, API Gateway’s built-in monitoring and throttling 
capabilities help ensure that the system remains responsive and secure, even as traffic patterns change over time.
