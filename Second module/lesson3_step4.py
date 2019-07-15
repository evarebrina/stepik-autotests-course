from selenium import webdriver
import math

def calc(x):
    return str(math.log(math.fabs(12 * math.sin(x))))

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/alert_accept.html')
browser.find_element_by_tag_name('button').click()
alert = browser.switch_to.alert
alert.accept()
x = int(browser.find_element_by_id('input_value').text)
browser.find_element_by_id('answer').send_keys(calc(x))
browser.find_element_by_css_selector('button[type="submit"]').click()
