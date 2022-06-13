from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome(ChromeDriverManager().install())
#driver.get("https://www.app.hubspot.com/login")
driver.get("http://guide.blazemeter.com")
time.sleep(10)
driver.maximize_window()
time.sleep(5)
#driver.find_element_by_css_selector('#username').send_keys('abc@automation.com')
driver.find_element(By.CSS_SELECTOR, 'ul#categories>li:first-of-type+li').click()
print("Element clicked!")
time.sleep(5)

