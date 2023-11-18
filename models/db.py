from sqlalchemy import create_engine, Column, String, Float, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///ecommerce.db')
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

class Product(Base):
    __tablename__ = 'products'
    product_id = Column(String, primary_key=True)
    price = Column(Float)
    desc = Column(String)
    quantity = Column(Float)
    supplier_id = Column(String, ForeignKey('suppliers.supplier_id'))
    supplier = relationship('Supplier', back_populates='products')

class Supplier(Base):
    __tablename__ = 'suppliers'
    supplier_id = Column(String, primary_key=True)
    name = Column(String)
    contact_info = Column(String)
    products = relationship('Product', back_populates='supplier')

class User(Base):
    __tablename__ = 'users'
    user_id = Column(String, primary_key=True)
    username = Column(String)
    email = Column(String)
    password = Column(String)
    user_type = Column(String)
