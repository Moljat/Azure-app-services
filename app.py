from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calcular', methods=['POST'])
def calcular():
    num1 = float(request.form['num1'])
    num2 = float(request.form['num2'])
    operacion = request.form['operacion']

    if operacion == 'sumar':
        resultado = num1 + num2
    elif operacion == 'restar':
        resultado = num1 - num2
    elif operacion == 'multiplicar':
        resultado = num1 * num2
    elif operacion == 'dividir':
        resultado = num1 / num2 if num2 != 0 else 'Error'
    else:
        resultado = 'Operación inválida'

    return render_template('index.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)
