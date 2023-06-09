from selenium.webdriver.common.by import By
from .driver import driver


def get_alldataSheet(name):
    url = "https://www.alldatasheet.com/view.jsp?Searchword="
    condition = f'//div/table/tbody/tr/td/table/tbody/tr/td/a'
    
    driver.get(url=url + name)
    rows = driver.find_elements(By.XPATH, condition)

    for r in rows:
        if r.text.strip().lower() == name.strip().lower():
            return r.text
    return ''
        





