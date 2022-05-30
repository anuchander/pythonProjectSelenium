from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


driver=webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://www.hyrtutorials.com")
driver.maximize_window()
driver.find_element(By.XPATH, "//a[contains(text(), 'Selenium Practice')]").click()
time.sleep(10)
print('Selenium Practice clicked')
#driver.find_element(By.LINK_TEXT, "XPath Practice").click()
driver.find_element(By.XPATH, "//a[contains(text(), 'XPath Practice')]").click()
time.sleep(10)
print('XPath Practice clicked')
driver.find_element(By.XPATH, "//label[text()='Email']/following::input[1]").send_keys("abc@gmail.com")
time.sleep(10)
print('test completed!')

#use ancescestors- gives all ancescetors, index gives which ancescestor
#getval = driver.find_element(By.XPATH, "//label[text()='Last Name']/ancestor::div[1]]")
#print(getval)

#enter val in firstname
driver.find_element(By.XPATH, "//div[@class='container']/child::input[@type='text'][1]").send_keys("Hello World!")
time.sleep(10)

driver.execute_script("window.scrollTo(0,1200)")
time.sleep(10)
print("Scrolled Down!")
driver.find_element(By.XPATH, "//div[@class='container']/descendant::button[1]").click()
print("button Clicked")

driver.find_element(By.XPATH, "//td[text()='Maria Anders']/preceding-sibling::td/child::input").click
time.sleep(10)
print("Checkbox clicked")
'''

driver.get("http://www.w3schools.com")
driver.maximize_window()
time.sleep(5)
driver.find_element(By.LINK_TEXT, "Tutorials").click()
time.sleep(10)
driver.find_element(By.XPATH, "//a[contains(text(),'Learn HTML')][1]").click()
time.sleep(10)
driver.find_element(By.XPATH, "//a[contains(text(),'HTML Tables')]").click()
time.sleep(10)

#print Alfred Futterkiste from Maria Anders using Axes
tval = driver.find_element(By.XPATH, "//td[text()='Maria Anders']/preceding-sibling::td")
print(tval.text)

#method 2 for printing Alfred Futterkiste from Maria Anders using Axes
tval = driver.find_element(By.XPATH, "//td[text()='Maria Anders']/preceding::td")
print(tval.text)

#method 3 for printing Alfred Futterkiste from 	Roland Mendel using Axes
tval = driver.find_element(By.XPATH, "//td[text()='Roland Mendel']/preceding::td[7]")
print(tval.text)

#print Germany from Maria Anders using Axes
tval = driver.find_element(By.XPATH, "//td[text()='Maria Anders']/following-sibling::td")
print(tval.text)

#print Germany from Maria Anders using Axes
tval = driver.find_element(By.XPATH, "//td[text()='Maria Anders']/following::td")
print(tval.text)

#print Austria from Maria Anders using Axes
tval = driver.find_element(By.XPATH, "//td[text()='Maria Anders']/following::td[7]")
print(tval.text)

'''