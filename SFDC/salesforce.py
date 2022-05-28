from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


driver=webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get('https:login.salesforce.com')
driver.find_element(By.ID, "username").send_keys("test@tek.com")
driver.find_element(By.ID, "password").send_keys("changesales1")
driver.find_element(By.ID, "Login").click()
time.sleep(10)

driver.find_element(By.XPATH, "//span[@id='userNavLabel']").click()
time.sleep(5)
driver.find_element(By.XPATH, "//a[@title='Logout']").click()
print("Test Completed!")




