from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://selectorshub.com/xpath-practice-page")
time.sleep(10)
driver.maximize_window()
time.sleep(30)
abc = driver.find_element(By.ID, "userId").send_keys("test@tesla.com")
time.sleep(20)
print(abc)
driver.execute_script("window.scrollTo(0,550)")
time.sleep(10)
driver.switch_to.frame("pact")
time.sleep(25)
print("Switched to frame successfully")
webele = driver.execute_script("return document.querySelector(\"#snacktime\").shadowRoot.querySelector(\"#tea\")")
print(webele)
js = "arguments[0].setAttribute('value', 'Green Masala Tea')"
print(js)
driver.execute_script(js, webele)
time.sleep(25)
webele2 = driver.execute_script("return document.querySelector(\"#snacktime\").shadowRoot.querySelector(\"#app2\").shadowRoot.querySelector(\"#pizza\")")
print(webele2)
js2 = "arguments[0].setAttribute('value', 'Sambar Sadam')"
print(js2)
driver.execute_script(js2, webele2)
time.sleep(25)
print("Shadow root element value printed")
time.sleep(20)

'''
driver.get("http://www.google.com")
inputval=driver.execute_script("return document.querySelector('ntp-app').shadowRoot.querySelector("#realbox").shadowRoot.querySelector("#input"))
#js = "arguments[0].setAttribute('value', 'python')"
driver.execute_script("arguments[0].setAttribute('value', 'python')", inputval)
'''

print("test shadow root")

