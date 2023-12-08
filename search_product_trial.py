#!/usr/bin/env python3
"""
search for debugging search function
"""
from models.engine.search_manager import Search_manager

sm = Search_manager
res = sm.search_product_name("Cement")
print(res)