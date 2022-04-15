import time 
from selenium import webdriver
from selenium.webdriver.support.ui import Select

import math


link = "http://suninjuly.github.io/selects1.html"

try:

    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element_by_id('num1')

    x2 = x.text
    
    y = browser.find_element_by_id('num2')

    y2 = y.text

    sum_xy = int(x2)+int(y2)

    

    browser.find_element_by_tag_name("select").click()

    browser.find_element_by_css_selector(f"[value='{sum_xy}']").click()


    
    button = browser.find_element_by_css_selector("button.btn")
    button.click()


finally:

    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
