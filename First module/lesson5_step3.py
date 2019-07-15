from selenium import webdriver
import math

link = "http://suninjuly.github.io/registration2.html"
browser = webdriver.Chrome()
browser.get(link)

elem = browser.find_element_by_css_selector('input[placeholder="Введите имя"')
elem.send_keys('Name')
elem = browser.find_element_by_css_selector('input[placeholder="Введите фамилию"')
elem.send_keys('Surname')
elem = browser.find_element_by_css_selector('input[placeholder="Введите Email"')
elem.send_keys('email@email.com')

button = browser.find_element_by_xpath('//button[contains(text(), "Отправить")]')
button.click()
browser.quit()