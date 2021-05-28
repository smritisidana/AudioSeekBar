from flask import *

app = Flask(__name__, template_folder='template', static_url_path='')
app.config['DEBUG'] = True

@app.route('/play')
def main():
        return render_template("index.html")

@app.route('/audio/<path:path>')
def audio(path):
        return send_from_directory('template/audio', path)
app.run()