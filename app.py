from flask import  Flask, render_template, request, jsonify

from chatUtils import ask_bot

app = Flask(__name__)

@app.get("/")
def home():
    return render_template("index.html")

@app.get("/test")
def test():
    return "server is working friends"

@app.post("/chat")
def chat():
    text = request.get_json().get("message")    
    model_response = ask_bot(text)
    response = {"data": model_response}
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True, port=3000)