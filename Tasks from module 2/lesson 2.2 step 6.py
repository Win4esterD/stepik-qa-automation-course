from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/execute_script.html")
    browser.execute_script("window.scrollBy(0, 100);")
    button = browser.find_element_by_id("robotsRule")
    button.click()
    n1 = browser.find_element_by_id("input_value")
    num1 = n1.text
    num1 = int(num1)
    field = browser.find_element_by_id("answer")
    field.send_keys(calc(num1))
    check_button = browser.find_element_by_id("robotCheckbox")
    check_button.click()
    submit = browser.find_element_by_class_name('btn')
    submit.click()

finally:
    time.sleep(9)
    browser.quit()
