from models import storage
from models.product import Product
from models.user import User
from models.location import Location
from models.cart import Cart
from models.orders import Order
from models.base_model import Base, BaseModel
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from models.engine.db_engine import Db_storage

# Creating instances of models
location_instance = Location(country='Kenya', county='Nairobi', zone='Kasarani')
user_instance = User(firstName='John', sec_name='Doe', email='john@example.com', username='johndoe', phone_num='+1234567890', password='password', location=location_instance)


# Create tables and insert data
db_handler = Db_storage()
db_handler.reload() #the reload method creetes all tables in the db
db_handler.insert_data(user_instance, location_instance)  