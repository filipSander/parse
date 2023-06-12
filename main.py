from time import sleep
from parser.productlinq import Productlinq
from parser.step_two import get_alldataSheet
from parser.step_one import checkProduct, getCatalog
from parser.driver import Driver
from product import Product



try:
    browser = Driver()
    driver = browser.getDriver()

    product = Productlinq(
        "Интегральные микросхемы",
        "AC/DC конвертеры",
        "https://www.chipfind.ru/catalog/testeq/accessories/"
    )

    getCatalog(driver=driver,catalog=product)
    

except Exception as ex:
    print(ex)

finally:
    browser.closeDriver()
    
