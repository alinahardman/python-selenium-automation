from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()

driver.get('https://www.amazon.com/')
sleep(10)

# Sign In page
driver.find_element(By.ID, 'nav-link-accountList').click()

# Amazon logo
driver.find_element(By.XPATH, '//i[@class="a-icon a-icon-logo]')

#Email field
driver.find_element(By.ID, 'ap_email_login').send_keys('<EMAIL>')

# Continue button
driver.find_element(By.XPATH, '//input[@type="submit"]').click()

# Forgot your password link
driver.find_element(By.ID, 'auth-fpp-link-bottom')

# Conditions of use link
drive.find_element(By.XPATH, '//a[text()="Conditions of Use"]')

# Privacy Notice link
drive.find_element(By.XPATH, '//a[text()="Privacy Notice"]')

# Need help link
drive.find_element(By.XPATH, '//a[@role="button"]')


# Other issues with Sign-In link
# Couldn't find this option, maybe the UI changed?


# Create your Amazon account button
driver.find_element(By.XPATH, '//input[@class="a-button-input"]')




