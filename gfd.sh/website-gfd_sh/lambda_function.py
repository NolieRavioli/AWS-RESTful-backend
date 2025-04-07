import os

def lambda_handler(event, context):
    # Extract the path from the event (default to "/" if not present).
    path = event["path"]
    if path != '/':
        path_parts = path.split('/')
        if path[0] == '/':
            path_parts = path_parts[1:]
        file_path = os.path.join(os.path.dirname(__file__), "www",*path_parts, "index.html")
    else:
        file_path = os.path.join(os.path.dirname(__file__), "www","index.html")

    # Read and return the appropriate HTML file.
    try:
        with open(file_path, "r") as f:
            html_content = f.read()

        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "text/html"
            },
            "body": html_content
        }
    except FileNotFoundError:
        # In case the file doesn't exist for some reason.
        return {
            "statusCode": 404,
            "headers": {"Content-Type": "text/plain"},
            "body": "404 Not Found"
        }