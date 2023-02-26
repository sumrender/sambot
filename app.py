from flask import  Flask, render_template, request, jsonify

from chatUtils import get_response

app = Flask(__name__)

@app.get("/")
def home():
    return render_template("index.html")

@app.post("/chat")
def chat():
    text = request.get_json().get("message")    
    model_response = get_response(text)
    response = {"data": model_response}
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True, port=3000)