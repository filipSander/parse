from time import sleep, time
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
        count = 0
        for catalog in catalogItems:
            if catalog.group == group:
                print("Парсинг каталога " + catalog.type + "..")
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
        print("_________________________>>>> Ахтунг - " + ex)

    finally:
        tread_browser.closeDriver() 

def main():
    try: 
        browser = Driver()
        print("Поиск групп и каталогов..")
        catalogItems: Productlinq  = checkCatalog(driver=browser.getDriver())
    
    except Exception as ex:
        print("_________________________>>>> Ахтунг в точке входа - " + ex)

    finally:
        browser.closeDriver()
        group:str = []
        for c in catalogItems:
            if not c.group in group:
                group.append(c.group)

        i = 0
        threads = []
        for g in group:
            tr = threading.Thread(target=theadGetCatalog,args=(g,catalogItems))
            tr.start()
            threads.append(tr)
            print(f"Создан поток {i}")
            if i == 8 or i == 16 or i == 24 or i == 32:
                print("Разгрузка потока")
                for t in threads:
                    t.join()
                threads = []
            i+=1
            sleep(5)

if __name__ == "__main__":
    start = time()
    main()
    print("Время: ", "%.2f" %start - time())
    