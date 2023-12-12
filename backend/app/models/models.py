from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, Integer, String, TIMESTAMP
from sqlalchemy.orm import relationship

Base = declarative_base()


class Role(Base):
    __tablename__ = 'Role'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False, unique=True)
    user = relationship('User', cascade='delete')


class User(Base):
    __tablename__ = 'User'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    role_id = Column(ForeignKey(Role.id))
    doctor = relationship('Doctor', cascade='delete')
    parent = relationship('Parent', cascade='delete')


class Specialization(Base):
    __tablename__ = 'Specialization'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False, unique=True)
    doctor = relationship('Doctor', cascade='delete')


class Doctor(Base):
    __tablename__ = 'Doctor'
    id = Column(Integer, primary_key=True, autoincrement=True)
    FML = Column(String, nullable=False)
    img = Column(String, default='placeholder.png')
    experience = Column(Integer, default=0)
    specialization_id = Column(ForeignKey(Specialization.id), nullable=False)
    user_id = Column(ForeignKey(User.id), nullable=False, unique=True)


class Parent(Base):
    __tablename__ = 'Parent'
    id = Column(Integer, primary_key=True, autoincrement=True)
    FML = Column(String, nullable=False)
    contact = Column(String, nullable=False)
    user_id = Column(ForeignKey(User.id), nullable=False, unique=True)
    child = relationship('Child', cascade='delete')


class Medcard(Base):
    __tablename__ = 'Medcard'
    id = Column(Integer, primary_key=True, autoincrement=True)
    unique_key = Column(String, nullable=False, unique=True)
    child = relationship('Child', cascade='delete')
    entries = relationship('MedcardEntries', cascade='delete')
    diagnosis = relationship('Diagnosis', cascade='delete')

class MedcardEntries(Base):
    __tablename__ = 'MedcardEntries'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    medcard_id = Column(ForeignKey(Medcard.id))


class Child(Base):
    __tablename__ = 'Child'
    id = Column(Integer, primary_key=True, autoincrement=True)
    FML = Column(String, nullable=False)
    img = Column(String, default='placeholder.png') 
    parent_id = Column(ForeignKey(Parent.id), nullable=False)
    medcard_id = Column(ForeignKey(Medcard.id), unique=True)


class Diagnosis(Base):
    __tablename__ = 'Diagnosis'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False, unique=True)
    medcard_id = Column(ForeignKey(Medcard.id), nullable=False)
    procedures = relationship('Procedures', cascade='delete')


class Procedures(Base):
    __tablename__ = 'Procedures'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    diagnosis_id = Column(ForeignKey(Diagnosis.id), nullable=False)

