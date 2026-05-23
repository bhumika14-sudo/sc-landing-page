import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from flask import Flask, render_template, send_from_directory

# Get the parent directory of the api folder
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

app = Flask(__name__, 
            template_folder=os.path.join(BASE_DIR, 'templates'),
            static_folder=os.path.join(BASE_DIR, 'static'),
            static_url_path='/static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory(os.path.join(BASE_DIR, 'static'), path)

@app.route('/<path:path>')
def catch_all(path):
    # For any other route, serve index.html (SPA behavior)
    return render_template('index.html')

@app.errorhandler(404)
def not_found(error):
    return render_template('index.html'), 200
