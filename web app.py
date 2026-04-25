from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def home():
    # This data will show up in your "Mesmerizing" cards
    project_list = [
        {
            "title": "Creative UI Engine", 
            "impact": "Increased conversion by 40%", 
            "status": "Live"
        },
        {
            "title": "Blockchain Visualizer", 
            "impact": "High-impact data design", 
            "status": "In Progress"
        }
    ]
    # The '12' is your client count - update it as you grow!
    return render_template('index.html', projects=project_list, client_count=12)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)