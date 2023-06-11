from time import sleep
from parser.step_two import get_alldataSheet
from parser.driver import driver
from product import Product

try:
    get_alldataSheet("AVS1ACP08")

except Exception as ex:
    print(ex)
    
finally:
    driver.close()
    driver.quit()