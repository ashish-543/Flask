from flask import Flask,redirect,url_for

app=Flask(__name__)


@app.route('/')
def home():
    return f"<h1>Welcome to the homepage</h1>"

@app.route('/pass')
def passed():
    return f"<h1>Congratulations, You have pased</h1>"

@app.route('/fail')
def failed():
    return f"<h1>sorry you have failed</h1>"

# Here to redirect to another endpoint, the name of the function inside the endpoint should be specified.
# We have to import redrect an url_for function
@app.route('/score/<name>/<int:marks>')
def score(name,marks):
    if marks>50:
        return redirect(url_for('passed'))
    else:
        return redirect(url_for('failed'))


if __name__ == '__main__':
    app.run(debug=True)