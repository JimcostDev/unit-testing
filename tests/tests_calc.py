import unittest

from src.calculator import sum, subtract

# usando unittest
class CalculatorTests(unittest.TestCase):

    def test_sum(self):
        assert sum(2, 3) == 5

    def test_subtract(self):
        assert subtract(10, 5) == 5
        
# usando pytest
def test_suma(): 
    assert sum(4, 3) == 7

def test_subtract():
    assert subtract(4, 3) == 1