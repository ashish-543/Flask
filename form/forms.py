from flask_wtf import FlaskForm
from wtforms import(
    StringField,
    SelectField,
    DateField,
    PasswordField,
    SubmitField,
    BooleanField
)

from wtforms.validators import (
    DataRequired,
    Length,
    Email,
    Optional,
    EqualTo,
)

# Here the signup class inherits from the flaskform
class SignupForm(FlaskForm):
    username=StringField(
        "Username",
        validators=[DataRequired(), Length(5,20)]
        #Here validators are used to ckeck wether the given field is empty or not and it is also used to check the length of the input
         )
    email=StringField(
        "Email",
        validators=[DataRequired(), Email()]
    )
    gender=SelectField(
        "Gender",
        choices=['Male','Female','Others'],
        validators=[Optional()]
    )
    DOB=DateField(
        "Date Of Birth",
        validators=[Optional()]
    )
    password=PasswordField(
        "Password",
        validators=[DataRequired(), Length(5,15)]
    )
    confirm_password=PasswordField(
        "Confirm Password",
        validators=[DataRequired(),Length(5,15), EqualTo('password')]
        # Here equalto is used to match the values of password and confirm_password
    )
    submit=SubmitField("Sign Up")



class LoginForm(FlaskForm):
    username=StringField(
        "Username",
        validators=[DataRequired(), Length(5,20)]
         )
    password=PasswordField(
        "Password",
        validators=[DataRequired(), Length(5,15)]
    )
    remember_me=BooleanField('Remember Me')
    submit=SubmitField('Login')


    
