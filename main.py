import csv

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.firefox.options import Options

options = Options()
# options.headless = True
with webdriver.Firefox(options=options) as driver:
    driver.get("https://bokapass.nemoq.se/Booking/Booking/Index/stockholm")
    driver.find_element(By.NAME, "StartNextButton").click()
    driver.find_element(By.ID, "AcceptInformationStorage").click()
    driver.find_element(By.NAME, "Next").click()
    driver.find_element(By.ID, "ServiceCategoryCustomers_0__ServiceCategoryId").click()
    driver.find_element(By.NAME, "Next").click()
    dropdown = driver.find_element(By.ID, "SectionId")
    dropdown.find_element(By.XPATH, "//option[. = 'Sthlm City']").click()
    driver.find_element(By.NAME, "TimeSearchFirstAvailableButton").click()

    tbl = driver.find_element(By.CSS_SELECTOR, "table.timetable")

    dates = []
    for date in tbl.find_elements_by_css_selector('tbody tr td[headers]'):
        dates += [d.get_attribute('aria-label') for d in date.find_elements_by_css_selector('div.timecell') if d.text != 'Bokad']

print(*dates, sep='\n')
