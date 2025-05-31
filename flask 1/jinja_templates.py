from flask import Flask,render_template,url_for
from employees import employees_data
# Jinja is used for template inheritance. It is written inside {} with placeholder being {{}}.

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html',title='home')

@app.route('/about')
def about():
    return render_template('about.html',title='about')

@app.route('/evaluate/<int:num>')
def evaluate(num):
    return render_template('evaluate.html',title='evaluate',number=num)


@app.route('/employees')
def employees():
    return render_template('employees.html',title='Employees',emp=employees_data)

@app.route('/employees/manager')
def manager():
    return render_template('manager.html',title='Manager',emp=employees_data)


if __name__=='__main__':
    app.run(debug=True)