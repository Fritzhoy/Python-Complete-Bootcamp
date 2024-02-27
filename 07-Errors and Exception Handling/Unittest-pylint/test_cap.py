'''
General structure of a test
 - Create your classe to be called
 - Inherit from unittest.TestCase
 - Function to be called(usually number them like test1, test2)
 - Call whatever functions you want to test 

 this test will assert that the function cap will
   always return the capitilized string
'''
import unittest
import cap

class TestCap(unittest.TestCase):
    
    def test_one_word(self):
        text = 'python'
        result = cap.cap_text(text)
        self.assertEqual(result, 'Python')
        
    def test_multiple_words(self):
        text = 'monty python'
        result = cap.cap_text(text)
        self.assertEqual(result, 'Monty Python')

if __name__ == '__main__':
    unittest.main()
