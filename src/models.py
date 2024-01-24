import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    person = relationship("Person")


class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    climate = Column(String(250))
    terrain = Column(String(250))
    population = Column(Integer)
    favorites = relationship("Favorite")

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    height = Column(Integer)
    hair_color = Column(String(250))
    eye_color = Column(String(250))
    gender = Column(String(250))
    favorites = relationship("Favorite")

class Starship(Base):
    __tablename__ = 'starship'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    model = Column(String(250))
    manufacturer = Column(String(250))
    crew = Column(Integer)
    passengers = Column(Integer)
    favorites = relationship("Favorite")
    # Add any additional fields as necessary

class Favorite(Base):
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    planet_id = Column(Integer, ForeignKey('planet.id'))
    character_id = Column(Integer, ForeignKey('character.id'))
    starship_id = Column(Integer, ForeignKey('starship.id'))

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
