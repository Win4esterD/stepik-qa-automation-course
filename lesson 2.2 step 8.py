import os
from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/file_input.html")
    first_name = browser.find_element_by_name("firstname")
    first_name.send_keys("Pavel")
    last_name = browser.find_element_by_name("lastname")
    last_name.send_keys("Winchester")
    email = browser.find_element_by_name("email")
    email.send_keys("fakemail@gmail.com")
    file = browser.find_element_by_name("file")
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, 'file.txt')
    file.send_keys(file_path)
    button = browser.find_element_by_class_name("btn")
    button.click()

finally:
    time.sleep(4)
    browser.quit()
