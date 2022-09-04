from distutils.log import debug
from urllib import response
from flask import Flask, request, jsonify , render_template
import util

app = Flask(__name__)


@app.route('/engine_locations', methods=['GET'])
def engine_location():
    response = jsonify({
        'engine_locations': util.engine_location_util()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


@app.route('/fuel_type', methods=['GET'])
def fuel_type():
    response = jsonify({
        'fuel_type': util.fuel_type_util()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


@app.route('/odometer', methods=['GET'])
def odometer():
    response = jsonify({
        'odometer': util.odometer_util()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


@app.route('/speedometer', methods=['GET'])
def speedometer():
    response = jsonify({
        'speedometer': util.speedometer_util()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


@app.route('/seats_material', methods=['GET'])
def Seats_material():
    response = jsonify({
        'seats_material': util.Seats_material_util()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


@app.route('/audiosystem', methods=['GET'])
def audiosystem():
    response = jsonify({
        'audiosystem': util.audiosystem_util()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


@app.route('/predict', methods=['GET', 'POST'])
def predict():

    engine_location = request.form['engine_location']
    odometer = request.form['odometer']
    speedometer = request.form['speedometer']
    seats_material = request.form['seats_material']
    audiosystem = request.form['audiosystem']
    fuel_type = request.form['fuel_type']
    Fuel_Tank_Capacity = int(request.form['Fuel_Tank_Capacity'])
    Height = int(request.form['Height'])
    Length = int(request.form['Length'])
    Width = int(request.form['Width'])
    City_Mileage = float(request.form['City_Mileage'])
    Gears = int(request.form['Gears'])
    Seating_Capacity = int(request.form['Seating_Capacity'])
    Number_of_Airbags = int(request.form['Number_of_Airbags'])

    response = jsonify({
        'estimated_price': util.estimated_price(engine_location, odometer, speedometer, seats_material, audiosystem, fuel_type, Fuel_Tank_Capacity, Height, Length, Width, City_Mileage, Gears, Seating_Capacity, Number_of_Airbags)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictor')
def predictor():
    return render_template('form.html')

@app.route('/price')
def price():
    return render_template('results.html')

# app = Flask(__name__, static_url_path='/static')

@app.route('/results')
def results():
    return render_template('results.html')

if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    util.load_saved_artifacts()
    app.run(debug=True)