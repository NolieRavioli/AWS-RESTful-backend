import os
import boto3
import base64
import requests

PRE_SHARED_TOKEN = os.environ.get("PRE_SHARED_TOKEN")

def lambda_handler(event, context):
    """Entry point for API Gateway -> Lambda integration."""
    
    http_method = event.get('httpMethod', '')
    headers = event.get('headers', {})
    # Route by HTTP method
    if http_method == 'POST':
        # Auth Check
        auth_header = headers.get('Authorization', '')
        if not auth_header.startswith("Bearer "):
            return response(401, "Unauthorized")
        
        # Extract token from 'Bearer XXXXXX'
        _, token_value = auth_header.split(" ")
        if token_value != PRE_SHARED_TOKEN:
            return response(401, "Invalid token.")
        return post_data(event)
    elif http_method == 'GET':
        return get_data()
    else:
        return response(405, f"Method {http_method} not allowed.")

def post_data(event):
    """
    1) Extract body from 'event'
    2) POST it to the self-hosted service https://cpu1.nolp.net/data
    """
    body = event.get('body', '')
    auth_header = event['headers']['Authorization']

    is_b64 = event.get('isBase64Encoded', False)
    
    try:
        # If the request from API Gateway is base64-encoded
        data = base64.b64decode(body) if is_b64 else body.encode("utf-8")
    except Exception as e:
        return response(400, f"Error decoding body: {e}")
    
    try:
        resp = requests.post('https://cpu1.nolp.net/data', headers={'Authorization':auth_header}, data=data, timeout=2, allow_redirects=False)
        if resp.status_code in (301, 302, 303, 307):
            new_url = resp.headers.get('location')
            print("Redirecting to:", new_url)
            # Manually issue the POST request to the new URL
            resp = requests.post(new_url)
        print("Final Response Text:", resp.text)
        if resp.status_code != 200:
            return response(500, f"Self-host error: {resp.status_code} {resp.text}")
        return response(200, "Data stored successfully on self-host.")
    except requests.exceptions.RequestException as e:
        return response(502, f"Error reaching self-host: {str(e)}")

def get_data():
    """
    1) Try to get data from self-host http://cpu1.nolp.net/data
    2) If unsuccessful, fallback to S3
    """
    return response(200, requests.get('https://cpu1.nolp.net/data').text)
    try:
        resp = requests.get('https://cpu1.nolp.net/data', timeout=2)
        if resp.status_code == 200:
            # Return that data

            return response(200, resp.text)  # or base64 if it's binary
        else:
            # fallback to S3
            return get_data_from_s3()
    except requests.exceptions.RequestException:
        # fallback to S3
        return get_data_from_s3()

def get_data_from_s3():
    """Fetch data from S3 if self-host is unreachable or returns error."""
    s3 = boto3.client('s3')
    bucket_name = "hondo-cabin"
    object_key = "YOUR_OBJECT_KEY"
    
    try:
        obj = s3.get_object(Bucket=bucket_name, Key=object_key)
        data = obj['Body'].read()
        # Return as text or base64
        return response(200, data.decode('utf-8'))
    except Exception as e:
        return response(503, f"S3 backup also unavailable: {e}")

def response(status_code, message):
    """Helper to return a structured JSON response to API Gateway."""
    return {
        'statusCode': status_code,
        'headers': { 'Content-Type': 'text/plain' },
        'body': message
    }
