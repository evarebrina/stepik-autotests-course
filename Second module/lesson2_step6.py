import math
from selenium import webdriver

def calc(x):
    return math.log(math.fabs(12*math.sin(x)))

browser = webdriver.Chrome()
browser.get('http://SunInJuly.github.io/execute_script.html')
x = int(browser.find_element_by_id('input_value').text)
input = browser.find_element_by_css_selector('input[type="text"]')
input.send_keys(str(calc(x)))
browser.find_element_by_id('robotCheckbox').click()
radio = browser.find_element_by_id('robotsRule')
browser.execute_script('return arguments[0].scrollIntoView(true);',radio)
radio.click()
button = browser.find_element_by_css_selector('button[type="submit"]')
browser.execute_script('return arguments[0].scrollIntoView(true);', button)
button.click()
#browser.quit()