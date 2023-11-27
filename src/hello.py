from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Derik is Awesome!!"
    
if __name__ == "__main__":
    app.run()