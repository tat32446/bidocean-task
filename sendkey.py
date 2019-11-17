
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys

import pandas as pd

Data=[]

driver = webdriver.Chrome(executable_path='chromedriver')
driver.get('https://www.google.com/')
timeout = 30


element = driver.find_element(By.XPATH,'//INPUT[@class="gLFyf gsfi"]')
element.send_keys('testing sendkeys function')
element.send_keys(Keys.RETURN)
element.close()