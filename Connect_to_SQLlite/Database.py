# Import necessary modules from SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Define the database URL for SQLite (creates 'books.db' in current directory)
SQLALCHEMY_DATABASE_URL = "sqlite:///./books.db"

# Create the SQLAlchemy engine with the database URL
# connect_args is specific to SQLite to allow connections from multiple threads
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Create a sessionmaker factory for database sessions
# autocommit=False: changes are not auto-committed
# autoflush=False: changes are not auto-flushed to DB
# bind=engine: binds the sessions to our engine
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create the base class for declarative models
# All SQLAlchemy model classes will inherit from this Base
Base = declarative_base()
