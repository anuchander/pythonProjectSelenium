from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

class DemoParameterizeXPathElements():
    def demo_is_displayed(self):
        driver=webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://html5-tutorial.net/try.html#pre3")
        time.sleep(10)
        driver.maximize_window()
        time.sleep(2)
        x=1
        print(driver.find_element(By.XPATH, "(//code[@class='hljs xml'])['x']"))
        print(driver.find_element(By.XPATH, "(//code[@class='hljs xml'])['x']").is_displayed())

        print("Test Completed!")

demo=DemoParameterizeXPathElements()
demo.demo_is_displayed()