#!/usr/bin/env python3
"""
products model
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship

class Product(Base, BaseModel):
    __tablename__ = "products"
    product_name = Column(String(239), nullable=True)
    description = Column(String(350), nullable=True)
    quantity = Column(Integer, nullable=True)
    price = Column(Integer, nullable=True)
    #img_filename = Column(String(256), nullable=True)
    supplier_id = Column(String(256), ForeignKey('supplier.id'), nullable=True)
    location_id = Column(String(256), ForeignKey('location.id'), nullable=True)
    supplier = relationship("Supplier", backref="product")

    def __repr__(self):
        return f"<Product {self.product_name}, {self.description}, {self.quantity}, {self.price}>"

    @classmethod
    def serialize(cls, product_instance):
        return {
            "id": product_instance.id,
            "product_name": product_instance.product_name,
            "description": product_instance.description,
            "quantity": product_instance.quantity,
            "price": product_instance.price,
            "supplier_id": product_instance.supplier_id,
            "supplier_name": product_instance.supplier.business_name if product_instance.supplier else None,
            "location_id": product_instance.location_id
        }
