from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

class DemoHiddenElements():
    def demo_is_displayed(self):
        driver=webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.w3schools.com/howto/howto_js_toggle_hide_show.asp")
        time.sleep(10)
        driver.maximize_window()
        time.sleep(2)
        print(driver.find_element(By.XPATH, "//div[@id='myDIV']").is_displayed())
        driver.find_element(By.XPATH, "//button[@class='ws-btn w3-hover-black w3-dark-grey']").click()
        time.sleep(2)
        print(driver.find_element(By.XPATH, "//div[@id='myDIV']").is_displayed())
        print("Test Completed!")

    def demo_is_displayed_yatra(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https:yatra.com/hotels")
        time.sleep(10)
        driver.maximize_window()
        time.sleep(5)
        driver.find_element(By.XPATH, "//span[normalize-space()='Traveller']").click()
        time.sleep(2)
        x=2
        print(driver.find_element(By.XPATH, "(//span[@class='ddSpinnerPlus'])['x']"))
        driver.find_element(By.XPATH, "(//span[@class='ddSpinnerPlus'])['x']").click()
        print("Object clicked")
        #time.sleep(2)
        #print(driver.find_element(By.XPATH, "(//select[@class='ageselect'])[1]").is_displayed())
        #time.sleep(5)
       # driver.find_element(By.XPATH, "(//span[@class='ddSpinnerMinus disabled'])[1]").click()
        #time.sleep(5)
        #print(driver.find_element(By.XPATH, "//select[@class='ageselect'][1]").is_displayed())

demo=DemoHiddenElements()
#demo.demo_is_displayed()
demo.demo_is_displayed_yatra()