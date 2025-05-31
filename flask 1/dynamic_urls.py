from flask import Flask

app=Flask(__name__)

@app.route('/')
def home():
    return f"<h1>Welcome to the homepage</h1>"
'''
@app.route('/welcome/steve')
def welcome_steve():
    return f"<h1>Welcome steve, This is our webpage<h1>"
'''
@app.route('/welcome/<name>')
def welcome(name):
    return f'<h1>Welcome {name.title()}, This is our webpage</h1>'

if __name__ == '__main__':
    app.run(debug=True)
