from chatbot1 import chatbot
from flask import Flask, render_template, request

app = Flask(__name__)
app.static_folder = 'static'

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(chatbot.get_response(userText))
@app.route("/CustomerCare")
def get_human():
    return render_template("index1.html")

if __name__ == "__main__":
    app.run()