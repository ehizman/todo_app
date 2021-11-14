from datetime import datetime
from enum import Enum

from todo import db


class Status(Enum):
    UNCOMPLETED = "Uncompleted"
    COMPLETED = "Completed"


class Todo(db.Model):
    __tablename__ = "todo"
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(), nullable=False)
    status = db.Column(db.Enum(Status), nullable=False, default=Status.UNCOMPLETED)
    date_added = db.Column(db.DateTime, nullable=False,
                           default=datetime.now())
