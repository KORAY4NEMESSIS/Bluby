from flask import Flask, request, jsonify
from flask_cors import CORS
import random
import os
import json

app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})

try:
    with open("data.json", "r", encoding="utf-8") as admins_file:
        data_base = json.load(admins_file)
except (FileNotFoundError, json.JSONDecodeError):
    data_base = {}

@app.route('/project', methods=['GET'])
def get_project():
    language = request.args.get('language')
    projects = data_base.get(language, []) 
    if projects:
        project = random.choice(projects)
        return jsonify({"project": project})
    else:
        return jsonify({"error": "Langage non supporté"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
