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


# Function to search and verify results
def search_manga_and_verify(search_term, expected_result):
    search_box = driver.find_element(By.ID, "manga-search")
    search_box.clear()
    search_box.send_keys(search_term)
    search_box.send_keys(Keys.RETURN)

    # Verify that the correct results are displayed
    results = driver.find_elements(By.CLASS_NAME, "manga-card")
    for result in results:
        assert expected_result in result.text


# Search for "Naruto"
search_manga_and_verify("Naruto", "Naruto")

# Search for "One Piece"
search_manga_and_verify("One Piece", "One Piece")

# Search for "Seven Deadly Sins"
search_manga_and_verify("Seven Deadly Sins", "Seven Deadly Sins")

# Search for a term that returns no results
search_manga_and_verify("No manga found", "No manga found")
time.sleep(5)

# Close the browser
driver.quit()
