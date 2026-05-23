import os
from flask import Flask, render_template, send_from_directory

# Get the parent directory (project root)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

# Set template and static folders
app.template_folder = os.path.join(BASE_DIR, 'templates')
app.static_folder = os.path.join(BASE_DIR, 'static')
app.static_url_path = '/static'

@app.route('/')
def index():
    try:
        return render_template('index.html')
    except Exception as e:
        return f"Error: {str(e)}", 500

@app.route('/<path:path>')
def serve_static(path):
    """Serve static files and catch-all for SPA"""
    if path.startswith('static/'):
        return send_from_directory(app.static_folder, path[7:])
    return render_template('index.html')

@app.errorhandler(404)
def handle_404(e):
    return render_template('index.html'), 200
