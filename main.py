from flask import Flask, request, jsonify
import json

app = Flask(__name__)

global data


with open('data.json') as f:
    data = json.load(f)




@app.route('/students')
def get_students():
  result = []
  pref = request.args.get('pref') 
  if pref:
    for student in data: 
      if student['pref'] == pref: 
        result.append(student) 
    return jsonify(result)
  return jsonify(data)


@app.route('/stats')
def get_stats():
    meal_preferences = {}
    programmes = {}

    for student in data:
        
        meal_pref = student.get('pref')
        if meal_pref:
            meal_preferences[meal_pref] = meal_preferences.get(meal_pref, 0) + 1

        
        programme = student.get('programme')
        if programme:
            programmes[programme] = programmes.get(programme, 0) + 1

   
    stats = {
        'meal_preferences': meal_preferences,
        'programmes': programmes
    }

    return jsonify(stats)  


@app.route('/add/<int:a>/<int:b>')
def add(a, b):
    result = a + b
    return jsonify({'operation': 'add', 'a': a, 'b': b, 'result': result})

@app.route('/subtract/<int:a>/<int:b>')
def subtract(a, b):
    result = a - b
    return jsonify({'operation': 'subtract', 'a': a, 'b': b, 'result': result})

@app.route('/multiply/<int:a>/<int:b>')
def multiply(a, b):
    result = a * b
    return jsonify({'operation': 'multiply', 'a': a, 'b': b, 'result': result})

@app.route('/divide/<int:a>/<int:b>')
def divide(a, b):
    if b == 0:
        return jsonify({'error': 'Division by zero is not allowed'}), 400
    result = a / b
    return jsonify({'operation': 'divide', 'a': a, 'b': b, 'result': result})

app.run(host='0.0.0.0', port=8080, debug=True)
