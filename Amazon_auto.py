from selenium import webdriver
import time

myuname = "Your_Username"
mypass = "Your_Password"
productname = "Product_To_Search"
bdriver = webdriver.Chrome("D:\chromedriver_win32\chromedriver.exe")
bdriver.get("https://www.amazon.in/")
bdriver.maximize_window()
time.sleep(1)

bdriver.find_element_by_partial_link_text("Account & Lists").click()
time.sleep(1)

bdriver.find_element_by_id("ap_email").send_keys(myuname)
bdriver.find_element_by_id("continue").click()
time.sleep(2)

bdriver.find_element_by_id("ap_password").send_keys(mypass)
bdriver.find_element_by_id("signInSubmit").click()
time.sleep(2)

bdriver.find_element_by_id("twotabsearchtextbox").send_keys(productname)
bdriver.find_element_by_class_name("nav-input").click()
time.sleep(2)

bdriver.find_element_by_link_text(productname).click()
time.sleep(10)

bdriver.switch_to.window(bdriver.window_handles[1])
time.sleep(2)

bdriver.find_element_by_id("add-to-wishlist-button-submit").click()
time.sleep(5)

bdriver.find_element_by_link_text("Continue shopping").click()
time.sleep(3)

bdriver.find_element_by_id("add-to-cart-button").click()
time.sleep(5)

bdriver.find_element_by_id("hlb-ptc-btn-native").click()
time.sleep(5)

bdriver.find_element_by_link_text("Deliver to this address").click()
time.sleep(7)

bdriver.find_element_by_class_name("a-button-text").click()
bdriver.quit()
