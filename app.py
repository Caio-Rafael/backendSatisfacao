from flask import Flask, request, render_template
from warnings import filterwarnings
import pickle

filterwarnings('ignore')
 
def import_model(): 
    # Abre o modelo treinado
    modelo = pickle.load(open('RL_Satisfacao_v1.1.pkl', 'rb'))
    return modelo

modelo = import_model()
app = Flask(__name__)

@app.route('/') 
def index():
    return render_template('forms_satisfacao.html')

@app.route('/predict', methods=['POST']) 
def predict():
    # Obter os parâmetros do formulário
    parametros = [
        float(request.form['Customer Type_Encoded']),
        float(request.form['Age']), 
        float(request.form['Type of Travel_Encoded']),
        float(request.form['Class_Encoded']), 
        float(request.form['Flight Distance']), 
        float(request.form['Seat comfort']), 
        float(request.form['Departure/Arrival time convenient']),
        float(request.form['Food and drink']), 
        float(request.form['Gate location']), 
        float(request.form['Inflight wifi service']), 
        float(request.form['Inflight entertainment']), 
        float(request.form['Online support']), 
        float(request.form['Ease of Online booking']), 
        float(request.form['On-board service']), 
        float(request.form['Leg room service']),
        float(request.form['Baggage handling']), 
        float(request.form['Checkin service']), 
        float(request.form['Cleanliness']), 
        float(request.form['Online boarding']), 
        float(request.form['Departure Delay in Minutes']),
        float(request.form['Arrival Delay in Minutes'])
    ]
    
    # Fazer a predição
    resultado = modelo.predict([parametros])[0]
    
    # Interpretação do resultado
    if resultado == 0: 
        resultado = 'O cliente provavelmente está insatisfeito'
    else:
        resultado = 'O cliente provavelmente está satisfeito'

    return render_template('resultado.html', resultado=resultado)

if __name__ == '__main__':
    app.run(
        debug=True,
        port=5000
    )
