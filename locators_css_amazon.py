from selenium import webdriver
from selenium.webdriver.common.by import By
from faker import Faker
from time import sleep

# Start Chrome browser:
driver = webdriver.Chrome()

driver.get('https://www.amazon.com/')

# Amazon logo
driver.find_element(By.CSS_SELECTOR, 'i.a-icon.a-icon-logo')

# Create account
driver.find_element(By.CSS_SELECTOR, 'h1.a-spacing-small')

# Your name field
driver.find_element(By.ID, 'ap_customer_name')
driver.find_element(By.CSS_SELECTOR, '#ap_customer_name')

# Email field
driver.find_element(By.ID, 'ap_email')
driver.find_element(By.CSS_SELECTOR, '#ap_email')

# Password field
driver.find_element(By.ID, 'ap_password')
driver.find_element(By.CSS_SELECTOR, '#ap_password')

# Re-enter password field
driver.find_element(By.ID, 'ap_password_check')
driver.find_element(By.CSS_SELECTOR, '#ap_password_check')

# Continue button
driver.find_element(By.ID, 'continue')
driver.find_element(By.CSS_SELECTOR, '#continue')

# Conditions of Use
driver.find_element(By.XPATH, '//a[text()="Conditions of Use"]')

# Privacy Notice
driver.find_element(By.XPATH, '//a[text()="Privacy Notice"]')

# Sign In
driver.find_element(By.ID, 'ra-sign-in-link')
driver.find_element(By.CSS_SELECTOR, '#ra-signin-button')




