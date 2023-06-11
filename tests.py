import unittest
from parser.step_two import  get_alldataSheet


class TestStepTwo(unittest.TestCase):

    def test_get_alldataSheet(self):
        self.assertEqual(get_alldataSheet("AVS1ACP08"), "AVS1ACP08")
        self.assertEqual(get_alldataSheet("	6AM-6PA"), "")
        self.assertEqual(get_alldataSheet("	6LR61XWA/1SB"), "")
        self.assertEqual(get_alldataSheet("	AD1990Acpz "), "AD1990ACPZ")


