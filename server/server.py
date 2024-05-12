from flask import Flask, request, jsonify
import util

app = Flask(__name__)


@app.route('/get_estimated_price', methods=['GET', 'POST'])
def get_estimated_price():
    car_model = request.form['car_model']
    engine_type = request.form['engine_type']
    gearbox_type = request.form['gearbox_type']
    transmitter_type = request.form['transmitter_type']
    year = int(request.form['year'])
    engine_volume = float(request.form['engine_volume'])
    horse_power = float(request.form['horse_power'])
    mileage = float(request.form['mileage'])

    response = jsonify({
        'estimated_price': util.get_estimated_price(car_model, engine_type, gearbox_type, transmitter_type, year, engine_volume, horse_power, mileage)
    })

    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/get_car_models', methods=['GET', 'POST'])
def get_car_models():
    response = jsonify({
        'car_models': util.get_car_models()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == '__main__':
    print('Starting Python Flask Server For Car Price Prediction . . .')
    util.load_saved_artifacts()
    app.run()
