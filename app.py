import json
import os
from flask import Flask, render_template

app = Flask(__name__, template_folder='templates', static_folder='static')

def load_projects():
    # Absolute path check to prevent Error 500
    base_path = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(base_path, 'projects.json')
    try:
        with open(json_path, 'r') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading JSON: {e}")
        return []

@app.route('/')
def home():
    return render_template('index.html', projects=load_projects(), selected_project=None)

@app.route('/project/<int:project_id>')
def project_detail(project_id):
    projects = load_projects()
    # Safety check: is the ID within the list range?
    if projects and 0 <= project_id < len(projects):
        return render_template('index.html', projects=projects, selected_project=projects[project_id])
    return "Project not found", 404

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
