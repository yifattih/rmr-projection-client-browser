from flask import render_template, request, jsonify
from app import app
from .bmr import model
from .bmr.helpers import type_alias

# To hold the data for the table on buffer
data_input = []
data_output = []

def process_data_in(data: type_alias.JSONType) -> dict[str, str | type_alias.number]:
    return {"weight": float(data["weight"]),
            "height": float(data["height"]),
            "age": int(data["age"]),
            "time": int(data["time"])}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/data-in',
           methods=['GET'])
def get_data_in():
    return jsonify(data_input)

@app.route('/data-out',
           methods=['GET'])
def get_data_out():
    return jsonify(data_output)

@app.route('/model-construct',
           methods=['POST'])
def model_construct():
    # Get data from AJAX request
    data_in = request.json
    data_in = process_data_in(data=data_in)
    # Calculate output from model
    data_out = model.construct(data=data_in)
    
    data_input.append(data_in)
    data_output.append(data_out)

    response = {
        "message": "Data processed!",
        "status": "Success!",
        "data_out": data_output
        }

    return jsonify(response)

@app.route('/reset', methods=['POST'])
def clear():
    # Get data from AJAX request
    data_input.clear()
    data_output.clear()
    
    response = {"message": "Data cleared!",
                "status": "success"}

    return jsonify(response)
