from os import getcwd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from fake_useragent import UserAgent

options = webdriver.ChromeOptions()
options.binary_location = r"C:\Users\csw\AppData\Local\CentBrowser\Application\chrome.exe"
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_argument('--disable-blink-features=AutomationControlled')
# options.add_argument(f"user-agent={UserAgent().random}") 
options.add_argument(f"user-data-dir={getcwd()}//parser//profile")

driver = webdriver.Chrome(
    service = Service(getcwd() + r"\parser\chromedriver.exe"),
    options = options
)
