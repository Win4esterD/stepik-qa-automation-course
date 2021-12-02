import time
from selenium import webdriver
import math

link = "http://suninjuly.github.io/alert_accept.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element_by_class_name("btn")
    button.click()
    alert = browser.switch_to.alert
    alert.accept()
    x = browser.find_element_by_id("input_value")
    x = x.text
    x = int(x)
    field = browser.find_element_by_id("answer")
    field.send_keys(calc(x))
    button2 = browser.find_element_by_class_name("btn")
    button2.click()


finally:
    time.sleep(7)
    browser.quit()
