import datetime
import time
from flask import Flask, abort

app = Flask(__name__)


@app.route('/')
def root():
    return "Thank you for hitting the centralized api root endpoint...try hitting the error endpoints please"

@app.route("/four-zero-zero")
def four_zero_zero():
    return abort(400, "Bad Request")

@app.route("/four-zero-one")
def four_zero_one_abort():
    return abort(401, "This resource is not authorized for your credentials")

@app.route("/four-zero-four")
def four_zero_four_abort():
    return abort(404, "Not Found")

@app.route("/four-zero-eight")
def four_zero_eight_abort():
    # time.sleep(5)
    return abort(408, "Request Timeout")

@app.route("/four-one-eight")
def four_one_eight_abort():
    return abort(418, "You hit the Teapot endpoint...LOL")

@app.route("/five-zero-zero")
def five_zero_zero_abort():
    return abort(500, "Internal Server Error")

@app.route("/five-zero-one")
def five_zero_one_abort():
    return abort(501, "Not yet implemented")

@app.route("/five-zero-three")
def five_zero_three_abort():
    return abort(503, "Server is down temporarily.")

# With params example
# @app.route('/name/<name>')
# def hello_name(name):
#     return f"Hello, {name}"





# Necessary... don't know why yet, need research
if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    # Flask's development server will automatically serve static files in
    # the "static" directory. See:
    # http://flask.pocoo.org/docs/1.0/quickstart/#static-files. Once deployed,
    # App Engine itself will serve those files as configured in app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)


