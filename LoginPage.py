import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Initialize WebDriver
driver = webdriver.Chrome()

# Open the application
driver.get("https://myalice-automation-test.netlify.app")
time.sleep(5)
driver.maximize_window()


# Enter login credentials
username = driver.find_element(By.ID, "username")
password = driver.find_element(By.ID, "password")
username.send_keys("testuser")
password.send_keys("password")
# Click the Login button
login_button = driver.find_element(By.ID, "login-btn")
login_button.click()
time.sleep(3)


# Locate the Search button using its class name
search_button = driver.find_element(By.CLASS_NAME, "bg-green-500")
# Verify that the Search button is displayed
assert search_button.is_displayed()

# Close the browser
driver.quit()
