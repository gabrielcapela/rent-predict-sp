from flask import Flask, render_template, request
import pickle
import numpy as np

# Inicializa o Flask
app = Flask(__name__)

# Carrega o modelo
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Suponha que você espera 3 inputs numéricos do usuário
    inputs = [float(x) for x in request.form.values()]
    final_input = np.array(inputs).reshape(1, -1)
    prediction = model.predict(final_input)
    return render_template('index.html', prediction_text=f'Predição: R$ {prediction[0]:,.2f}')

if __name__ == "__main__":
    app.run(debug=True)
