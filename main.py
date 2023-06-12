from time import sleep
from parser.step_two import get_alldataSheet
from parser.step_one import checkProduct
from parser.driver import Driver
from product import Product



try:
    browser = Driver()
    checkProduct(browser.getDriver())
    

except Exception as ex:
    print(ex)

finally:
    browser.closeDriver()
    
