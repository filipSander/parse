from selenium.webdriver.common.by import By
from selenium import webdriver

 

def get_alldataSheet(name, driver: webdriver.Chrome):

    url = "https://www.alldatasheet.com/view.jsp?Searchword="
    condition = '//div/table/tbody/tr/td/table/tbody/tr/td/a'
    
    driver.get(url=url + name)
    rows = driver.find_elements(By.XPATH, condition)

    for r in rows:
        if r.text.strip().lower() == name.strip().lower():
            return r.text
    return ''
        





