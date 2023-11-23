<<<<<<< HEAD
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


=======
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
from models import storage

db = storage
some_id = '6d290236-80a3-41e6-8cc2-e0ee975c4716'
res = db.new_get(User, some_id)
print(res.__dir__)



>>>>>>> 31a363f692dcd2740c885be3f64357cbfc102f2b
