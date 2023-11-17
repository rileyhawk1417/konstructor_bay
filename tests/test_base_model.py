#!usr/bin/env python3
"""Unittest for BaseModel class"""
import unittest
from models.base_model import BaseModel
from datetime import datetime
import os
import pep8

class TestBaseModel(unittest.TestCase):
    def setUp(self):
        """Setup for testing"""
        self.b1 = BaseModel()
        self.b2 = BaseModel()
        self.b3 = BaseModel()


    def tearDown(self):
        """Teardown"""
        pass
    

    def test_docstring(self):
        """test docstring"""
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)
        self.assertIsNotNone(BaseModel.delete.__doc__)
        
    def test_init(self):
        """test init"""
        self.assertTrue(isinstance(self.b1, BaseModel))
        self.assertTrue(isinstance(self.b2, BaseModel))
        self.assertTrue(isinstance(self.b3, BaseModel))
        self.assertTrue(hasattr(self.b1, "id"))
        self.assertTrue(hasattr(self.b2, "id"))
        self.assertTrue(hasattr(self.b3, "id"))
        self.assertTrue(hasattr(self.b1, "created_at"))
        self.assertTrue(hasattr(self.b2, "created_at"))
        self.assertTrue(hasattr(self.b3, "created_at"))
        self.assertTrue(hasattr(self.b1, "updated_at"))
        self.assertTrue(hasattr(self.b2, "updated_at"))
        self.assertTrue(hasattr(self.b3, "updated_at"))
        self.assertTrue(isinstance(self.b1.id, str))
        self.assertTrue(isinstance(self.b2.id, str))
        self.assertTrue(isinstance(self.b3.id, str))
        self.assertTrue(isinstance(self.b1.created_at, datetime))
        self.assertTrue(isinstance(self.b2.created_at, datetime))
        self.assertTrue(isinstance(self.b3.created_at, datetime))
        self.assertTrue(isinstance(self.b1.updated_at, datetime))
        self.assertTrue(isinstance(self.b2.updated_at, datetime))
        self.assertTrue(isinstance(self.b3.updated_at, datetime))
        self.assertNotEqual(self.b1.id, self.b2.id)
        self.assertNotEqual(self.b1.id, self.b3.id)
        self.assertNotEqual(self.b2.id, self.b3.id)
        self.assertNotEqual(self.b1.created_at, self.b2.created_at)
        self.assertNotEqual(self.b1.created_at, self.b3.created_at)
        self.assertNotEqual(self.b2.created_at, self.b3.created_at)
        self.assertTrue(isinstance(self.b1.__dict__, dict))
        self.assertTrue(isinstance(self.b2.__dict__, dict))
        self.assertTrue(isinstance(self.b3.__dict__, dict))
        self.assertTrue(isinstance(self.b1.to_dict(), dict))
        self.assertTrue(isinstance(self.b2.to_dict(), dict))
        self.assertTrue(isinstance(self.b3.to_dict(), dict))
        self.assertTrue(isinstance(self.b1.to_dict()['id'], str))
        self.assertTrue(isinstance(self.b2.to_dict()['id'], str))
        self.assertTrue(isinstance(self.b3.to_dict()['id'], str))
        self.assertTrue(isinstance(self.b1.to_dict()['created_at'], str))
        self.assertTrue(isinstance(self.b2.to_dict()['created_at'], str))
        self.assertTrue(isinstance(self.b3.to_dict()['created_at'], str))
        self.assertTrue(isinstance(self.b1.to_dict()['updated_at'], str))
        self.assertTrue(isinstance(self.b2.to_dict()['updated_at'], str))
        self.assertTrue(isinstance(self.b3.to_dict()['updated_at'], str))


    def test_id(self):
        """test id"""
        self.assertTrue(isinstance(self.b1.id, str))
        self.assertNotEqual(self.b1.id, self.b2.id)
        self.assertNotEqual(self.b1.id, self.b3.id)


    def test_created_at(self):
        """test created_at"""
        self.assertTrue(isinstance(self.b1.created_at, datetime))
        self.assertTrue(isinstance(self.b2.created_at, datetime))
        self.assertTrue(isinstance(self.b3.created_at, datetime))


    def test_updated_at(self):
        """test updated_at"""
        self.assertTrue(isinstance(self.b1.updated_at, datetime))
        self.assertTrue(isinstance(self.b2.updated_at, datetime))
        self.assertTrue(isinstance(self.b3.updated_at, datetime))
    
    def test_save(self):
        """test save"""
        self.b1.save()
        self.assertNotEqual(self.b1.created_at, self.b1.updated_at)
        self.b2.save()
        self.assertNotEqual(self.b2.created_at, self.b2.updated_at)
        self.b3.save()
        self.assertNotEqual(self.b3.created_at, self.b3.updated_at)

    

    
