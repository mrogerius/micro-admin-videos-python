from dataclasses import is_dataclass
from datetime import datetime
from unicodedata import category
import unittest
from category.domain.entities import Category

class TestCategoryUnit(unittest.TestCase):
    
    #data = {'name':'Movie', 'description':'Ultimo', 'is_active':'True', 'created_at':'datetime.now()'}
    #category = Category(**data)
    
    def test_is_a_dataclass(self):
        self.assertTrue(is_dataclass(Category))
    
    def test_constructor(self):        
        category = Category(name='Movie')
        self.assertEqual(category.name, 'Movie')
        self.assertEqual(category.description, None)
        self.assertEqual(category.is_active, True)
        self.assertIsInstance(category.created_at, datetime)
        
        created_at = datetime.now()
        category = Category(
            name='Movie', 
            description='Ultimo', 
            is_active=False,
            created_at=created_at
        )
        
        self.assertEqual(category.name, 'Movie')
        self.assertEqual(category.description, 'Ultimo')
        self.assertEqual(category.is_active, False)
        self.assertEqual(category.created_at, created_at)
    
    def teste_if_created_ad_is_generate_in_constructor(self):
        category1 = Category(name='Movie 1')
        category2 = Category(name='Movie 2')
        self.assertNotEqual(
            category1.created_at.timestamp(),
            category2.created_at.timestamp()
        )

        #self.assertEqual(category.name, 'Movie')
        #self.assertEqual(category.description, 'Ultmo')
        #self.assertEqual(category.is_active, True)
        #self.assertIsInstance(category.created_at, datetime)

        