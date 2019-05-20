from flask import Flask, render_template, request
import requests

webserver = Flask(__name__)

@webserver.route("/")
def home():
    return render_template("index.html"), 200

@webserver.route("/go")
def go():
    r = request.args.get('r')
    w = requests.request(request.method, r)
    return w.content, 200

if (__name__ == "__main__"):
    webserver.run(debug=True, port=5055)