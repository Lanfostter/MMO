from flask import Flask
from flask_restful import Api
from config import Config
app = Flask(__name__)

if __name__ == "__main__":
    config = Config("localhost", "8080", False)
    app.run(config.HOST, config.PORT, config.DEBUG)
