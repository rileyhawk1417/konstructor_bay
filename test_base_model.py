#!/usr/bin/env python3
"""
test if the base model is returning output as exepected
"""
from models.base_model import BaseModel

obj1 = BaseModel()
obj2 = BaseModel()

print(obj1.id)
print(obj2.id)

obj1.name = "Root"
print(obj1.name)

obj1.number = 34
print(obj1.number)

print(obj1)

dict_test = obj1.to_dict()
print(f"\n\n{dict_test}")

