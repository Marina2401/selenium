from selenium import webdriver
driver = webdriver.Chrome("E:\Programms\chromedriver.exe")
driver.get("http://suninjuly.github.io/simple_form_find_task.html")

input1 = driver.find_element_by_tag_name("input")
input1.send_keys("Marina")
input2 = driver.find_element_by_name("last_name")
input2.send_keys("B")
input3 = driver.find_element_by_class_name("form-control.city")
input3.send_keys("City")
input4 = driver.find_element_by_id("country")
input4.send_keys("Russia")
button = driver.find_element_by_css_selector("button.btn")
button.click()



