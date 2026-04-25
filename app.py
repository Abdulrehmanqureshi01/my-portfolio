from flask import Flask, render_template
import os

app = Flask(__name__, 
            template_folder='templates', 
            static_folder='static')

@app.route('/')
def home():
    # You can add your actual projects here later
    project_list = [
        {"title": "E-Commerce Solution", "impact": "50% Sales Boost", "status": "Completed"},
        {"title": "AI Dashboard", "impact": "High Efficiency", "status": "Live"},
        {"title": "Brand Identity", "impact": "Market Growth", "status": "Active"}
    ]
    return render_template('index.html', projects=project_list)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
