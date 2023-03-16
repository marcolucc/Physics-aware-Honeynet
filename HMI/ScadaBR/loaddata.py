from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from pprint import pprint
import json

from time import sleep

# setting chromedriver as headless to not fuck with us working!

driver_location = "/usr/bin/chromedriver"
binary_location = "/usr/bin/google-chrome"

options = webdriver.ChromeOptions()
options.binary_location = binary_location
options.add_argument('--headless')
options.add_argument("--log-level=3")
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(executable_path=driver_location, chrome_options=options)

# loading scada site   
driver.get("http://localhost:9090/ScadaBR")


# WE'RE IN!

user = driver.find_element_by_xpath('//*[@id="username"]')

user.click()
user.clear()
user.send_keys('admin')


password = driver.find_element_by_xpath('//*[@id="password"]')

password.click()
password.clear()
password.send_keys('admin')
   
button = driver.find_element_by_xpath('/html/body/div[1]/table/tbody/tr/td[1]/form/table/tbody/tr[3]/td[1]/input')
button.click()

sleep(1)


#Import page

import_page = driver.find_element_by_xpath('/html/body/table[2]/tbody/tr/td[1]/a[17]/img')

import_page.click()

sleep(1)


#Import Json

with open('dataHMI.txt', 'r') as jf:
   myjson = json.load(jf)

data = driver.find_element_by_xpath('//*[@id="emportData"]')
data.click()
data.clear()

data.send_keys(json.dumps(myjson))

button = driver.find_element_by_xpath('//*[@id="importJsonBtn"]')
button.click()

sleep(2)

datasource = driver.find_element_by_xpath('/html/body/table[2]/tbody/tr/td[1]/a[6]/img')
datasource.click()

active = driver.find_element_by_xpath('//*[@id="dsImg1"]')
active.click()

driver.close()
