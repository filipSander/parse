from .driver import driver

def checkProduct():
    url = "https://www.chipfind.ru/catalog/"
    driver.get(url=url)

