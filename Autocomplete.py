import time

from selenium import webdriver
from selenium.webdriver.common.by import By

"""------------------------------------------------------------------------------------------------------------------"""

link = 'https://formy-project.herokuapp.com/autocomplete'
driver = webdriver.Chrome()
driver.get(link)

time.sleep(3)
driver.maximize_window()

address = driver.find_element(By.CLASS_NAME,"pac-target-input")
address.send_keys('Popescu')
time.sleep(1)

street_address = driver.find_element(By.ID,"street_number")
street_address.send_keys('100 Flushcombe Road,Albury 2148')
time.sleep(1)

street_address2 = driver.find_element(By.ID,"route")
street_address2.send_keys('	100 Boulevard Alexis-Nihon,Suite 310,Montreal,H4M 2N7,Canada')
time.sleep(1)

city = driver.find_element(By.ID,"locality")
city.send_keys('Zurich')
time.sleep(1)

state = driver.find_element(By.ID,"administrative_area_level_1")
state.send_keys('Deutschland')
time.sleep(1)

zip_code = driver.find_element(By.ID,"postal_code")
zip_code.send_keys('00000')
time.sleep(1)

country = driver.find_element(By.ID,"country")
country.send_keys('Deutschland')
time.sleep(1)