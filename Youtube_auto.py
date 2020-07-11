from selenium import webdriver
import time

bdriver = webdriver.Chrome("D:\chromedriver_win32\chromedriver.exe")
bdriver.get("https://www.youtube.com/")
bdriver.maximize_window()
time.sleep(3)

bdriver.find_element_by_xpath("/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div/div[1]/input").send_keys("How to Work From Home as a Team")
time.sleep(2)

bdriver.find_element_by_xpath("/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/button").click()
time.sleep(2)

bdriver.find_element_by_link_text("How to Work From Home as a Team").click()
time.sleep(20)

bdriver.quit()