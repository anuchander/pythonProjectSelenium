from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://www.amazon.in")
time.sleep(10)

ddbox=driver.find_element(By.ID, "searchDropdownBox")
ddbox.click()
time.sleep(5)
drp=Select(ddbox)
drp.select_by_visible_text("Clothing & Accessories")
time.sleep(5)
drp.select_by_index(5)
time.sleep(5)
drp.select_by_value("search-alias=appliances")
time.sleep(5)

