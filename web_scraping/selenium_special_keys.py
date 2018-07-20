#! python3
# -*- encoding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.get('http://nostarch.com')
htmlElem = browser.find_element_by_tag_name('html')
htmlElem.send_keys(Keys.END)
#htmlElem.send_keys(Keys.HOME)

browser.refresh()

