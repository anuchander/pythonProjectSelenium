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
driver.find_element(By.XPATH, "//a[@title='My Profile']").click()
time.sleep(5)
'''
#make a post
post=driver.find_element(By.XPATH, "//span[normalize-space()='Post']")
post.click()
time.sleep(5)
WindowHandleBefore=driver.current_window_handle
print(WindowHandleBefore)
frameid=driver.find_element(By.XPATH, "//iframe[@title='Rich Text Editor, publisherRichTextEditor']")
driver.switch_to.frame(frameid)
print("I am inside frame 0")
textarea=driver.find_element(By.XPATH, "//body")
textarea.send_keys("Hello, this is a new test, in Python!")
time.sleep(10)
driver.switch_to.window(WindowHandleBefore)
driver.find_element(By.ID, "publishersharebutton").click()
time.sleep(10)
print("Test Completed!")
'''
#upload a file
file= driver.find_element(By.XPATH, "//span[normalize-space()='File']")
file.click()
time.sleep(5)
driver.find_element(By.XPATH, "//a[@id='chatterUploadFileAction']").click()
time.sleep(10)
choosefile=driver.find_element(By.XPATH, "//input[@id='chatterFile']")
choosefile.click()
time.sleep(5)
choosefile.send_keys("/Users/anu/Pictures/Scan1.jpeg")
print("File upload completed!")

#inputfile.send_keys("Scan7.jpeg")

#time.sleep(5)






