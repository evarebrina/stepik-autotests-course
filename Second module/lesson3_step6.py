from selenium import webdriver
import math


def calc(x):
    return math.log(math.fabs(12*math.sin(x)))

browser = webdriver.Chrome()

browser.get('http://suninjuly.github.io/redirect_accept.html')

browser.find_element_by_css_selector('button[type="submit"]').click()
browser.switch_to.window(browser.window_handles[1])

x = int(browser.find_element_by_id('input_value').text)
browser.find_element_by_id('answer').send_keys(str(calc(x)))
browser.find_element_by_css_selector('button[type="submit"]').click()