import os
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

# Database instance

db = SQLAlchemy()

class Message(db.Model):
    __tablename__ = 'messages'
    id = db.Column(db.Integer, primary_key=True)
    sender = db.Column(db.String(32))
    receiver = db.Column(db.String(32))
    text = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Message {self.id} from {self.sender}>"
