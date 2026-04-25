from flask import Flask, render_template
import os

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/')
def home():
    # Final Project List with Professional Tech Thumbnails
    project_list = [
        {
            "title": "E-Commerce Ecosystem", 
            "impact": "40% Revenue Growth", 
            "status": "Live",
            "image": "https://images.unsplash.com/photo-1557821552-17105176677c?q=80&w=800"
        },
        {
            "title": "AI Analytics Portal", 
            "impact": "Real-time Data Scaling", 
            "status": "Completed",
            "image": "https://images.unsplash.com/photo-1551288049-bebda4e38f71?q=80&w=800"
        },
        {
            "title": "Modern Brand Revamp", 
            "impact": "Market-Leading Identity", 
            "status": "Active",
            "image": "https://images.unsplash.com/photo-1542744094-3a31f272c490?q=80&w=800"
        }
    ]
    
    return render_template('index.html', projects=project_list)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
