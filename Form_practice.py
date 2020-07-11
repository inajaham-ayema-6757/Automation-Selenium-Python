from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

bdriver = webdriver.Chrome("D:\chromedriver_win32\chromedriver.exe")
bdriver.get("https://cosmocode.io/automation-practice/")
bdriver.maximize_window()
time.sleep(1)

bdriver.find_element_by_link_text("Click here to reload this page")
time.sleep(5)

bdriver.find_element_by_id("firstname").send_keys("MyFirstName")
time.sleep(1)

bdriver.find_element_by_class_name("lastname").send_keys("MyLastName")
time.sleep(1)

bdriver.find_element_by_xpath("//input[@value='Male']").click()
time.sleep(1)

bdriver.find_element_by_name("language_java").click()
time.sleep(1)

bdriver.find_element_by_name("language_python").click()
time.sleep(1)

bdriver.find_element_by_name("language_c").click()
time.sleep(1)

bdriver.find_element_by_name("age")
select_fr = Select(bdriver.find_element_by_name("age"))
select_fr.select_by_value("20 to 29")
time.sleep(1)

bdriver.find_element_by_id("submit_htmlform").click()
time.sleep(2)

bdriver.quit()