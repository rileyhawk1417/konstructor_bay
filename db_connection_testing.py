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
from models.engine.inventory_manager import Inventory_manager
from models.engine.user_manager import User_manager

um = User_manager

um.create_user('moses', 'gitonga', 'root', 'infosec947@gmail.com', 'my_password')
print(um.read_users())


