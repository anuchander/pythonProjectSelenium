from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://www.google.com")
driver.find_element(By.NAME, 'q').send_keys("Java")
time.sleep(10)
#a=driver.find_elements_by_tag_name('a')
a=driver.find_elements(By.XPATH, "//ul[@role='listbox']/li/descendant::div[@class='wM6W7d']")
print(len(a))
for i in a:
    print(i.text)
    if i.text=='java arraylist':
        i.click()
        break
