import unittest
from models.country import Country

class TestCountry(unittest.TestCase):

    def setUp(self): 
        self.country = Country("Japan", "Top 87", True)

    def test_country_has_name(self):
        self.assertEqual("Japan",self.country.name)
    
    def test_country_has_rating(self):
        self.assertEqual("Top 87", self.country.rating)
    
    def test_country_has_visited(self):
        self.assertEqual(True, self.country.visited)

if __name__ == '__main__':
    unittest.main()