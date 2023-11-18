from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.supplier import Supplier
from models.base_model import BaseModel  # Import all other models similarly

# Create an engine to connect to your MySQL database
engine = create_engine('mysql+pymysql://root@32f748541f8d:Clear@127.0.0.1:3306/mysql')

# Create all tables defined in your models
BaseModel.metadata.create_all(engine)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

# Closing the session after operations
session.close()
