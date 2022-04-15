import time 
from selenium import webdriver

import math
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"

try:

    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id('treasure')
    x_treasure = x_element.get_attribute('valuex')
    x = x_treasure
    y = calc(x)

    input1 = browser.find_element_by_id('answer')
    input1.send_keys(y)

    option1 = browser.find_element_by_id('robotCheckbox')
    option1.click()

    option1 = browser.find_element_by_css_selector("[value='robots']")
    option1.click()
    
    button = browser.find_element_by_css_selector("button.btn")
    button.click()


finally:

    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
