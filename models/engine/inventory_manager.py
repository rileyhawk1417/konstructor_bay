<<<<<<< HEAD
#!/usr/bin/env python3
from models.product import Product
from models.engine.db_engine import Db_storage

class Inventory_manager:
    def __init__(self):
        self.db = Db_storage()

    def add_product(self, name, quantity, price, location):
        new_product = Product(name=name, quantity=quantity, price=price, location=location)
        self.db.new()
        self.db.save()

    def update_product_quatity(self, product_id, new_quantity):
        product = self.db.get(Product, product_id)
        if product:
            products.quantity = new_product
            self.db.new()
            self.db.save()
        else:
            print("The product is not available")

    def delete_product(self, product_id):
        self.db.delete(product_id)
        self.db.new()
        self.db.save()

    def read_all_products(self):
        return self.db.all(Product)
=======
#!/usr/bin/env python3
from models.product import Product
from models.location import Location
from models.engine.db_engine import Db_storage
from uuid import uuid4
import uuid

class Inventory_manager:
    def __init__(self):
        self.db = Db_storage()

    def add_product(self, name, quantity, price):
        product_id = str(uuid.uuid4())
        new_product = Product(id=product_id, product_name=name, quantity=quantity, price=price)
        self.db.new(new_product)
        self.db.save()

    def update_product_quantity(self, product_id, new_quantity):
        product = self.db.get(Product, product_id)
        if product:
            products.quantity = new_product
            self.db.new()
            self.db.save()
        else:
            print("The product is not available")

    def delete_product(self, product_id):
        product = self.db.new_get(Product, product_id)
        if product:
            self.db.delete(product)
            self.db.save()
        else:
            print("The product is not available")

    def read_all_products(self):
        return self.db.new_get(Product)
>>>>>>> 31a363f692dcd2740c885be3f64357cbfc102f2b
