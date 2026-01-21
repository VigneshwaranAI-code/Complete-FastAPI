# Import SQLAlchemy components for defining database columns and types
from sqlalchemy import Column, Integer, String
# Import the base class from Database.py for declarative models
from Database import Base

# Define the Books model (database table)
class Books(Base):
    # Specify the database table name
    __tablename__ = "books"

    # Primary key column (auto-incrementing integer)
    id = Column(Integer, primary_key=True, index=True)
    # Book title (string/text field)
    title = Column(String)
    # Book author (string/text field)
    author = Column(String)
    # Book description (string/text field)
    description = Column(String)
    # Book rating (integer field, 1-5 or similar)
    rating = Column(Integer)
    
 