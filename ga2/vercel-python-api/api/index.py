import json

# Load the marks data from the JSON file when the module is imported.
# Make sure that the file is located at the root of your project.
with open('q-vercel-python.json') as f:
    student_marks = json.load(f)

def handler(request):
    """
    Vercel will call this function on each request.
    The request object behaves like Flask's request.
    """
    # Retrieve all occurrences of the "name" query parameter.
    # For example, for ?name=X&name=Y, this returns ["X", "Y"].
    names = request.args.getlist("name")
    
    # Look up each name in the student_marks dictionary.
    # If a name isn't found, you can decide to return None (or any other default value).
    marks = [student_marks.get(name, None) for name in names]

    # Create the JSON response body.
    response_body = json.dumps({"marks": marks})
    
    # Include CORS headers to allow GET requests from any origin.
    headers = {
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin": "*"
    }
    
    # Return the response in the format Vercel expects.
    return {
        "statusCode": 200,
        "headers": headers,
        "body": response_body
    }


if __name__ == "__main__":
    from flask import Flask, request
    app = Flask(__name__)

    @app.route("/api", methods=["GET"])
    def api():
        return handler(request)

    app.run(host="0.0.0.0", port=5000)