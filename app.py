from flask import Flask, render_template
import os

# This line tells Flask EXACTLY where your folders are
app = Flask(__name__, 
            template_folder='templates', 
            static_folder='static')

@app.route('/')
def home():
    project_list = [
        {"title": "Creative UI Engine", "impact": "40% Growth", "status": "Live"},
        {"title": "AI Content Hub", "impact": "High Scale", "status": "Active"}
    ]
    return render_template('index.html', projects=project_list, client_count=12)

if __name__ == "__main__":
    # Render uses the PORT environment variable
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
