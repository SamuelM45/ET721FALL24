import unittest

def addtwonumbers(a,b):
    return a+b

# create a unit test to check if function 'addtwonumbers' is working properly
class TestAddFunction(unittest.TestCase):
    def test_addtwonumbers(self):
        self.assertEqual(addtwonumbers(3,5),15)

if __name__ == '__main__':
    unittest.main()
    