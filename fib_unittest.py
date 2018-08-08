import unittest

import fibonacci

class fibTest(unittest.TestCase):
    
    def testBasic(self):
        self.assertEqual(fib(1), 1)
        self.assertEqual(fib(5), 5)



if __name__ == '__main__':
    unittest.main()
