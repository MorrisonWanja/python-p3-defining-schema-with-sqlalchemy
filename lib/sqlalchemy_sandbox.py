#!/usr/bin/env python3
import sqlalchemy
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
engine = create_engine('sqlite:///students.db')
Session = sessionmaker(bind=engine)

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer(),primary_key=True)
    name = Column(String())
    pass
Base.metadata.create_all(engine)
if __name__ == '__main__':
    pass