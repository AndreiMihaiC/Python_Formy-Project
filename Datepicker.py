import time

from assertpy import soft_assertions, assert_that
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest


class Website(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://formy-project.herokuapp.com/datepicker')
        self.driver.maximize_window()

    # TODO: Open the website and select the current day::

    def test_todaySelect(self):

        clickFormy = self.driver.find_element(By.ID, 'datepicker')
        clickFormy.click()

        searchToday = self.driver.find_element(By.CLASS_NAME, 'today')

        print(f'The current day is:: {searchToday.text}')
        searchToday.click()

        currentDay = self.driver.find_element(By.XPATH, "//input[@id='datepicker' and @class='form-control']")
        time.sleep(3)

        with soft_assertions():
            assert_that(currentDay).is_true()

    # TODO: We open the website and display how many days the current month has:

    def test_daysMonths(self):
        datePicker = self.driver.find_element(By.ID, 'datepicker')

        datePicker.click()
        time.sleep(2)

        currentMonth = self.driver.find_element(By.CLASS_NAME, 'datepicker-switch').text

        currentMonthDays = self.driver.find_elements(By.XPATH,
                                                     '//td[contains(@class,"day") and not (contains(@class,"old")) and not  (contains(@class,"new"))]')
        numberOfDays = len(currentMonthDays)

        print(f'Current month:{currentMonth} has {numberOfDays} days.')
        time.sleep(3)

    # TODO: We navigate the calendar using the ">>" button until the year 2015:

    def test_navigation1(self):

        datePickerButton = self.driver.find_element(By.XPATH, "//input[@id='datepicker' and @placeholder='mm/dd/yyyy']")
        datePickerButton.send_keys('1/1/2015')
        datePickerButton.click()
        time.sleep(3)

    # TODO:       OR:

    def test_navigation2(self):
        clickDatepicker = self.driver.find_element(By.ID, 'datepicker')
        clickDatepicker.click()

        prevButton = (self.driver.find_element(By.CLASS_NAME, 'prev'))

        while True:
            currentYear = self.driver.find_element(By.XPATH, '//th[@class="datepicker-switch"]').text
            if currentYear != 'January 2016':
                prevButton.click()
            else:
                break

        with soft_assertions():
            assert_that(currentYear).is_not_equal_to('December 2015')

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
