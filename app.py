# importar os pacotes necessários
import pandas as pd
import numpy as np
from flask import Flask, jsonify, request, render_template, redirect, url_for
from flask_restful import Resource, Api
from flask_babel import Babel, gettext
from joblib import load


# instanciar Flask object
app = Flask(__name__)



def get_locale():
    lang = request.args.get('lang')
    if lang in ['pt', 'en']:
        return lang
    return 'pt'

@app.context_processor
def inject_get_locale():
    return dict(get_locale=get_locale)


# Languages configuration
app.config['BABEL_DEFAULT_LOCALE'] = 'pt'
app.config['BABEL_SUPPORTED_LOCALES'] = ['en', 'pt']
babel = Babel(app, locale_selector=get_locale)






# api
api = Api(app)

# carregar modelo
model = load('model/Final_Model.pkl')

# definir nomes das features esperadas (ordem importa!)
feature_names = [
    'Size', 'Rooms', 'Toilets', 'Suites', 'Parking', 
    'Elevator', 'Furnished', 'Swimming Pool', 'New', 'District'
    ]

class PrecoImoveis(Resource):
    def get(self):
        return {'message': 'Use método POST para prever o aluguel'}

    def post(self):
        data = request.get_json(force=True)
        
        try:
            # transformar dados recebidos em DataFrame
            input_data = pd.DataFrame([data], columns=feature_names)
            
            # prever
            prediction = model.predict(input_data)
            return jsonify({'predicted_rent': float(prediction[0])})
        
        except Exception as e:
            return jsonify({'error': str(e)})


api.add_resource(PrecoImoveis, '/predict')

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')



if __name__ == '__main__':
    app.run()





