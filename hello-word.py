from flask import Flask, jsonify

app = Flask(__name__)


# string_html = "<center><u style='color: red'><h1 style='color: red; font-family: Arial'>Home Page</h1></u></center> " \
#              "<center><h2> rsrsrsrsrs </h2></center> <input type='submit' value='Tô testando só'>  <input " \
#              "type='submit' value='Tô testando só 2'> <h1> Let's go dude, i played that shi* perfect!!</h1>"

# Student = [
#    {
#        'id': 1,
#        'firstName': 'Aditya',
#        'lastName': 'Malviya',
#        'age': '24'
#    },
#    {
#        'id': 2,
#        'firstName': 'Aman',
#        'lastName': 'Mehta',
#        'age': '25'
#    },
#    {
#        'id': 3,
#        'firstName': 'Nuclear',
#        'lastName': 'Geeks',
#        'age': '26'
#    }
# ]


@app.route('/helloworld-api')
def hello_world():
    return 'Hello, World!'
    # jsonify({'tasks': Student})


#@app.route('/api-do-mayer/da-json-ae')
#def req_json():
#    return jsonify({'task': Student})


app.run()
