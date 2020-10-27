from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome("E:\Programms\chromedriver.exe")
driver.get("https://www.labirint.ru/books/")

a = driver.find_element_by_css_selector("div.swiper-container-actions.action-block-desktop.swiper-container-initialized.swiper-container-horizontal.swiper-container-free-mode")
books = a.find_elements_by_class_name("card-column")
button = books[3].find_element_by_class_name("btn-primary")
button.click()

basket = driver.find_element_by_class_name("b-header-b-personal-e-icon-count-m-cart.basket-in-cart-a")
print(basket.text)