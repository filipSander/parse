from os import getcwd
import shutil
import threading
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from fake_useragent import UserAgent



class Driver:
    options = webdriver.ChromeOptions()
    options.binary_location = r"C:\Users\csw\AppData\Local\CentBrowser\Application\chrome.exe"
    
    driver: webdriver.Chrome
    pathProfile: str

    def __init__(self):
        self.pathProfile = f"{getcwd()}//parser//profiles//p{threading.get_ident()}"
        shutil.copytree(f"{getcwd()}//parser//profile", self.pathProfile)
        self.openDriver()


    def openDriver(self):
        print("Открытие драйвера")
        self.options.add_experimental_option("excludeSwitches", ["enable-logging"])
        self.options.add_argument('--disable-blink-features=AutomationControlled')
        self.options.add_argument(f"user-data-dir={self.pathProfile}")
        self.options.add_argument(f"user-agent={UserAgent().random}") 
        # self.options.headless = True
        self.driver = webdriver.Chrome(
            service = Service(getcwd() + r"\parser\chromedriver.exe"),
            options = self.options
        )
        self.driver.switch_to.new_window('tab')
        self.driver.switch_to.new_window('tab')
        self.driver.switch_to.window(self.driver.window_handles[0])



    def changeUA(self):
        self.closeDriver()
        self.openDriver()
        print(self.driver.execute_script("return navigator.userAgent"))

    def closeDriver(self):
        print("Закрытие драйвера")
        self.driver.close()
        self.driver.quit()

    def getDriver(self):
        return self.driver