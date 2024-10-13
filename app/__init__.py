from flask import Flask

app = Flask(__name__)

from app import routes  # Import the routes after creating the app
