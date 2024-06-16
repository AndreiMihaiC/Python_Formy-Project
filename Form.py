import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from assertpy import soft_assertions, assert_that
"""------------------------------------------------------------------------------------------------------------------"""

link = 'https://formy-project.herokuapp.com/form'
driver = webdriver.Chrome()
driver.get(link)

time.sleep(3)
driver.maximize_window()

first_name = driver.find_element(By.CSS_SELECTOR,"input[placeholder='Enter first name']")
first_name.send_keys('Popescu')
time.sleep(1)

last_name = driver.find_element(By.XPATH,"//input[@id='last-name']")
last_name.send_keys('Andrei')
time.sleep(1)

job_title = driver.find_element(By.ID,"job-title")
job_title.send_keys('QA')
time.sleep(1)

high_school = driver.find_element(By.ID,'radio-button-1')
high_school.click()
time.sleep(1)

sex = driver.find_element(By.CSS_SELECTOR,"input[id='checkbox-2']")
sex.click()
time.sleep(1)

clickExperience = driver.find_element(By.CSS_SELECTOR,'select.form-control').click()
experience = driver.find_element(By.XPATH,"//option[text()='0-1']")
experience.click()
time.sleep(1)

openDatePicker = driver.find_element(By.XPATH,"//input[@id='datepicker']")
openDatePicker.click()
today = driver.find_element(By.CLASS_NAME, 'today')
today.click()
time.sleep(1)

buttonSubmit = driver.find_element(By.CSS_SELECTOR,'.btn.btn-lg.btn-primary')
buttonSubmit.click()
time.sleep(1)

success_message = driver.find_element(By.XPATH,'/html/body/div/h1')

with soft_assertions():
    assert_that(success_message).is_true()

time.sleep(3)
driver.quit()