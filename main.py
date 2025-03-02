from flask import Flask, request, jsonify
import json

app = Flask(__name__)

global data

# read data from file and store in global variable data
with open('data.json') as f:
    data = json.load(f)


@app.route('/')
def hello_world():
    return 'Hello, Welcome to  my INFO 2602 Lab 1!' 

#-----------------------------------------------------------------------------------------------
#This is the first function version:
#@app.route('/students')
#def get_students():
#    return jsonify(data)# return student data in response

#This is the second function version:
#@app.route('/students/<id>')
#def get_student(id):
#  for student in data: 
#    if student['id'] == id: # filter out the students without the specified id
#      return jsonify(student)
#-----------------------------------------------------------------------------------------------

#Final function version:
@app.route('/students')
def get_students():
  result = []
  pref = request.args.get('pref') # get the parameter from url
  if pref:
    for student in data: # iterate dataset
      if student['pref'] == pref: # select only the students with a given meal preference
        result.append(student) # add match student to the result
    return jsonify(result) # return filtered set if parameter is supplied
  return jsonify(data) # return entire dataset if no parameter supplied

#Exercise 1:
@app.route('/stats')
def get_stats():
    meal_preferences = {}
    programmes = {}

    for student in data:
        # Count meal preferences
        meal_pref = student.get('pref')
        if meal_pref:
            meal_preferences[meal_pref] = meal_preferences.get(meal_pref, 0) + 1

        # Count programmes
        programme = student.get('programme')
        if programme:
            programmes[programme] = programmes.get(programme, 0) + 1

    # Combine results into a single response
    stats = {
        'meal_preferences': meal_preferences,
        'programmes': programmes
    }

    return jsonify(stats)  # Returns a JSON response

#Exercise 2:
#In the URL, put it as http://<port>/<operation/<num1>/<num2>
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
