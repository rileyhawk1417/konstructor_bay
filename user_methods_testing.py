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
um.login("johndoe", "mysecurepassword")

"""
um.create_user('moses', 'gitonga', 'root', 'infosec947@gmail.com', 'my_password')
print(um.read_users())
#user_id = storage.query_id(User)
#print(user_id)
#um.update_email('812da25b-7309-4a4c-b02b-e6f1ad28962d', 'rootcode947@gmail.com')


#all_users = um.read_users()
#print(all_users)
#all_users = um.read_users()
#um.delete_user('43620e5d-7d75-4544-bb40-8db00abf75b5')


all_users = um.read_users()
print(all_users)
"""
