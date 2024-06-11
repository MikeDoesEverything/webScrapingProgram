from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import datetime
import csv
from .functions import extract_number, shorten_title
# from webScrapingApp.userInteractiveApp.models import amazonScraper


def run_web_scraper(url):

    driver = webdriver.Firefox()

    website_list = [
        url,
        'https://www.amazon.co.uk/dp/B0CDHNJ22G/ref=twister_B0CC8RN3YR?_encoding=UTF8&psc=1',
    ]

    def check_prices():
        # Keep record of iterations so we know which URL wasn't extracted correctly
        i = 0

        for webpage in website_list:
            driver.implicitly_wait(30)
            i = i + 1

            try:
                driver.get(webpage)
            except:
                print('failed to retrieve webpage')

            data = []
            date = datetime.date.today()
            shortened_title, full_price, stock_number = None, None, None
            web_scaper_error = False

            rejected_cookies = False
            if not rejected_cookies:
                try:
                    # wait for the webpage to load, then close the cookies window
                    reject_cookies = driver.find_element(
                        By.XPATH, '//button[@id="sp-cc-rejectall-link"]')
                    reject_cookies.click()
                    rejected_cookies = True
                except:
                    print('failed to click reject cookies')

            try:
                # extract title
                title = driver.find_element(
                    By.XPATH, '//span[@id="productTitle"]').text
                print(title)

                shortened_title = shorten_title(title)
                print(shortened_title)

                # extract the price and format
                price_whole = driver.find_element(
                    By.XPATH, '//span[@class="a-price-whole"]').text
                price_fraction = driver.find_element(
                    By.XPATH, '//span[@class="a-price-fraction"]').text

                full_price = f"£{price_whole}.{price_fraction}"
                print(full_price)

                # find and extract stock
                stock_button = driver.find_element(
                    By.CSS_SELECTOR, '.a-touch-link')
                stock_button.click()

                stock = driver.find_element(
                    By.XPATH, '//span[@id="aod-filter-offer-count-string"]').text
                print(stock)

                stock_number = extract_number(stock)
                print(stock_number)

            except Exception as e:
                error_message_scraper = f'Issue with iteration {i} of web scraping'
                print(error_message_scraper)
                print(str(e))
                web_scaper_error = True

            try:
                header = ["Title", "Price", "Stock", "Date", "Errors"]
                data = [shortened_title, full_price, stock_number, date]

                if web_scaper_error:
                    data.append(str(error_message_scraper))

                with open("amazon-web-scraper.csv", "a+", newline="", encoding="UTF-8") as f:
                    writer = csv.writer(f)
                    # writer.writerow(header)
                    writer.writerow(data)

            except Exception as e:
                error_message_write_csv = f'failed to save scraped data to csv in iteration {i}'
                print(error_message_write_csv)
                print(str(e))

        driver.close()

    while (True):
        check_prices()
        break
        time.sleep(86400)


if __name__ == '__main__':
    run_web_scraper()
