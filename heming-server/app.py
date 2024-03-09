import os
from flask import Flask, request, jsonify
from review_functions import get_passage_edits
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

response_cache = {}

@app.route('/review', methods=['POST'])
def review_text():
    data = request.json
    passage = data['passage']
    instruction = data['instruction']
    model = data['model']
    key = (passage, instruction, model)
    print("SERVER REQUEST:\n", key)
    if key not in response_cache:
        response_cache[key] = get_passage_edits(instruction, passage, model)
    print("SERVER RESPONSE:\n", response_cache[key])
    return jsonify(response_cache[key])

if __name__ == '__main__':
    app.run(debug=True)