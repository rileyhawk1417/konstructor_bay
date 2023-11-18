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

username = 'ks_developers'
password = ''
host = 'localhost'
database = 'ks_dev_db'




new_user = User(firstName='Root', sec_name='shadow', email='rootcode947@gmail.com',
        username='Mr root', phone_num='0700000000', password='rootcode', location_id='254'    
        )
new_location = Location(country='Nairobi')
engine = create_engine(f"mysql+mysqldb://{username}:{password}@{host}/{database}")
Session = sessionmaker(bind=engine)
session = Session()

my_db.new(new_user)
my_db.save()

#querying all users
all_users = session.query(User).all()
for user in all_users:
    print(user.email)

my_db.close()
