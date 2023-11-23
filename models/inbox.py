<<<<<<< HEAD
#!/usr/bin/env python3
from models.base_model import Base, BaseModel
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class Inbox(Base, BaseModel):
    __tablename__ = "inbox"
    message= Column(String(4096), nullable=True)
    user_id = Column(String(256), ForeignKey('user.id'), nullable=True)
    user = relationship("User", backref="inbox")
    
    supplier = relationship("Supplier", backref="inbox")
=======
#!/usr/bin/env python3
from models.base_model import Base, BaseModel
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class Inbox(Base, BaseModel):
    __tablename__ = 'inbox'
    user_id = Column(String(60), ForeignKey('user.id'), nullable=False)    
    user = relationship('User', backref='inbox')

class Message(Base, BaseModel):
    __tablename__ = 'message'
    sender_id = Column(String(60), ForeignKey('user.id'), nullable=False)
    receiver_id = Column(String(60), ForeignKey('user.id'), nullable=False)
    content = Column(String(140), nullable=False)
    sender = relationship('User', foreign_keys=[sender_id])
    receiver = relationship('User', foreign_keys=[receiver_id])
    inbox_id = Column(String(60), ForeignKey('inbox.id'), nullable=False)
    inbox = relationship('Inbox', backref='message')
>>>>>>> 31a363f692dcd2740c885be3f64357cbfc102f2b
