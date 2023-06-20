#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)
    return parameter

@app.route('/count/<int:param>')
def count(param):    
    return '\n'.join(str(num) for num in range(0, param + 1)) 

@app.route('/math/<int:num1><string:operation><int:num2>')
def math(num1, num2, operation):
    if operation == '+':
        return f'{num1 + num2}\n'
    elif operation == '-':
        return f'{num1 - num2}\n'
    elif operation == '*':
        return f'{num1 * num2}\n'
    elif operation == 'div':
        if num2 != 0:
            return f'{num1 / num2}\n'
        else:
            return 'Error: Division by zero is not allowed.\n'
    elif operation == '%':
        return f'{num1 % num2}\n'
    else:
        return 'Operation not recognized. Please use one of the following: + - * div %'
    
if __name__ == '__main__':
    app.run(port=5555, debug=True)
