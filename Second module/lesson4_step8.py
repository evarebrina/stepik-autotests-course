from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import math


def calc(x):
    return math.log(math.fabs(12*math.sin(x)))

browser = webdriver.Chrome()

browser.get('http://suninjuly.github.io/explicit_wait2.html')

button = browser.find_element_by_id('book')
price = browser.find_element_by_id('price')
WebDriverWait(browser, 12).until(expected_conditions.text_to_be_present_in_element((By.ID, 'price'), text_='10000 RUR'))
button.click()
x = int(browser.find_element_by_id('input_value').text)
browser.find_element_by_id('answer').send_keys(str(calc(x)))
browser.find_element(value='solve').click()