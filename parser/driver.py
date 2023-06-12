from os import getcwd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from fake_useragent import UserAgent



class Driver:
    options = webdriver.ChromeOptions()
    # options.binary_location = r"C:\Users\csw\AppData\Local\CentBrowser\Application\chrome.exe"
    driver: webdriver.Chrome
    
    def __init__(self):
        self.openDriver()


    def openDriver(self):
        print("Открытие драйвера")
        self.options.add_experimental_option("excludeSwitches", ["enable-logging"])
        self.options.add_argument('--disable-blink-features=AutomationControlled')
        self.options.add_argument(f"user-data-dir={getcwd()}//parser//profile")
        # self.options.add_argument(f"user-agent={UserAgent().random}") 
        self.driver = webdriver.Chrome(
            service = Service(getcwd() + r"\parser\chromedriver.exe"),
            options = self.options
        )

    def changeUA(self):
        self.closeDriver()
        self.openDriver()

    def closeDriver(self):
        print("Закрытие драйвера")
        self.driver.close()
        self.driver.quit()

    def getDriver(self):
        return self.driver
    
    def checkUA(self):
        print(self.driver.execute_script("return navigator.userAgent"))
    



