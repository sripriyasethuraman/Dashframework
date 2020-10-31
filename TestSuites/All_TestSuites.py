import unittest
from Package1.Loginpage import LoginTest
from Package1.Registerpage import Registerpage

from Package2.Accountsettingspage import Accountsettingspage
from Package2.Homepage import Homepage

tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
tc2 = unittest.TestLoader().loadTestsFromTestCase(Registerpage)
tc3 = unittest.TestLoader().loadTestsFromTestCase(Accountsettingspage)
tc4 = unittest.TestLoader().loadTestsFromTestCase(Homepage)

# creating test suites

sanityTestSuite = unittest.TestSuite([tc1, tc2])
functionTestSuite = unittest.TestSuite([tc3, tc4])
masterTestSuite = unittest.TestSuite([sanityTestSuite, functionTestSuite])

# unittest.TextTestRunner().run(sanityTestSuite)
# unittest.TextTestRunner().run(functionTestSuite)
unittest.TextTestRunner(verbosity=2).run(masterTestSuite)

if __name__ == "__main__":
    unittest.main()
