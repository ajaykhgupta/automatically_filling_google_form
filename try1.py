# name = quantumWizTextinputPaperinputInput
# comment  = quantumWizTextinputPapertextareaInput

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome('/usr/local/bin/chromedriver')
driver.get('https://docs.google.com/forms/u/0/d/e/1FAIpQLSf4y_5irOTMPCywwYbjbWzRqaDZwozSthrErdkkdcLG2QPzog/formResponse')



for i in range(1,101):
    # print("hello")
    time.sleep(1)
    name = driver.find_element_by_class_name('quantumWizTextinputPaperinputInput')
    name.send_keys('Ajay ')
    comment = driver.find_element_by_class_name('quantumWizTextinputPapertextareaInput')
    comment.send_keys('Response no.: ', i)
    submit_btn = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span/span')
    submit_btn.click()
    submit_another = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    submit_another.click()
    

driver.close()