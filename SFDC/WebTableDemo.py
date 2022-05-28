from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.w3schools.com/html/html_tables.asp")

webtable = driver.find_element(By.XPATH, "//table[@id='customers']/tbody")
print(webtable.text)
#print("*********")
header=driver.find_elements(By.XPATH, "//table[@id='customers']/tbody/tr[1]/th")
print(len(header))
for i in header:
    print(i.text, end=" ")
print()
rows=webtable.find_elements(By.TAG_NAME, "tr")
for i in rows:
    cols=i.find_elements(By.TAG_NAME, "td")
    for j in cols:
        print(j.text, end=",  ")
    print()

