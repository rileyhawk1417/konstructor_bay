from sqlalchemy import Column, String, ForeignKey
from models.base_model import BaseModel

class Supplier(BaseModel):
    __tablename__ = 'suppliers'

    supplier_id = Column(String(50), primary_key=True)
    name = Column(String)
    contact_info = Column(String)
    product_id = Column(String(50), ForeignKey('products.product_id'))  # Assuming the product_id references the 'products' table
