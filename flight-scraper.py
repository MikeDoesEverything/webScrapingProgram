from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd

driver = webdriver.Firefox()
website = "https://www.expedia.co.uk/"
driver.get(website)

driver.implicitly_wait(15)

try:
    reject_cookies = driver.find_element(By.ID,
                                         "onetrust-reject-all-handler")
    reject_cookies.click()
    print("Clicked on reject cookies button")

except NoSuchElementException:
    print("Reject cookies button not found")

driver.implicitly_wait(25)

try:
    flights_button = driver.find_element(By.XPATH, '//span[text()="Flights"]')
    flights_button.click()
    print('flights button clicked')

    departure_button = driver.find_element(By.XPATH,
                                           '//button[@aria-label="Leaving from"]')
    departure_button.click()
    print('departure button clicked')

    driver.implicitly_wait(35)
    departure_input = driver.find_element(
        By.ID, 'origin_select')
    departure_input.send_keys('london')
    departure_input.send_keys(Keys.RETURN)

except NoSuchElementException:
    print("Failed to find departure destination")

driver.implicitly_wait(45)

try:
    going_to_button = driver.find_element(
        By.XPATH, '//button[@aria-label="Going to"]')
    going_to_button.click()
    print("going to button clicked")

    going_to_input = driver.find_element(By.ID, 'destination_select')
    going_to_input.send_keys('TFS')
    going_to_input.send_keys(Keys.RETURN)


except:
    print("failed to search going to")

driver.implicitly_wait(55)

try:
    dates_button = driver.find_element(
        By.XPATH, '//button[@data-testid="uitk-date-selector-input1-default" ]')
    dates_button.click()
    print("dates button clicked")
    date = driver.find_element(By.XPATH, '//div[@tab-index="0"]')
    date.click()

except:
    print("failed to select date")

# departure_destination = input('Pick your destination')
# print("Destination Chosen")

# for vid in videos:
#     title_element = vid.find_element(
#         By.CSS_SELECTOR, 'yt-formatted-string.style-scope.ytd-video-renderer')
#     title = title_element.text
#     print(title)
# # driver.quit()
