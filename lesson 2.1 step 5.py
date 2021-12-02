from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/math.html")
    button = browser.find_element_by_id("robotsRule")
    button.click()
    x = browser.find_element_by_id('input_value')
    x = x.text
    field = browser.find_element_by_id("answer")
    field.send_keys(calc(x))
    check_button = browser.find_element_by_id("robotCheckbox")
    check_button.click()
    submit = browser.find_element_by_class_name('btn')
    submit.click()

finally:
    time.sleep(4)
    browser.quit()
