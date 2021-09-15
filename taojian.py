import unittest

class MyTestCase(unittest.TestCase):
    a = unittest.defaultTestLoader.discover('./',pattern='*dy.py')
    b = unittest.TextTestRunner()
    b.run(a)
if __name__ == '__main__':
    unittest.main()