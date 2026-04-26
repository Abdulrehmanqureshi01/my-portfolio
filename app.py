import json
import os
from flask import Flask, render_template, abort

app = Flask(__name__, template_folder='templates', static_folder='static')

def load_projects():
    try:
        with open('projects.json', 'r') as f:
            return json.load(f)
    except:
        return []

@app.route('/')
def home():
    projects = load_projects()
    return render_template('index.html', projects=projects)

@app.route('/project/<int:project_id>')
def project_detail(project_id):
    projects = load_projects()
    if 0 <= project_id < len(projects):
        return render_template('project.html', project=projects[project_id])
    return abort(404)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
