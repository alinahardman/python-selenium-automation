from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get('https://www.target.com/')
sleep(5)


# Click Account button
driver.find_element(By.ID, 'account-sign-in').click()
sleep(5)

# 3. Click SignIn btn from side navigation
driver.find_element(By.XPATH, "//button[@data-test='accountNav-signIn']").click()
sleep(5)

# 4. Verify SignIn page opened:
# “Sign in or create account” text is shown,
# actual_text = driver.find_element(By.XPATH, "//div[@data-test='lp-resultsCount']").text
actual_text = driver.find_element(By.XPATH, "//h1[contains(text(), 'Sign in or create account')]").text
expected_text = 'Sign in or create account'


assert expected_text in actual_text, f'Error. Expected text {expected_text}'
print('Test case passed')

driver.quit()
