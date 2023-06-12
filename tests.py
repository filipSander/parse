import unittest
from parser.productlinq import Productlinq
from parser.step_one import getCatalog
from parser.step_two import  get_alldataSheet
from parser.driver import Driver
from product import Product


class testStepOne(unittest.TestCase):

    def test_checkProduct(self):
        driver = Driver().getDriver()
        catalog = Productlinq(
            "Интегральные микросхемы",
            "AC/DC конвертеры",
            "https://www.chipfind.ru/catalog/testeq/accessories/"
        )
        self.assertEqual(len(getCatalog(driver=driver,catalog=catalog)),302)
        self.assertEqual(302, Product.count)


# class TestStepTwo(unittest.TestCase):

#     def test_get_alldataSheet(self):
#         driver = Driver().getDriver()
#         self.assertEqual(get_alldataSheet("AVS1ACP08", driver), "AVS1ACP08")
#         self.assertEqual(get_alldataSheet("	6AM-6PA", driver), "")
#         self.assertEqual(get_alldataSheet("	6LR61XWA/1SB", driver), "")
#         self.assertEqual(get_alldataSheet("	AD1990Acpz ", driver), "AD1990ACPZ")


