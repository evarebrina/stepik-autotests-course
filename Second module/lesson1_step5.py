from selenium import webdriver
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/get_attribute.html')

chest = browser.find_element_by_css_selector('#treasure')
x = chest.get_attribute('valuex')
answer = browser.find_element_by_css_selector('#answer')
answer.send_keys(calc(x))
checkbox = browser.find_element_by_css_selector('#robotCheckbox')
checkbox.click()
radio = browser.find_element_by_css_selector('#robotsRule')
radio.click()
button = browser.find_element_by_css_selector('button[type="submit"]')
button.click()