from flask import Flask
from flask_sqlalchemy import SQLAlchemy # type: ignore


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///employees_db.db"
# URL of DB to establish connection. Since sqlite is serverless, there is no need for username and password of the database server.
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False  # to hide warnings by SQL Alchemy

# Creating a database object
db = SQLAlchemy(app)




# database models
class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)

    def __repr__(self):
        return f"Employee('{self.name}', {self.age}, '{self.email}')"
    # Here the repr function is used to view the values of the databases just by typing the object of the class.
    # Without this function, on typing the name of the object, we get only the memory location of the created object
    


# run the flask app
if __name__ == "__main__":
    app.run(debug=True)