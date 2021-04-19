import unittest
import random
from unittest.mock import MagicMock
from src.LogIn import LogIn

import self as self

from src.ReadCSVFile import ReadCSVFile


class testReadCSV(unittest.TestCase):
    readFile = ReadCSVFile()

    def test_CSV(self):
        self.assertEqual(['07711223344', 'Derek', 'Somerville', '1234'], self.readFile)

    def test_fakeData(self):
        testPhone = ['07712321234356', '07789462734', '07654756475']
        testPasswords = ['9999', '6666', '4444']
        items = [
            {
                "phone": random.choice(testPhone),
                "password": random.choice(testPasswords)
            }
            for _ in range(3)
        ]
        self.assertEqual(items, self.readFile)
        return self

    def test_readFileData(self):
        self.readFile.getFileData = MagicMock(return_value=['07711223344', 'Derek', 'Somerville', '1234'])
        self.assertEqual(self.readFile.getFileData("customer", ['07722334455', 'Matt', 'Barr', '4321']))

    def test_FakeList(self):
        logIn = LogIn()
        customers = Customers()
        main = Main()

        testList = ['07711122233', '077897654321', '07896789894', '07123421234']
        displayFakeList = LogIn()
        displayFakeList.getPassword = MagicMock(return_value=testList.pop())
        self.assertEqual('Enter phone number', displayFakeList.display())


if __name__ == '__main__':
    unittest.main()
