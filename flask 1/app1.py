from flask import Flask

# Creating the name of the app i.e module
app = Flask(__name__)

# Creating endpoints i.e address
# Multiple endpoints for same address
# The name of the function inside the route should be different for each route
@app.route('/')
@app.route('/home')
def home():
    return "<h1>This is the home page<h1>"

# Path parameters. Here, by default path parameters are strings.
@app.route('/<name>')
def name(name):
    return f"<h1>Welcome {name.title()}</h1>"
#Here the title() function caps the first letter of the string

# For integer path parameters
@app.route('/<int:num>')
def integer(num):
    return f'<h1>The integer is {num}</h1>'

@app.route('/<int:num1>/<int:num2>')
def integerSum(num1,num2):
    return f"<h1>The sum is {num1+num2}</h1>"

@app.route('/about')
def about():
    return "<h1>This is the about page<h1>"

''' 
Starting the app
It is necessary to write name==main because name is equal to main only inside the scope of the file that is currently running so for 
other files, name is equal to the name of the file itself and the file only runs if it is run sitting inside the file but if the file 
is run from outside the file then the file is not executed but the classes inside the file can be inherited.
'''
if __name__=='__main__':
    app.run(debug=True)
