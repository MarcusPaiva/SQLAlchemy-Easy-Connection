# SQLAlchemy-Easy-Connection
Simple way to connect Database using SQLAlchemy.
## Project motivations
This repository makes use of trivial options in the creation of the database engine.
My intention is to facilitate the connection to the database using SQLAlchemy, distributing this package that I created and use many years ago, I intend over time to add standard options for each type of database, making only you worry about connecting to the database.


Suggestions, improvements and contact, I am available at email: 'marcus.paiva.ti@gmail.com'.

## How to install?
You can install using the following command:
```
pip install SQLAlchemy-Easy-Connection
```

## Simple usage example
```
from SQLAlchemyEasyConnection.EasyConnections import EasyConnection  # Using this package we use to connect into database
from SQLAlchemyEasyConnection import DatabaseTypes  # This file is easy way to get you SQL server name
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

db_connection = EasyConnection()  # Instance
db_connection.connect_to_database(type_database=DatabaseTypes.SQLITE,
                                  database="C:\\temp\\sqltest.db")  # Create Connection to database

# Using declarative base
Base = declarative_base()


# This class is a simple example to create using SQLAlchemy
class User(Base):
    __tablename__ = "user"

    id_user = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)


Base.metadata.create_all(db_connection.get_engine)  # Create table

# Creating a new user using ORM
user = User()
user.name = "foo"
user.email = "foo@bar.com"

# Add new User
db_connection.insert_item(user)
db_connection.session_commit()

print(user.id_user)  # see? This show new user ID after create a new user in table 'user'
```