from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException
from pathlib import Path

chromeOptions = webdriver.ChromeOptions()
##chromeOptions.add_argument("--start-maximized")

driver = webdriver.Chrome(chrome_options=chromeOptions,executable_path='chromedriver')
html_file = Path.cwd() / "sample.html"

driver.get(html_file.as_uri());


usernameElement = driver.find_element_by_id("idUsername")
passwordElement = driver.find_element_by_id("idPassword")

usernameElement.send_keys("testuser")

driver.find_element_by_id("reloadLink").click()

try:
    passwordElement.send_keys("password")
except StaleElementReferenceException as Exception:
    print ('StaleElementReferenceException while trying to type password, trying to find element again')
    passwordElement = driver.find_element_by_id("idPassword")
    passwordElement.send_keys("password")

driver.close()