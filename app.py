from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# To hold the data for the table
data_store = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    # Get data from AJAX request
    new_data = request.json
    data_store.append(new_data)
    return jsonify(data_store)

@app.route('/clear', methods=['POST'])
def clear():
    # Get data from AJAX request
    data_store.clear()
    return jsonify(data_store)

@app.route('/data', methods=['GET'])
def get_data():
    return jsonify(data_store)

if __name__ == '__main__':
    app.run(debug=True)