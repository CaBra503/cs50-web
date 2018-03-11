from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, World"


@app.route("/<string:name>")
def hello(name):
    name = name.capitalize()
    return f"<h1>hello, {name}!!<h1>"

if __name__ == "__main__":
    app.run()

