# To run te unittest , go to the test folder and run the command python -m unittest
import unittest

class FirstClass():
    first = 5

class SecondClass():
    second = 5

class TestStringMethods(unittest.TestCase):
    def setUp(self):
        self.value = 'some text'
        self.otherValue = 'some other value'
       
    def test_upper(self):
        self.assertEqual(self.value.upper(), 'SOME TEXT')

    def test_isupper(self):
        self.assertTrue('ANY TEXT'.isupper())
        self.assertFalse('any Text'.isupper())

    def test_split(self):
        self.assertEqual(self.value.split(), ['some', 'text'])
        with self.assertRaises(TypeError):
            self.value.split(2)

    def test_is(self):
        message = None
        self.assertIs(self.value, 'some text')
        self.assertIsNot(self.value, self.otherValue)
        self.assertIsNone(message)

    def test_in(self):
        myList = [2,4,6,8,10]
        self.assertIn(2,myList)
        self.assertNotIn(3,myList)
    
    def test_instance(self):
        a = FirstClass()
        self.assertIsInstance(a,FirstClass, "not the instance of testClass")
        self.assertNotIsInstance(a,SecondClass,"not the instance of anotherTestClass")


if __name__ == '__main__':
    unittest.main()
