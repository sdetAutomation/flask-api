import requests

from flask import Flask

app = Flask(__name__)


@app.route('/')
def rest_call_to_another_other_api():
    url = 'https://springboot-gradle.herokuapp.com/locations/v1'
    return requests.get(url).content


if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
