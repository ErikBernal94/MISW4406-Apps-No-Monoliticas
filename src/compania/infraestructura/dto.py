from compania.config.db import db
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, ForeignKey, Integer, Table

import uuid

Base = db.declarative_base()

class Compania(db.Model):
    __tablename__ = "companias"
    id = db.Column(db.Integer, primary_key=True)
    correo_electronico = db.Column(db.String(255), nullable=True)
    direccion = db.Column(db.String(255), nullable=True)