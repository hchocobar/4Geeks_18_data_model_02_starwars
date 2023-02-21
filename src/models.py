import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Float, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er


Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False, unique=True)
    email = Column(String(100), nullable=False) 
    password = Column(String(15), nullable=False)
    # Relationship
    # planets_favourites = relationship('Favourites_planets')
    # characters_favourites = relationship('Favourites_characters')


class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    height = Column(Integer)
    gender = Column(Boolean(), nullable=False)
    eyes_color = Column(String(15), nullable=False)
    hair_color = Column(String(15), nullable=False)
    skin_color = Column(String(15))
    birth_year = Column(String(10))
    # Relationship
    # characters_favourites = relationship('Favourites_characters')


class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    mass = Column(Float)
    climate = Column(String(250))
    terrain = Column(String(250))
    gravity = Column(String(250))
    diameter = Column(Integer)
    rotation = Column(Integer)
    population = Column(Integer)
    translation = Column(Integer)
    # Relationship
    # planets_favourites = relationship('Favourites_planets')


class CharacterFavorites(Base):
    __tablename__ = 'characterfavorites'
    id = Column(Integer, primary_key=True)
    # FK and Relations
    user_id = Column(Integer, ForeignKey('user.id'))
    character_id = Column(Integer, ForeignKey('character.id'))
    # Relationship
    user = relationship(User)
    character = relationship(Character)


class PlanetFavorites(Base):
    __tablename__ = 'planetfavorites'
    id = Column(Integer, primary_key=True)
    # ForeingKey
    user_id = Column(Integer, ForeignKey('user.id'))
    planet_id = Column(Integer, ForeignKey('planet.id'))
    # Relationship
    user = relationship(User)
    planet = relationship(Planet)


# Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
