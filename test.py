from flask import Flask
import json
app = Flask(__name__)


@app.route('/')
def index():
    response = {"body": "Hello, world!"}
    return json.dumps(response)


# We only need this for local development.
if __name__ == '__main__':
    app.run()
