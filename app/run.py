from src import app

"""
This is the main file that starts the flask server and serves the web app UI in the browser.

To run, type in terminal:

python run.py
"""

if __name__ == '__main__':
    app.run(debug=True, port=5000)
