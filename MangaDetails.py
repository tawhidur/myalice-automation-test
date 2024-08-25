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


# Click on the Details link for a manga card
details_link = driver.find_element(By.CLASS_NAME, "text-blue-500")
# Click the "Details" link
details_link.click()
time.sleep(3)

# Locate the image within the modal
manga_image = driver.find_element(By.XPATH, "//img[@alt='Attack on Titan']")

# Verify that the modal containing the image is displayed
assert manga_image.is_displayed()

# Verify the image source URL
expected_src = "https://res.cloudinary.com/emerging-it/image/upload/v1724240584/mangaImage/lyj3i7qwtp3f2qz59so1.jpg"
assert manga_image.get_attribute("src") == expected_src

# Verify the alt text of the image
assert manga_image.get_attribute("alt") == "Attack on Titan"
time.sleep(3)

# Close the modal
close_button = driver.find_element(By.CLASS_NAME, "bg-blue-500")
close_button.click()

# Close the browser
driver.quit()
