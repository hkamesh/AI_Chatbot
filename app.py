from flask import Flask, render_template, request, jsonify
from chatbot import get_response

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get', methods=['GET'])
def get_bot_response():
    user_input = request.args.get('msg')
    if user_input:
        response = get_response(user_input)
        return jsonify(response=response)
    return jsonify(response="Please enter a valid question.")

if __name__ == '__main__':
    app.run(debug=True)
