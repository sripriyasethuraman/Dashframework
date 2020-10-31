import unittest


class Homepage(unittest.TestCase):

   def test__home_page_surgeon(self):
    print ("Home page of surgeon")
    self.assertTrue(True)

   def test__home_page_hcp(self):
    print ("Home pge of hcp")
    self.assertTrue(True)

   def test__home_page_aa(self):
    print ("Home page of aa")
    self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()
