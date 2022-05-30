from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
import time

browser='firefox'
if browser=='firefox':
    #driver = webdriver.Firefox(executable_path="/Users/anu/Software/geckodriver")
    driver=webdriver.Firefox(executable_path=GeckoDriverManager().install())
elif browser=='chrome':
    driver=webdriver.Chrome(ChromeDriverManager().install())
elif browser=='safari':
    driver=webdriver.safari
driver.get("http://www.google.com")
driver.maximize_window()
time.sleep(10)
driver.find_element(By.NAME, 'q').send_keys("Java")
time.sleep(10)
