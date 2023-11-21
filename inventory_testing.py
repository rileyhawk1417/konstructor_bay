#!/usr/bin/env python3
"""
inventory manager testing
"""
from models.engine.inventory_manager import Inventory_manager
from models import storage

im = Inventory_manager()
im.add_product("chair", 20, 500)
im.add_product("table", 10, 1000)

storage.all(Product)