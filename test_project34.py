import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


class TestSum(unittest.TestCase):
    
    def setUp(self):

        self.driver = webdriver.Chrome()
        
    def test_list_link1(self):
        driver = self.driver
        link1 = "http://suninjuly.github.io/registration1.html"
        driver.get(link1)
        
        input1 = driver.find_element_by_css_selector('div.form-group.first_class > input')
        input1.send_keys("Ivan")
        input2 = driver.find_element_by_xpath("//input[@placeholder='Input your last name'][@type='text']")
        input2.send_keys("Petrov")
        input3 = driver.find_element_by_css_selector('div.form-group.third_class > input')
        input3.send_keys("email")
        button = driver.find_element_by_css_selector("button.btn")
        button.click()
        time.sleep(1)
        welcome_text_elt = driver.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!")
        
    def test_list_link2(self):
        driver = self.driver
        link2 = "http://suninjuly.github.io/registration2.html"
        driver.get(link2)
        

        input1 = driver.find_element_by_css_selector('div.form-group.first_class > input')
        input1.send_keys("Ivan")
        input2 = driver.find_element_by_xpath("//input[@placeholder='Input your last name'][@type='text']")
        input2.send_keys("Petrov")
        input3 = driver.find_element_by_css_selector('div.form-group.third_class > input')
        input3.send_keys("email")
        button = driver.find_element_by_css_selector("button.btn")
        button.click()
        time.sleep(1)
        welcome_text_elt = driver.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!")

if __name__ == '__main__':
    unittest.main()
