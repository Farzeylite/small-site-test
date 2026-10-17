import os
from flask import *

app = Flask(__name__)

FILES_DIR = os.path.join(app.root_path, 'Downloads')

app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route("/")
def index(name=None):
    return render_template('index.html', person=name)

@app.route("/blog")
def blog(posts=None):
    return render_template('blog.html', all_posts=posts)

@app.route("/creative")
def creative():
    return render_template('creative.html')

@app.route("/downloads")
def downloads():
    try:
        files = os.listdir(FILES_DIR)
    except FileNotFoundError:
        files = []
    return render_template('downloads.html', files=files)

@app.route("/downloads/<filename>")
def download_file(filename):
    try:
        return send_from_directory(FILES_DIR, filename)#, as_atachment=True)
    except:
        abort(404)

if __name__ == "__main__":
    app.run(port=8080, debug=True)