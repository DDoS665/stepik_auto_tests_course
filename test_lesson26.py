import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


# Функция ожидания элементов
def wait_of_element_located(xpath, driver_init):
    element = WebDriverWait(driver_init, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, xpath)
        )
    )
    return element

# Вынесем инициализцию драйвера в отдельную фикстуру pytest
def driver_init():
    driver = webdriver.ChromeOptions()
    driver.get("https://www.duckduckgo.com")
    yield driver
    driver.close()
    
def test_basic_duckduckgo_search(browser):
    PHRASE = 'panda'
    URL = 'https://www.duckduckgo.com'
    driver.get(URL)
    search_input = driver.find_element_by_id('search_form_input_homepage')
    search_input.send_keys(PHRASE + Keys.RETURN)
