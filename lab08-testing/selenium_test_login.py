import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture(scope="module")
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")   # chạy ngầm
    driver = webdriver.Chrome(options=options)
    driver.get("http://localhost:5500/labs/lab04-login/index.html")  # thay bằng URL form login
    yield driver
    driver.quit()

def test_login_success(driver):
    driver.find_element(By.ID, "username").send_keys("demo")
    driver.find_element(By.ID, "password").send_keys("1234")
    driver.find_element(By.ID, "loginBtn").click()
    assert "Dashboard" in driver.page_source or "Login success" in driver.page_source

def test_login_wrong(driver):
    driver.find_element(By.ID, "username").clear()
    driver.find_element(By.ID, "password").clear()
    driver.find_element(By.ID, "username").send_keys("demo")
    driver.find_element(By.ID, "password").send_keys("wrong")
    driver.find_element(By.ID, "loginBtn").click()
    assert "Invalid login" in driver.page_source

def test_login_empty(driver):
    driver.find_element(By.ID, "username").clear()
    driver.find_element(By.ID, "password").clear()
    driver.find_element(By.ID, "loginBtn").click()
    assert "Please enter username" in driver.page_source or "required" in driver.page_source
