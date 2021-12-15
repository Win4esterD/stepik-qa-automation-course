import math
import time
from selenium import webdriver
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/redirect_accept.html")
    button = browser.find_element_by_class_name("trollface")
    button.click()
    new_window = browser.window_handles[2]
    browser.switch_to.window(new_window)
    x = browser.find_element_by_id("input_value")
    x = x.text
    x = int(x)
    field = browser.find_element_by_id("answer")
    field.send_keys(calc(x))
    button2 = browser.find_element_by_class_name("btn")
    button2.click()



finally:
    time.sleep(6)
    browser.quit()
