import flask
import werkzeug
import numpy as np
import json
from inference import FoodRecognitionHandler

ROOT = 'C:/Users/Andre/Documents/CVC-TheDons/'
DAMAGE_MODEL_PATH = ROOT + '/AiModels/carDamage/results/exp/checkpoints/16.pth'
BRANDS_MODEL_PATH = ROOT + '/AiModels/carBrands/results/exp/checkpoints/37.pth'

# load numpy array with the classes
damageClasses = np.load(ROOT + '/Flask/resources/damageClasses.npy')
brandsClasses = np.load(ROOT + '/Flask/resources/brandsClasses.npy')
handlerDamage = FoodRecognitionHandler(DAMAGE_MODEL_PATH, damageClasses)
handlerBrands = FoodRecognitionHandler(BRANDS_MODEL_PATH, brandsClasses)

currentPriceIndex = 0

app = flask.Flask(__name__)
@app.route('/', methods = ['GET', 'POST'])

def handle_request():
    imagefile = flask.request.files['image']
    filename = werkzeug.utils.secure_filename(imagefile.filename)
    print("\nReceived image File name : " + imagefile.filename)
    imagefile.save(filename)
    model = 0
    if imagefile.filename == 'brandImage.jpg':
        model = 1
    else:
        model = 2

    priceindex = {'AUDI-A4' : 1.25, 'BMW-SERIA3': 1.25, 'BMW-X5': 1.75, 'CHEVROLETE-CORVETTE': 2.5,
                  'FORD-MUSTANG': 2 , 'HONDA-CIVIC': 0.75, 'MAZDA-3': 0.75, 'MERCEDES-BENZ-SKLASS': 1.5,
                  'MINI-COOPER': 1, 'TOYOTA-PRIUS': 1, 'VOLKSWAGEN-BEETLE': 0.75, 'VOLKSWAGEN-GOLF': 0.5,
                  'VOLKSWAGEN-PASSAT': 0.75}
    repairCost = {'bumper_dent': 375, 'bumper_scratch': 300, 'crashed': 2500, 'door_dent': 300, 'door_scratch': 200, 'glass_shatter': 300, 'head_lamp': 425, 'no_damage': 0, 'tail_lamp': 325}
    #get predictions
    global currentPriceIndex
    if model == 1:
        prediction = handlerBrands.predict(filename)
        currentPriceIndex = priceindex[prediction]
        return " ".join(prediction.split('-'))
    else:
        prediction = handlerDamage.predict(filename)
        currentRepairCost = currentPriceIndex * repairCost[prediction]
        prediction = prediction.upper()
        return " ".join(prediction.split('_')) + '\n' + 'Repair cost: ' + str(int(currentRepairCost))


app.run(host="0.0.0.0", port=5000, debug=True)
