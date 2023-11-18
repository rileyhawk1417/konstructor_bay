import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from your_models_file import Product, Supplier, User  # Import your SQLAlchemy models

DATABASE_URI = 'sqlite:///test_ecommerce.db'  # Use a test database

@pytest.fixture(scope='module')
def engine():
    # Set up the engine and create tables
    test_engine = create_engine(DATABASE_URI)
    Product.metadata.create_all(test_engine)
    Supplier.metadata.create_all(test_engine)
    User.metadata.create_all(test_engine)
    return test_engine

@pytest.fixture(scope='function')
def session(engine):
    # Create a session for each test function
    Session = sessionmaker(bind=engine)
    test_session = Session()
    yield test_session
    test_session.rollback()

def test_product_creation(session):
    # Test creating a product
    new_product = Product(product_id='P001', price=100.0, desc='Product Description', quantity=50.0)
    session.add(new_product)
    session.commit()

    # Fetch the product and assert attributes
    fetched_product = session.query(Product).filter_by(product_id='P001').first()
    assert fetched_product is not None
    assert fetched_product.price == 100.0

def test_supplier_creation(session):
    # Test creating a supplier
    new_supplier = Supplier(supplier_id='S001', name='Supplier 1', contact_info='Contact Info')
    session.add(new_supplier)
    session.commit()

    # Fetch the supplier and assert attributes
    fetched_supplier = session.query(Supplier).filter_by(supplier_id='S001').first()
    assert fetched_supplier is not None
    assert fetched_supplier.name == 'Supplier 1'

def test_user_creation(session):
    # Test creating a user
    new_user = User(user_id='U001', username='user1', email='user1@example.com', password='pass123', user_type='customer')
    session.add(new_user)
    session.commit()

    # Fetch the user and assert attributes
    fetched_user = session.query(User).filter_by(user_id='U001').first()
    assert fetched_user is not None
    assert fetched_user.email == 'user1@example.com'

def test_relationships(session):
    # Test relationships between Product and Supplier
    new_supplier = Supplier(supplier_id='S002', name='Supplier 2', contact_info='Contact Info 2')
    new_product = Product(product_id='P002', price=200.0, desc='Product 2 Description', quantity=30.0)
    new_supplier.products.append(new_product)
    session.add(new_supplier)
    session.commit()

    # Fetch the supplier and assert products
    fetched_supplier = session.query(Supplier).filter_by(supplier_id='S002').first()
    assert fetched_supplier is not None
    assert len(fetched_supplier.products) == 1
    assert fetched_supplier.products[0].product_id == 'P002'

    # Test relationships between User and Product
    new_user = User(user_id='U002', username='user2', email='user2@example.com', password='pass456', user_type='admin')
    new_user_products = [Product(product_id=f'P00{i}', price=300.0, desc=f'Product {i} Description', quantity=20.0) for i in range(3)]
    new_user_products[0].supplier_id = 'S002'  # Assign supplier for the product
    new_user.products = new_user_products
    session.add(new_user)
    session.commit()

    # Fetch the user and assert products
    fetched_user = session.query(User).filter_by(user_id='U002').first()
    assert fetched_user is not None
    assert len(fetched_user.products) == 3
