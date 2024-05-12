import json
import pickle
import numpy as np
import warnings

warnings.filterwarnings('ignore')

__car_models = []
__engine_models = []
__gearbox_models = []
__transmitter_models = []
__data_columns = []
__model = []


def get_estimated_price(car_model: str, engine_type: str, gearbox_type: str, transmitter_type: str, year: int,
                        engine_volume: float, horse_power: int, mileage: float) -> str:
    try:
        car_model_index = __data_columns.index(f'model_{car_model.lower()}')
    except:
        car_model = 'other'
    try:
        engine_type_index = __data_columns.index(f'engine_type_{engine_type.lower()}')
    except:
        engine_type = 'benzin'
    try:
        gearbox_type_index = __data_columns.index(f'gearbox_{gearbox_type.lower()}')
    except:
        gearbox_type = 'avtomat'
    try:
        transmitter_type_index = __data_columns.index(f'transmitter_{transmitter_type.lower()}')
    except:
        transmitter_type = 'Tam'

    X = np.zeros(len(__data_columns))
    X[0] = year
    X[1] = engine_volume
    X[2] = horse_power
    X[3] = mileage

    X[car_model_index] = 1
    X[engine_type_index] = 1
    X[gearbox_type_index] = 1
    X[transmitter_type_index] = 1

    ans = round(__model.predict([X])[0], 2)

    return f'{ans}'


def load_saved_artifacts() -> None:
    print('loading saved artifacts . . .start')
    global __car_models
    global __engine_models
    global __gearbox_models
    global __transmitter_models
    global __data_columns
    global __model

    with open('./artifacts/columns.json', 'r') as f:
        __data_columns = json.load(f)['data_columns']
        __car_models = __data_columns[4: 417]
        __engine_models = __data_columns[417: 422]
        __gearbox_models = __data_columns[422: 426]
        __transmitter_models = __data_columns[426:]
        for i in range(len(__car_models)):
            __car_models[i] = __car_models[i][6:]
        for i in range(len(__engine_models)):
            __engine_models[i] = __engine_models[i][12:]
        for i in range(len(__gearbox_models)):
            __gearbox_models[i] = __gearbox_models[i][8:]
        for i in range(len(__transmitter_models)):
            __transmitter_models[i] = __transmitter_models[i][12:]

    with open('./artifacts/car_prices_model.pickle', 'rb') as f:
        __model = pickle.load(f)

    print('loading saved artifacts . . .done')


if __name__ == '__main__':
    load_saved_artifacts()
    for i in range(len(__data_columns)):
        print(i, __data_columns[i])
    print(__car_models)
    print(__engine_models)
    print(__gearbox_models)
    print(__transmitter_models)
    print(get_estimated_price('Kia Sorento', 'Dizel', 'Avtomat', 'Ön', 2011, 2.0, 184, 206000))
