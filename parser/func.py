from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver
from .driver import Driver

from selenium.common.exceptions import StaleElementReferenceException

from product import Product
from .productlinq import Productlinq



def getCatalogPagesCount(pages):
    """
    Возвращает количество страниц в каталоге
    """
    if len(pages) == 0:
        return 1
    else:
        lastLinq = pages[-1].get_attribute("href").split("/")
        lastNum = lastLinq[-1].split(".")
        return int(lastNum[0])

def checkAnalog(driver: webdriver.Chrome, productLinq):
    """
    Собирает аналоги со страници товара 2я вкладка
    """
    driver.switch_to.window(driver.window_handles[1])
    
    driver.get(url=productLinq)
    condition = '//table[contains(@class, "catdata")]/tbody/tr'

    analogs = []
    try:
        rows = driver.find_elements(By.XPATH, condition)
        for r in range(1, len(rows)):
            td = rows[r].find_elements(By.TAG_NAME,'td')
            analogs.append(td[1].text)
    
    except TypeError as ex:
        pass
    
    except StaleElementReferenceException as ex:
        pass
    
    driver.switch_to.window(driver.window_handles[0])

    return analogs


def getCatalog(driver: webdriver.Chrome, catalog: Productlinq):
    """
    Собирает товары из каталога, на 1й вкладке
    """

    driver.get(url=catalog.linq)
    
    condition = '//div[contains(@class, "pages")]/span/a'
    count = getCatalogPagesCount(pages=driver.find_elements(By.XPATH, condition))
    
    condition = '//table[contains(@class, "catdata")]/tbody/tr'
    products : Product = []

    for i in range(1, count + 1):
        driver.get(url=catalog.linq + str(i) + ".htm?")
        rows = driver.find_elements(By.XPATH, condition)

        for r in range(1, len(rows)):
            try:          
                td = rows[r].find_elements(By.TAG_NAME,'td')
                chipFindURL = td[1].find_element(By.TAG_NAME, 'a').get_attribute("href")
                p = Product(
                        catalog.group,
                        catalog.type,
                        td[1].text,
                        td[2].text,
                        td[3].text
                    )
                p.analogs = checkAnalog(driver, chipFindURL)
                p.alldataSheet = get_alldataSheet(driver=driver, name=td[1].text)
                products.append(p)
                
            except TypeError as ex:
                pass
            except StaleElementReferenceException as ex:
                pass

    return products
        


def checkCatalog(driver: webdriver.Chrome):
    """
    Собирает все каталоги с первого ресурса в структуру Productlinq
    """

    url = "https://www.chipfind.ru/catalog/"
    driver.get(url=url)

    condition = '//tbody/tr/td/div/h3/a'
    groups = driver.find_elements(By.XPATH, condition)

    groupDict = dict()
    for g in groups:
        groupDict[g.text] = g.get_attribute("href")
        g.click()
        sleep(2)

    condition = '/html/body/table[3]/tbody/tr/td/div/div/div/ul/li/a'
    types = driver.find_elements(By.XPATH, condition)

    catalog: Productlinq = []
    for t in types:
        for k,v in groupDict.items():
            if v in t.get_attribute("href"):
                catalog.append(Productlinq(k,t.text,t.get_attribute("href")))

    return catalog

def get_alldataSheet(name, driver: webdriver.Chrome):
    """
    Прыгает в 3ю вкладку и ищет ссылку на запись 
    сопостовляя по имени
    """

    driver.switch_to.window(driver.window_handles[2])
    url = "https://www.alldatasheet.com/view.jsp?Searchword="
    condition = '//div/table/tbody/tr/td/table/tbody/tr/td/a'
    
    driver.get(url=url + name)
    rows = driver.find_elements(By.XPATH, condition)
    alldtSheet = ''
    for r in rows:
        if r.text.strip().lower() == name.strip().lower():
            alldtSheet = r.get_attribute("href")
            break
    driver.switch_to.window(driver.window_handles[0])
    return alldtSheet

        



 