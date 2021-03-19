from selenium import webdriver 
from selenium.webdriver.common.keys import Keys 
import time

email = "" #You can put your email and password info here to access to the site
password = ""

driver = webdriver.Firefox()
driver.get('https://www.amazon.com.tr/')#You can change the site if you want but this bot is made to shop from Amazon
time.sleep(2)

login_button = driver.find_element_by_xpath('/html/body/div[1]/header/div/div[3]/div[10]/div[2]/a/span')
login_button.click()

time.sleep(2)


login_input = driver.find_element_by_xpath('//*[@id="ap_email"]')
log_button = driver.find_element_by_xpath('//*[@id="continue"]')
login_input.send_keys(email)
time.sleep(2)
log_button.click()

password_input = driver.find_element_by_xpath('//*[@id="ap_password"]')
pas_button = driver.find_element_by_xpath('//*[@id="signInSubmit"]')
password_input.send_keys(password)
time.sleep(2)
pas_button.click()

search_bar = driver.find_element_by_xpath('//*[@id="twotabsearchtextbox"]')
search_img = driver.find_element_by_xpath('//*[@id="nav-search-submit-button"]')

product = input("Type what you want to buy: ")
time.sleep(10)

search_bar.send_keys(product)
search_img.click()

print("You have 20 seconds to set prices...")

time.sleep(20)

min_prc = int(input("min money you can give: "))
max_prc = int(input("max money you can give: "))

minprc_box = driver.find_element_by_xpath('//*[@id="low-price"]')
maxprc_box = driver.find_element_by_xpath('//*[@id="high-price"]')

minprc_box.send_keys(min_prc)
maxprc_box.send_keys(max_prc)


go_box = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div[2]/div/div[3]/span/div/span/div/div/div[5]/ul[1]/li[6]/span/form/span[3]/span/input')
go_box.click()