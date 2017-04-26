from flask import Flask
from flask import render_template, request
import requests

app = Flask(__name__)

url = 'https://w06sur7dz1.execute-api.us-east-1.amazonaws.com/prod/HabiTrackerUpdate?TableName=HabitTracker'

@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/get_data', methods=['GET', 'POST'])
def get_amazon_data():
    if request.method == 'GET':
        response = requests.get(url)
        return response.text
    else:
        r = requests.post(url, data=request.data)
        return r.text


if __name__ == '__main__':
    app.run(debug=True)
