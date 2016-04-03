from app import app
from flask import render_template
from flask import request


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")


@app.route('/shutdown')
def shutdown():
    shutdown_server()
    return 'Server shutting down...'


def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()