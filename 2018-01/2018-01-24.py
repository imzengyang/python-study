"""
unittest

"""
import unittest

class CnodeTest(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        print("setUpClass..")

    def setUp(self):
        print("this is setup...")

    def test_01register(self):
        print("test_01register")

    def test_02login(self):
        print('test_02login')

    def tearDown(self):
        print('this is teardwon....')

    @classmethod
    def tearDownClass(self):
        print('tearDownClass...')
    

if __name__ == '__main__':
    unittest.main(verbosity=2)