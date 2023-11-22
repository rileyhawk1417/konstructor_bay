#!/usr/bin/env python3
"""
cart  testing
"""

from models.engine.cart_manager import Cart_manager
from models import storage

cm = Cart_manager()

#create_cart(<user_id>, <product_id>)
cm.create_Cart('1c24003b-64d6-485b-9a59-bafc81db081b', '2105c257-950c-49e8-9518-05537cb74755')