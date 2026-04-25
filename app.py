import json
import os
from flask import Flask, render_template

app = Flask(__name__, template_folder='templates', static_folder='static')

def load_projects():
    # This reads your 'uploads' from the json file
    try:
        with open('projects.json', 'r') as f:
            return json.load(f)
    except:
        return []

@app.route('/')
def home():
    projects = load_projects()
    return render_template('index.html', projects=projects)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
