from typing import KeysView
import unittest
from parser.productlinq import Productlinq
from parser.func import checkAnalog, checkCatalog, getCatalog, get_alldataSheet
from parser.driver import Driver
from product import Product
from selenium.webdriver.common.by import By



class testStepOne(unittest.TestCase):

    def test_checkProduct(self):
        driver = Driver().getDriver()
        driver.execute_script('''window.open("http://google.com","_blank");''')
        catalog = Productlinq(
            "Интегральные микросхемы",
            "AC/DC конвертеры",
            "https://www.chipfind.ru/catalog/testeq/accessories/"
        )
        products = getCatalog(driver=driver,catalog=catalog)
        self.assertEqual(len(products),302)
        self.assertEqual(302, Product.count)

    def test_check_analog(self):
         driver = Driver().getDriver()
         self.assertEqual(checkAnalog(driver,"https://www.chipfind.ru/catalog/ic/ac-dc-converters/avs1acp08.htm?"),[])
         self.assertEqual(checkAnalog(driver,"https://www.chipfind.ru/catalog/ic/ac-dc-converters/fs6x0420rj.htm?"),["FS6X0420RJX"])

    def test_getCatalogs(self):
        driver = Driver().getDriver()
        catalogItem:Productlinq  = checkCatalog(driver=driver)
        self.assertEqual(catalogItem[0].type, "AC/DC конвертеры")
        self.assertEqual(catalogItem[len(catalogItem) - 1].type, "Приборы для поиска повреждений в цепи")


class TestStepTwo(unittest.TestCase):

    def test_get_alldataSheet(self):
        driver = Driver().getDriver()
        self.assertEqual(get_alldataSheet("AVS1ACP08", driver), "AVS1ACP08")
        self.assertEqual(get_alldataSheet("	6AM-6PA", driver), "")
        self.assertEqual(get_alldataSheet("	6LR61XWA/1SB", driver), "")
        self.assertEqual(get_alldataSheet("	AD1990Acpz ", driver), "AD1990ACPZ")
 