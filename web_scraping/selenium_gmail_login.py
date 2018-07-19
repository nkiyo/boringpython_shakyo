#! python3
# -*- encoding: utf-8 -*-

import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

if len(sys.argv) != 3:
    print('input two args. id and password.')
    sys.exit(1)

# ログインに使うID、パスワードはコマンドライン引数から受け取る
id = sys.argv[1]
passwd = sys.argv[2]

browser = webdriver.Chrome()

# アカウント入力画面
browser.get('http://www.google.com/gmail')
id_field = browser.find_element_by_id('identifierId')
id_field.send_keys(id)
next_button = browser.find_element_by_xpath("//span[contains(text(), 'Next')]")
next_button.click()

# パスワード入力画面
try:
    passwd_field = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@name='password']"))
    )
finally:
    print('wait failed.')
    sys.exit(1)
passwd_field.send_keys(passwd)
next_button = browser.find_element_by_xpath("//span[contains(text(), 'Next')]")
next_button.click()


