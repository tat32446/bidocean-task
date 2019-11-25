from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException

import pandas as pd

Data=[]
chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_argument("--start-maximized")
chromeOptions.add_argument("--headless")
driver = webdriver.Chrome(chrome_options=chromeOptions,executable_path='chromedriver')
driver.get('https://www.lazada.sg/#')
timeout = 30
try:
    WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.ID, "Level_1_Category_No1")))
except TimeoutException:
    driver.quit()


try:
    category_element = driver.find_element(By.ID,'Level_1_Category_No1').text
except NoSuchElementException as exception:
    print('Level_1_Category_No1 Element not Found!!')
#result -- Electronic Devices as the first category listing

##list_category_elements = driver.find_element(By.XPATH,'//*[@id="J_icms-5000498-1511516689962"]/div/ul')
try:
    list_category_elements = driver.find_element(By.XPATH,'//UL[@class="lzd-site-menu-root"]')
except NoSuchElementException as exception:
    print('//UL[@class="lzd-site-menu-root XPATH Not Found !!')

try:
    links = list_category_elements.find_elements(By.CLASS_NAME,"lzd-site-menu-root-item")
except NoSuchElementException as exception:
    print('Class Name:lzd-site-menu-root-item not Found!!')
for i in range(len(links)):
    print("element in list ",links[i].text)
#result {Electronic Devices, Electronic Accessories, etc}
try:
    element = driver.find_elements_by_class_name('J_ChannelsLink')[2]
except NoSuchElementException as exception:
    print('J_ChannelsLink class name not Found!!')


print(element)
webdriver.ActionChains(driver).move_to_element(element).click(element).perform()

product_titles = driver.find_elements_by_class_name('title')
for title in product_titles:
    print(title.text)
product_containers = driver.find_elements_by_class_name('product_container')

for container in product_containers:
    product_titles=(container.find_element_by_class_name('title').text)
    pack_sizes=(container.find_element_by_class_name('pack_size').text)
    product_prices=(container.find_element_by_class_name('product_price').text)
    rating_counts=(container.find_element_by_class_name('ratings_count').text)
    Dict={ }
    Dict={'product_title': product_titles, 'pack_size': pack_sizes,'product_price': product_prices, 'rating_count': rating_counts}
    Data.append(Dict)
driver.close()   
df_product = pd.DataFrame(Data)
df_product.to_csv('product_info.csv')