import unittest


class LoginTest(unittest.TestCase):

    def test_login_as_surgeon(self):
        print ("Surgeon login")
        self.assertTrue(True)

    def test_login_as_hcp(self):
        print("HCP login")
        self.assertTrue(True)

    def test_login_as_aa(self):
        print("AA login")
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()