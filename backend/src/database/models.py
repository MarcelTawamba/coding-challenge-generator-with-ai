# ORM: object-relational mapping
from sqlalchemy import Column, Integer, String, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

# Database connection setup
engine = create_engine('sqlite:///database.db', echo=True)

# Declarative base class for ORM models
Base = declarative_base()

# User model to store user information
class Challenge(Base):
    __tablename__ = 'challenges'

    id = Column(Integer, primary_key=True)
    difficulty = Column(String, nullable=False)
    date_created = Column(DateTime, default=datetime.now)
    created_by = Column(String, nullable=False)
    title = Column(String, nullable=False)
    options = Column(String, nullable=False) # "option 1, option 2, option 3" comma-separated string
    correct_answer_id = Column(Integer, nullable=False)
    explanation = Column(String, nullable=False)

class ChallengeQuota(Base):
    __tablename__ = 'challenge_quotas'

    id = Column(Integer, primary_key=True)
    user_id = Column(String, nullable=False, unique=True)
    quota_remaining = Column(Integer, default=50, nullable=False)  # Each user starts with a quota of 50 challenges
    last_reset_date = Column(DateTime, default=datetime.now)

# Create the database tables
Base.metadata.create_all(engine)

# Create a session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    """
    Dependency to get a database session.
    Yields a session and ensures it is closed after use.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
