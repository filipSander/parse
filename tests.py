import unittest
from parser.step_two import  get_alldataSheet
from parser.driver import Driver



class TestStepTwo(unittest.TestCase):

    def test_get_alldataSheet(self):
        driver = Driver().getDriver()
        self.assertEqual(get_alldataSheet("AVS1ACP08", driver), "AVS1ACP08")
        self.assertEqual(get_alldataSheet("	6AM-6PA", driver), "")
        self.assertEqual(get_alldataSheet("	6LR61XWA/1SB", driver), "")
        self.assertEqual(get_alldataSheet("	AD1990Acpz ", driver), "AD1990ACPZ")




