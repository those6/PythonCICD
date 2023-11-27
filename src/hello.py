from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, Derik"
    
if __name__ == "__main__":
    app.run()