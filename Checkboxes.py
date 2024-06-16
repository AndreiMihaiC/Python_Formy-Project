import time

from selenium import webdriver
from selenium.webdriver.common.by import By

"""------------------------------------------------------------------------------------------------------------------"""

link = 'https://formy-project.herokuapp.com/checkbox'
driver = webdriver.Chrome()
driver.get(link)

time.sleep(3)
driver.maximize_window()

checkbox1 = driver.find_element(By.ID,'checkbox-1')
checkbox1.click()
time.sleep(1)

checkbox2 = driver.find_element(By.ID,'checkbox-2')
checkbox2.click()
time.sleep(1)

checkbox3 = driver.find_element(By.ID,'checkbox-3')
checkbox3.click()
time.sleep(1)
