from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    first_number = data['firstNumber']
    second_number = data['secondNumber']
    operation = data['operation']

    print(f'First Number is {first_number}')

    if operation == 'add':
        result = first_number + second_number
    elif operation == 'subtract':
        result = first_number - second_number
    elif operation == 'multiply':
        result = first_number * second_number
    elif operation == 'divide':
        result = first_number / second_number
    else:
        result = 'Invalid Operation'

    return jsonify(result=result)

if __name__ == '__main__':
    app.run(debug=True)
