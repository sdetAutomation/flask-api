from flask import Response
from config import my_app


def welcome():
    response_text = '{ "message": "Hello, welcome to sdetAutomation flask-api" }'
    response = Response(response_text, 200, mimetype='application/json')
    return response


def health():
    response_text = '{ "status": "OK" }'
    response = Response(response_text, 200, mimetype='application/json')
    return response


if __name__ == '__main__':
    my_app.run(host='0.0.0.0', port=5000, debug=True)
