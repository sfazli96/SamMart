"""
Configuration Modules
    
Configuration settings for the application. Stores keys, uri, and other settings.
"""
import os

class Config:
    """
    This class stores configuration settings such as the secret key and database URI.

    Attributes:
        SECRET_KEY (str): The secret key used for various security purposes.
        SQLALCHEMY_TRACK_MODIFICATIONS (bool): Whether to track modifications in SQLAlchemy.
        SQLALCHEMY_DATABASE_URI (str): The URI of the database used by the application.
        SQLALCHEMY_ECHO (bool): Whether to log SQL statements generated by SQLAlchemy.
    """
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URL').replace('postgres://', 'postgresql://')
    SQLALCHEMY_ECHO = True
