import sqlalchemy 
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker 
from sqlalchemy.orm import scoped_session
from models.base_model import Base
from models.user import User
from models.orders import Order
from models.location import Location
from models.cart import Cart
from models.product import Product
from models import storage
from models.engine.db_engine import Db_storage
import models

my_db = Db_storage()
my_db.reload()

new_user = User(name='Root', email='rootcode947@gmail.com')
my_db.new(new_user)
my_db.save()

#querying all users
all_users = my_db.all(User)
for user in all_users:
    print(user.id, user.name, user.email)

my_db.close()
