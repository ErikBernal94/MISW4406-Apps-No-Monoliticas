from contrato.config.db import db
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, ForeignKey, Integer, Table

import uuid

Base = db.declarative_base()

class MovimientoInmobiliario(db.Model):
    __tablename__ = "movimientos_inmobiliarios"
    id = db.Column(db.String, primary_key=True)