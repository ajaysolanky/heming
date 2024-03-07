import os
from flask import Flask, request, jsonify
from review_functions import get_passage_edits
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/review', methods=['POST'])
def review_text():
    data = request.json
    passage = data['passage']
    instruction = data['instruction']
    model = data['model']
    return jsonify(get_passage_edits(instruction, passage, model))

if __name__ == '__main__':
    app.run(debug=True)