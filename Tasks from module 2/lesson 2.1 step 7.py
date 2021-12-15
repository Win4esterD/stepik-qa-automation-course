from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/get_attribute.html")
    button = browser.find_element_by_id("robotsRule")
    button.click()
    x = browser.find_element_by_id('treasure')
    x_value = x.get_attribute("valuex")
    field = browser.find_element_by_id("answer")
    field.send_keys(calc(x_value))
    check_button = browser.find_element_by_id("robotCheckbox")
    check_button.click()
    submit = browser.find_element_by_class_name('btn')
    submit.click()

finally:
    time.sleep(4)
    browser.quit()
