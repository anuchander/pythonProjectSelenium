from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://www.google.com")
inputval=driver.execute_script("return document.querySelector('ntp-app').shadowRoot.querySelector("#realbox").shadowRoot.querySelector("#input"))
#js = "arguments[0].setAttribute('value', 'python')"
driver.execute_script("arguments[0].setAttribute('value', 'python')", inputval)


