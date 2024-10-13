from flask import render_template, request, jsonify
from app import app
from .bmr import model



# To hold the data for the table
data_input = []
data_output = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/data', methods=['GET'])
def get_data():
    return jsonify(data_input)

@app.route('/calculate', methods=['POST'])
def calculate():
    # Get data from AJAX request
    data_in = request.json
    weight_initial = float(data_in.get("weight"))
    height = float(data_in.get("height"))
    age = int(data_in.get("age"))
    time = int(data_in.get("time"))
    # Calculate output from model
    data_out = model.calculate(weight_initial=weight_initial, height=height,
                               age=age, time=time)
    time_range = data_out["time"]
    weight_range = data_out["weight"]
    bmr = data_out["bmr"]

    print("The input data is: ",
          f"Weight: {weight_initial} -- Height: {height} -- Age: {age} -- Time: {time}" )
    print("The output data is: ",
          f"Time: {time_range} -- Weight Range: {weight_range} -- BMR: {bmr}")
    
    data_input.append(data_in)
    data_output.append(data_out)

    response_data = {
        "message": "Data received!",
        "wwight_in": weight_initial,
        "heihgt_in": height,
        "age_in": age,
        "time_in": time,
        "time_range": time_range,
        "weight_range": weight_range,
        "bmr": bmr,
        "status": "Success!",
        # "additional_info": {
            # "length_of_name": len(name),
            # "double_value": float(value) * 2
        # }
    }
    return jsonify(data_input)

@app.route('/clear', methods=['POST'])
def clear():
    # Get data from AJAX request
    data_input.clear()
    return jsonify(data_input)
