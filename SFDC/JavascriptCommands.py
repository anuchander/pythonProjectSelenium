from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://www.amazon.in")
time.sleep(10)
driver.find_element(By.LINK_TEXT,"Best Sellers").click()
time.sleep(5)

#scroll to bottom of page
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
time.sleep(5)

