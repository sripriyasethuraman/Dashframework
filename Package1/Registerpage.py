import unittest

class Registerpage(unittest.TestCase):

    def test_register_as_surgeon(self):
        print ("Surgeon register")
        self.assertTrue(True)

    def test_register_as_hcp(self):
        print("HCP register")
        self.assertTrue(True)

    def test_register_as_aa(self):
        print("AA register")
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()