from flask import (
    Flask,
    redirect,
    render_template,
    url_for,
    flash
)
from forms import SignupForm, LoginForm

app = Flask(__name__)
# without csrf token, the form cannot work so we need to provide the csrf token
app.config['SECRET_KEY'] = 'this_is_a_secret_key'

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html',title='home')

# to let the flask know that when we are working with post request inside the signup endpoint, we write method=post 
# but the action is empty so we need to write get as well as post method
@app.route('/signup', methods=['GET','POST'])
def signup():
    # creating an onject of the signup class
    form=SignupForm()
    # For validation
    # also flash message is used to display the success messsage which is displayed only once
    if form.validate_on_submit():
        flash(f"Successfully Registered the {form.username.data}!")
        return redirect(url_for('home'))
    return render_template('signup.html',title='signup',form=form)

@app.route('/login',methods=['GET','POST'])
def login():
    form=LoginForm()
    name = form.username.data
    pw = form.password.data
    if form.validate_on_submit():
        if name == '12345' and pw == '11111':
            flash("Logged In Sucessfully!")
            return redirect(url_for('home'))
        else:
            flash('Incorrect username or password')
    return render_template('login.html',title='login',form=form)


 
if __name__ == '__main__':
    app.run(debug=True)