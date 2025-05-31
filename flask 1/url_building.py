from flask import Flask,redirect,url_for
import time

app=Flask(__name__)


@app.route('/')
def home():
    return f"<h1>Welcome to the homepage</h1>"

@app.route('/pass/<sname>/<int:marks>')
def passed(sname,marks):
    return f"<h1>Congratulations {sname.title()}, You have pased with {marks} marks</h1>"

@app.route('/fail/<sname>/<int:marks>')
def failed(sname,marks):
    return f"<h1>sorry {sname.title()} you have failed with {marks} marks</h1>"

# Here to redirect to another endpoint, the name of the function inside the endpoint should be specified.
# We have to import redrect an url_for function
@app.route('/score/<name>/<int:marks>')
def score(name,marks):
    if marks>50:
        time.sleep(1)
        return redirect(url_for('passed',sname=name,marks=marks))
    else:
        time.sleep(1)
        return redirect(url_for('failed',sname=name,marks=marks))
# Here time.sleep() is used to add delaly

if __name__ == '__main__':
    app.run(debug=True)