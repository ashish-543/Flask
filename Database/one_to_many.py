from enum import unique
from flask import Flask
from flask_sqlalchemy import SQLAlchemy # type: ignore


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///ipl.db"
# URL of DB to establish connection. Since sqlite is serverless, there is no need for username and password of the database server.
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False  # to hide warnings by SQL Alchemy

# Creating a database object
db = SQLAlchemy(app)


class Team(db.Model):
    __tablename__ = 'teams'
    # The tablename is not mandatory. If it is not mentioned , the lowercased name of the class will be the tablename.
    id = db.Column(db.Integer, primary_key=True)
    team = db.Column(db.String(50), nullable=False, unique=True)
    state = db.Column(db.String(50), nullable=False)
    members = db.relationship("Player", backref='team')
    # Here, we have established relationship between Team and Player. The backref is used to establish the bi-directional relationship
    # between the two tables. Here the backref = 'team' establishes a imaginary column with name team so we don't have to write the team
    # id for each player in the Player table


    def __repr__(self):
        return f"Team('{self.team}', '{self.state}')"


class Player(db.Model):
    __tablename__ = 'players'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    nationality = db.Column(db.String(50), nullable=False)
    team_id = db.Column(db.Integer, db.ForeignKey("teams.id"))
    # For the foreign key, we write db.Foreignkey and inside it, we write the name of the table along with the primary key of that
    # table that is referenced by another table. Here, the id of the teams table is referenced by the foreign key of the players table


    def __repr__(self):
        return f"Player('{self.name}', '{self.nationality}')"




if __name__ == "__main__":
    app.run(debug=True)