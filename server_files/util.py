import json , pickle
import numpy as np
# from json import jsonify

def predict_price(type,lease_type,gym,lift,swimming_pool,parking,property_size,bathroom,facing,water_supply,balconies,LIFT,INTERNET,AC,INTERCOM,POOL,FS,SECURITY,SC,PARK,HK,PB,location):    
    
    loc_index = __data_columns.index(location.lower())

    x = np.zeros(len(X.columns))
    x[0] = type
    x[1] = gym
    x[2] = lift
    x[3] = swimming_pool
    x[4] = parking
    x[5] = property_size
    x[6] = bathroom
    x[7] = facing
    x[8] = water_supply
    x[9] = balconies
    x[11] = LIFT
    x[12] = INTERNET
    x[13] = AC
    x[14] = INTERCOM
    x[15] = POOL
    x[16] = FS
    x[17] = SECURITY
    x[18] = SC
    x[19] = PARK
    x[20] = HK
    x[21] = PB
    
    if loc_index >= 0:
        x[loc_index] = 1
    return __model.predict([x])[0]


def load_saved_artifacts() : 
    print("loading saved artifacts")
    global __data_columns
    global __model

    with open("support_files/columns.json" , 'r') as f:
        __data_columns = json.load(f)['data_columns']

    global __model

    with open("support_files/RealEstate.pickle" , 'rb') as f:
        __model = pickle.load(f)

if __name__ == '__main__' :
    load_saved_artifacts()