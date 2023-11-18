from sqlalchemy import Column, String, Float, ForeignKey
from models.base_model import BaseModel

class Product(BaseModel):
    __tablename__ = 'products'

    product_id = Column(String(50), primary_key=True)
    price = Column(Float)
    desc = Column(String)
    supplier_id = Column(String(50))
    quantity = Column(Float)
    supplier_id_1 = Column(String(50), ForeignKey('supplier.supplier_id'))  # Assuming the foreign key references the 'supplier' table
