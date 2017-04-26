from flask import Flask
from flask import render_template
import requests

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/get_data')
def get_amazon_data():
    response = requests.get('https://w06sur7dz1.execute-api.us-east-1.amazonaws.com/prod/HabiTrackerUpdate?TableName=HabitTracker')
    return response.text

# @app.route('/post_user', methods=["Post"])
# def post_user():


if __name__ == '__main__':
    app.run(debug=True)
