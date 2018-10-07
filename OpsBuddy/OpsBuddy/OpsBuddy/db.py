from datetime import datetime
from OpsBuddy import db, login_manager
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# https://docs.sqlalchemy.org/en/latest/orm/tutorial.html

class logonstats(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    acname = db.Column(db.String(45), nullable=False)
    servername = db.Column(db.String(100), nullable=False)
    datetime = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    serverip = db.Column(db.String(45), nullable=False)
    clientip = db.Column(db.String(45), nullable=False)

    def __init__(self, id, acname, servername,datetime,serverip,clientip):
        self.id=id
        self.acname=acname
        self.servername=servername
        self.datetime=datetime
        self.serverip=serverip
        self.clientip=clientip



class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
