from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Logique métier séparée pour pouvoir la tester facilement
def calculate(a, b, op):
    if op == 'add': return a + b
    if op == 'sub': return a - b
    if op == 'mul': return a * b
    if op == 'div': return a / b if b != 0 else "Erreur: Division par 0"
    return "Opération invalide"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/calc', methods=['POST'])
def calc():
    data = request.json
    try:
        a = float(data['a'])
        b = float(data['b'])
        res = calculate(a, b, data['op'])
        return jsonify({'result': res})
    except ValueError:
        return jsonify({'result': "Erreur: Entrée invalide"})

if __name__ == '__main__':
    app.run(port=5000)
