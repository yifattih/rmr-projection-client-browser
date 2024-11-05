from flask import Flask

app = Flask(__name__)

from src import routes  # Import the routes after creating the app
