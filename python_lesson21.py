
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))



browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))

btn = browser.find_element_by_id('book')

btn.click()

option = browser.find_element_by_id("solve")
browser.execute_script("return arguments[0].scrollIntoView(true);", option)

x_element = browser.find_element_by_id("input_value")
x = x_element.text
y = calc(x)

input1 = browser.find_element_by_id("answer")
input1.send_keys(y)


btn2 = browser.find_element_by_id("solve")

btn2.click()


