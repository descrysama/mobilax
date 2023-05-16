from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

def initBrowser(headless):
    options = webdriver.FirefoxOptions()
    firefox_profile = webdriver.FirefoxProfile()
    firefox_profile.set_preference("browser.privatebrowsing.autostart", True)
    if(headless):
        options.add_argument('--headless')
    try:
        driver = webdriver.Firefox(service=Service(executable_path=GeckoDriverManager().install()), options=options, firefox_profile=firefox_profile)
        return driver
    except Exception as err:
        print(err)
