#!/usr/bin/env python3
"""
inventory manager testing
"""
from models.engine.inventory_manager import Inventory_manager
from models import storage
from models.product import Product

im = Inventory_manager()


im.add_product("chair", 20, 500)
im.add_product("table", 10, 1000)
im.add_product("bed", 5, 2000)
x = im.read_all_products()
print(x)

storage.all(Product)
