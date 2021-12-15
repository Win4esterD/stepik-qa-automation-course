from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(" http://suninjuly.github.io/selects1.html")
    n1 = browser.find_element_by_id("num1")
    num1 = n1.text
    n2 = browser.find_element_by_id("num2")
    num2 = n2.text
    value = int(num1) + int(num2)
    value = str(value)
    browser.find_element_by_css_selector(f"[value='{value}']").click()
    button = browser.find_element_by_class_name('btn')
    button.click()




finally:
    time.sleep(4)
    browser.quit()
