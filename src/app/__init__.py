from flask import Flask
from src.app.Controllers.Controllers import main

app = Flask(__name__)

app.register_blueprint(main, url_prefix='/')
