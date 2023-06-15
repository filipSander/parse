import openpyxl

from parser.productlinq import Productlinq
from parser.func import checkCatalog, getCatalog
from parser.driver import Driver
from product import Product


try: 
    browser = Driver()
    catalogItems: Productlinq  = checkCatalog(driver=browser.getDriver())
    count = 0
    for catalog in catalogItems:
        print("Парсинг каталога " + catalog.type)
        products: Product = getCatalog(
            driver=browser.getDriver(),
            catalog=catalog
        )
        exel = openpyxl.open("dump.xlsx")
        for p in products:
            if count < 1000000 :
                exel.worksheets[0].append(p.getAttr())
            else:
                exel.worksheets[1].append(p.getAttr())
            count += 1
        exel.save("dump.xlsx")
        print(f"Записанно товаров - {count}")
        browser.changeUA()

except Exception as ex:
    print(ex)

finally:
    browser.closeDriver()