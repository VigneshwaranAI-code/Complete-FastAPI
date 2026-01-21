# Import the session factory from Database.py
from Database import SessionLocal

# Dependency function for FastAPI to provide database sessions
# This is a generator function that yields a DB session and ensures cleanup
def get_db():
    # Create a new database session
    db = SessionLocal()
    try:
        # Yield the session to the requesting function/route
        yield db
    finally:
        # Always close the session after use to free resources
        db.close()

  