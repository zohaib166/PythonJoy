# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 15:15:54 2024

@author: hasan
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)


# =============================================================================
# driver.get("https://www.selenium.dev/")
# downloads_link = driver.find_element(By.LINK_TEXT, "Downloads")
# downloads_link.click()
# 
# driver.get("https://www.google.com")
# search = driver.find_element(By.CLASS_NAME,"gLFyf")
# search.send_keys("Tripti Dimri")
# search.send_keys(Keys.ENTER)
# =============================================================================

driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver,600)
target = '"Nilofar"'
string = "I Love you, kachooo"

x_arg = '//span[contains(@title,'+target+')]'
target = wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))
target.click()

input_box = driver.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div[1]/div/div[1]')

for i in range(20):
    input_box.send_keys(string+ Keys.ENTER)
    

