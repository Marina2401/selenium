from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#import time
import unittest

#class Googletest(unittest.TestCase):
    #def test_search(self):
driver = webdriver.Chrome("E:\Programms\chromedriver.exe")
driver.get("https://www.google.com/")

input1 = driver.find_element_by_name("q")
input1.send_keys("python")
input1.send_keys(Keys.ENTER)
#time.sleep(3)
titles = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "g"))
    )
#titles = driver.find_elements_by_class_name("g")
for title in titles:
    if "python" not in title.text.lower():
        print('No')

driver.close()
    #self.assertIn("python", title.text.lower())




