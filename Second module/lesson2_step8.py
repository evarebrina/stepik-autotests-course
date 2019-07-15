import os
from selenium import webdriver
browser = webdriver.Chrome()

browser.get('http://suninjuly.github.io/file_input.html')

browser.find_element_by_css_selector('input[name="firstname"]').send_keys('123')
browser.find_element_by_css_selector('input[name="lastname"]').send_keys('123')
browser.find_element_by_css_selector('input[name="email"]').send_keys('123')

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file.txt')


browser.find_element_by_id('file').send_keys(file_path)

browser.find_element_by_css_selector('button[type="submit"').click()