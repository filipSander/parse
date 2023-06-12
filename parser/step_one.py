from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver
from .productlinq import Productlinq



def checkProduct(driver: webdriver.Chrome):
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

    productTypes: Productlinq = []
    for t in types:
        for k,v in groupDict.items():
            if v in t.get_attribute("href"):
                productTypes.append(Productlinq(k,t.text,t.get_attribute("href")))

    # print(len(productTypes))
    print(productTypes[0])
    print(productTypes[len(productTypes) - 1])


# /html/body/table[3]/tbody/tr[2]/td[1]/div[1]/div/div/ul/li[54]
# /html/body/table[3]/tbody/tr[2]/td[1]/div[2]/div/div/ul/li[12]
# /html/body/table[3]/tbody/tr[2]/td[1]/div[3]/div/div/ul/li[6]
# /html/body/table[3]/tbody/tr[2]/td[1]/div[4]/div/div/ul/li[16]
# /html/body/table[3]/tbody/tr[2]/td[1]/div[4]/div/div/ul/li[4]
# /html/body/table[3]/tbody/tr[2]/td[1]/div[6]/div/div/ul/li[16]
# /html/body/table[3]/tbody/tr[2]/td[1]/div[7]/div/div/ul/li[3]
# /html/body/table[3]/tbody/tr[2]/td[1]/div[8]/div/div/ul/li[9]
# /html/body/table[3]/tbody/tr[2]/td[1]/div[9]/div/div/ul/li[11]
# /html/body/table[3]/tbody/tr[2]/td[1]/div[10]/div/div/ul/li[9]
# /html/body/table[3]/tbody/tr[2]/td[1]/div[11]/div/div/ul/li[27]
# /html/body/table[3]/tbody/tr[2]/td[1]/div[12]/div/div/ul/li[8]
# /html/body/table[3]/tbody/tr[4]/td[1]/div[1]/div/div/ul/li[20]
# /html/body/table[3]/tbody/tr[4]/td[1]/div[2]/div/div/ul/li[9]
# /html/body/table[3]/tbody/tr[6]/td[1]/div[1]/div/div/ul/li[18]
# /html/body/table[3]/tbody/tr[6]/td[1]/div[2]/div/div/ul/li[7]
# /html/body/table[3]/tbody/tr[8]/td[1]/div[1]/div/div/ul/li[6]
# /html/body/table[3]/tbody/tr[8]/td[1]/div[2]/div/div/ul/li[32]
# /html/body/table[3]/tbody/tr[8]/td[1]/div[3]/div/div/ul/li[11]
# /html/body/table[3]/tbody/tr[8]/td[1]/div[4]/div/div/ul/li[11]
# /html/body/table[3]/tbody/tr[8]/td[1]/div[5]/div/div/ul/li[27]

# /html/body/table[3]/tbody/tr[8]/td[3]/div[5]/div/div/ul/li[32]
# /html/body/table[3]/tbody/tr[2]/td[3]/div[4]/div/div/ul/li[4]
# /html/body/table[3]/tbody/tr[8]/td[3]/div[3]/div/div/ul/li[13]
# /html/body/table[3]/tbody/tr[8]/td[3]/div[2]/div/div/ul/li[10]
# /html/body/table[3]/tbody/tr[8]/td[3]/div[1]/div/div/ul/li[17]
# /html/body/table[3]/tbody/tr[6]/td[3]/div/div/div/ul/li[15]
# /html/body/table[3]/tbody/tr[4]/td[3]/div/div/div/ul/li[19]
# /html/body/table[3]/tbody/tr[2]/td[3]/div[11]/div/div/ul/li[18]
# /html/body/table[3]/tbody/tr[2]/td[3]/div[10]/div/div/ul/li[5]
# /html/body/table[3]/tbody/tr[2]/td[3]/div[9]/div/div/ul/li[9]
# /html/body/table[3]/tbody/tr[2]/td[3]/div[8]/div/div/ul/li[15]
# /html/body/table[3]/tbody/tr[2]/td[3]/div[7]/div/div/ul/li[6]
# /html/body/table[3]/tbody/tr[2]/td[3]/div[6]/div/div/ul/li[4]
# /html/body/table[3]/tbody/tr[2]/td[3]/div[5]/div/div/ul/li[10]
# /html/body/table[3]/tbody/tr[2]/td[3]/div[4]/div/div/ul/li[31]
# /html/body/table[3]/tbody/tr[2]/td[3]/div[3]/div/div/ul/li[26]
# /html/body/table[3]/tbody/tr[2]/td[3]/div[2]/div/div/ul/li[48]
# /html/body/table[3]/tbody/tr[2]/td[3]/div[1]/div/div/ul/li[11]

 