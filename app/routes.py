from flask import render_template, request, jsonify
from app import app
from .bmr import model
from .bmr.helpers import type_alias

# To hold the data for the table on buffer
data_input = []
data_output = []

def process_data_in(data: type_alias.JSONType) -> dict[str, type_alias.number]:
    return {"weight": float(data["weight"]),
            "height": float(data["height"]),
            "age": int(data["age"]),
            "time": int(data["time"])}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/data',
           methods=['GET'])
def get_data():
    return jsonify(data_input)

@app.route('/calculate',
           methods=['POST'])
def calculate():
    # Get data from AJAX request
    data_in = request.json
    data_in = process_data_in(data=data_in)
    # Calculate output from model
    data_out = model.construct(data=data_in)
    
    data_input.append(data_in)
    data_output.append(data_out)
    print(data_output)

    response_data = {
        "message": "Data received!",
        "data_out": data_output,
        "status": "Success!"
        }

    return jsonify(response_data)

@app.route('/clear', methods=['POST'])
def clear():
    # Get data from AJAX request
    data_input.clear()

    return jsonify(data_input)
