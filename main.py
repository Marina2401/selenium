
from selenium import webdriver
driver = webdriver.Chrome("E:\Programms\chromedriver.exe")
driver.get("https://www.avito.ru/rossiya/hobbi_i_otdyh")

items = driver.find_elements_by_class_name("item_table")
for item in items:
    print(item.text)

