from selenium import webdriver
from selenium.webdriver.support.ui import Select

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/selects1.html')
num1 = browser.find_element_by_id('num1')
num2 = browser.find_element_by_id('num2')
select = Select(browser.find_element_by_tag_name('select'))
select.select_by_value(str(int(num1.text) + int(num2.text)))
button = browser.find_element_by_css_selector('button[type="submit"]')
button.click()