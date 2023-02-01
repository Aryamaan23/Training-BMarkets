from flask import Flask
import logging

app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)

@app.route('/')
def hello_world():
    app.logger.info('Processing default request')
    return 'Hello World!'

if __name__ == '__main__':
    app.run()