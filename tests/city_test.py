
import unittest
from models.city import City

class TestCity(unittest.TestCase):

    def setUp(self): 
        self.city = City("Oslo", "Sweden")

    def test_city_has_name(self):
        self.assertEqual("Oslo",self.city.name)
    
    def test_city_belongs_to_country(self):
        self.assertEqual("Sweden", self.city.country)

if __name__ == '__main__':
    unittest.main()