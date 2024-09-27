"""
Example 3: Verify if the email, full name, and salary fields are correctly formatted
Samuel Martinez
"""

import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    

    #set up templates
    def setUp(self):
        #create an instance of the class Employee
        emp1 = Employee("Peter", "Pan", 50000) 


    def test_email(self):
        # Create an instance of the Employee class
        emp1 = Employee("Peter", "Pan", 50000)
        self.assertEqual(emp1.emailemployee, "Peter.Pan@email.com")

    def test_fullname(self):
        # Create an instance of the Employee class
        emp1 = Employee("Peter", "Pan", 50000)
        self.assertEqual(emp1.emailemployee, "Peter.Pan@email.com")

    def test_apply_raise(self):
        self.emp1.apply_raise()

        self.assertEqual(self.emp1.salary, 52500)

        

if __name__ == "__main__":
    unittest.main()

