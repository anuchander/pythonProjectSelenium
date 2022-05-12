import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import allure

@pytest.fixture()
def test_setup():
    global driver
    driver=webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    yield
    driver.quit()

@allure.description("Validate Salesforce.com with valid login credentials")
@allure.severity(severity_level="CRITICAL")
def test_validLogin(test_setup):

    driver.get('https:login.salesforce.com')
    enter_username("test@tek.com")
    enter_password("salesforce1")
    driver.find_element_by_id("Login").click()
    Expected_title='Home Page ~ Salesforce - Developer Edition'
    Actual_title=driver.title
    assert (driver.title==Expected_title),"Values not equal"
    print("success, passed")

@allure.description("Validate Salesforce.com with invalid login credentials")
@allure.severity(severity_level="NORMAL")
def test_invalidLogin(test_setup):

    driver.get('https:login.salesforce.com')
    enter_username("test@tek.com")
    enter_password("salesforce2")
    driver.find_element_by_id("Login").click()
    Expected_title='Home Page ~ Salesforce - Developer Edition'
    Actual_title=driver.title
    try:
        assert (driver.title==Expected_title),"Values not equal"
        print("success, passed")
    finally:
        if(AssertionError):
            allure.attach(driver.get_screenshot_as_png(), name="Invalid Credentials", attachment_type=allure.attachment_type.PNG)

@allure.step("Entering username as {0}")
def enter_username(username):
    driver.find_element_by_id("username").send_keys(username)

@allure.step("Entering username as {0}")
def enter_password(password):
    driver.find_element_by_id("password").send_keys(password)