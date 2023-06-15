from time import sleep
import openpyxl
from os import getcwd
import threading


from parser.productlinq import Productlinq
from parser.func import checkCatalog, getCatalog
from parser.driver import Driver
from product import Product

def theadGetCatalog(group: str, catalogItems: Productlinq):
    docPath = f"{getcwd()}\\exel\\{group}-dump.xlsx"
    exel = openpyxl.Workbook().save(docPath)
    
    print("Парсинг группы " + group)
    try: 
        tread_browser = Driver()
        count = 2
        for catalog in catalogItems:
            if catalog.group == group:
                print("Парсинг каталога " + catalog.type)
                products: Product = getCatalog(
                    driver=tread_browser.getDriver(),
                    catalog=catalog
                )
                exel = openpyxl.open(docPath)
                for p in products:
                    exel.worksheets[0].append(p.getAttr())
                    count += 1
                exel.save(docPath)
                print(f"Записанно товаров - {count}")
    except Exception as ex:
        print(ex)

    finally:
        tread_browser.closeDriver() 

def main():
    try: 
        browser = Driver()
        catalogItems: Productlinq  = checkCatalog(driver=browser.getDriver())
        browser.closeDriver()
        
        group:str = []
        for c in catalogItems:
            if not c.group in group:
                group.append(c.group)

        print(group)
        for g in group:
            threading.Thread(target=theadGetCatalog,args=(g,catalogItems)).start()
            sleep(30)

    finally:
        pass

if __name__ == "__main__":
    main()
    