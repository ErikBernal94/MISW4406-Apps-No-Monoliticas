from propiedad.config.db import db
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, ForeignKey, Integer, Table

import uuid

Base = db.declarative_base()

class Propiedad(db.Model):
    __tablename__ = "propiedads"
    id = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(255), nullable=True)
    tipo = db.Column(db.String(255), nullable=True)