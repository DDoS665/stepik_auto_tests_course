from selenium import webdriver
import time
import os

try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    
    input1 = browser.find_element_by_xpath("//input[@placeholder='Enter first name'][@type='text']")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_xpath("//input[@placeholder='Enter last name'][@type='text']")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_xpath("//input[@placeholder='Enter email'][@type='text']")
    input3.send_keys("email")


    button1 = browser.find_element_by_id('file')
    

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "file.txt"
    file_path = os.path.join(current_dir, file_name)
    button1.send_keys(file_path)



    button2 = browser.find_element_by_xpath('//button[text()="Submit"]')
    button2.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

