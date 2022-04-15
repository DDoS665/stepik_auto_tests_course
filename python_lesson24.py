from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


# Функция ожидания элементов
def wait_of_element_located(xpath, driver):
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, xpath)
        )
    )
    return element


def test_add_jacket_to_the_shopcart():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.saucedemo.com/")

    # Поиск и ожидание элементов и присваивание к переменным.
    input_username = wait_of_element_located(xpath='//*[@id=\"user-name\"]', driver=driver)
    input_password = wait_of_element_located(xpath='//*[@id=\"password\"]', driver=driver)
    login_button = wait_of_element_located(xpath='//*[@id=\"login-button\"]', driver=driver)

    # Действия с формами
    input_username.send_keys("standard_user")
    input_password.send_keys("secret_sauce")
    login_button.send_keys(Keys.RETURN)

    # Поиск и ождиание прогрузки ссылки элемента товара магазина и клик по ссылке
    item_name = wait_of_element_located(xpath='//*[@id=\"item_5_title_link\"]/div', driver=driver)
    item_name.click()

    # Поиск и ожидание кнопки добавления товара и клик по этой кнопке
    item_add_button = wait_of_element_located(xpath='//*[@id=\"add-to-cart-sauce-labs-fleece-jacket\"]', driver=driver)
    item_add_button.click()

    # Ждем пока товар добавится в корзину, появится span(кол-во позиций в корзине) и кликаем по корзине чтобы перейти
    wait_of_element_located(xpath='//*[@id=\"shopping_cart_container\"]/a/span', driver=driver).click()

    # Еще один поиск ссылки элемента позиции магазина
    item_name = wait_of_element_located(xpath='//*[@id=\"item_5_title_link\"]/div', driver=driver)

    item_description = wait_of_element_located(
        xpath='//*[@id=\"cart_contents_container\"]/div/div[1]/div[3]/div[2]/div[1]',
        driver=driver
    )

    assert item_name.text == "Sauce Labs Fleece Jacket"
    assert item_description.text == "It's not every day that you come across a midweight quarter-zip fleece jacket capable of handling everything from a relaxing day outdoors to a busy day at the office."

   # Делаем скриншот результата

    driver.save_screenshot('eyetest.png')


    driver.close()


if __name__ == '__main__':
    test_add_jacket_to_the_shopcart()
