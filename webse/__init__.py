from flask import Flask

application = Flask(__name__)

from webse.home.routes import home

application.register_blueprint(home)