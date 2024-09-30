"""
Exercise
Samuel Martinez
"""

import unittest
from bankaccount import BankAccount

class TestBankAccount(unittest.TestCase):

    def setUp(self):
        self.account = BankAccount("12345", "Samuel Martinez")

    def test_initial_balance(self):
        self.assertEqual(self.account.get_balance(), 0.0)

    def test_deposit(self):
        self.account.deposit(100)
        self.assertEqual(self.account.get_balance(), 100.0)

    def test_withdraw(self):
        self.account.deposit(100)
        self.account.withdraw(50)
        self.assertEqual(self.account.get_balance(), 50.0)

    def test_withdraw_insufficient_funds(self):
        self.account.deposit(100)
        self.account.withdraw(150)
        self.assertEqual(self.account.get_balance(), 100.0)

    def test_sequence_of_transactions(self):
        self.account.deposit(200)
        self.account.withdraw(50)
        self.account.deposit(100)
        self.account.withdraw(75)
        self.assertEqual(self.account.get_balance(), 175.0)

if __name__ == '__main__':
    unittest.main()
