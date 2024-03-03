from contrato.config.db import db
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, ForeignKey, Integer, Table

import uuid

Base = db.declarative_base()

class Contrato(db.Model):
    __tablename__ = "contratos"
    id = db.Column(db.Integer, primary_key=True)
    estado = db.Column(db.String(255), nullable=True)
    tipo = db.Column(db.String(255), nullable=True)
