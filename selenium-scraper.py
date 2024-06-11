from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import datetime
import csv
from webScrapingApp.userInteractiveApp.functions import extract_number, shorten_title


driver = webdriver.Firefox()


'https://www.razer.com/gb-en/hard-bundles/Cobra-Pro-Mouse-Dock-Pro/RZHB-230629-02'
'https://www.razer.com/gb-en/gaming-keyboards/Razer-BlackWidow-V4-Pro/RZ03-04680300-R3W1'


website_list = [
    'https://www.google.com/search?q=iphone+15&sca_esv=339235e9794c2830&udm=3&biw=1366&bih=641&ei=JkL0ZabhOZi5hbIP9uuekAs&oq=iphone&gs_lp=Egxnd3Mtd2l6LXNlcnAiBmlwaG9uZSoCCAAyChAAGEcY1gQYsAMyChAAGEcY1gQYsAMyChAAGEcY1gQYsAMyChAAGEcY1gQYsAMyChAAGEcY1gQYsAMyChAAGEcY1gQYsAMyChAAGEcY1gQYsAMyChAAGEcY1gQYsANI3hVQAFgAcAF4AZABAJgBAKABAKoBALgBAcgBAJgCAaACCJgDAIgGAZAGCJIHATGgBwA&sclient=gws-wiz-serp'

    #     'https://www.amazon.co.uk/dp/B0CDHNJ22G/ref=twister_B0CC8RN3YR?_encoding=UTF8&psc=1'
    #     'https://www.amazon.co.uk/Razer-BlackWidow-Green-Switch-Multi-Function/dp/B0BSXRPJJC/ref=sr_1_2_sspa?crid=1KK071MBGMTXV&dib=eyJ2IjoiMSJ9.dJkV7z2sZHVa2W0fLtryQqjQIveMakjhJYzZdj2tykB_BLQIBagGTOAq7VZysxmM0hbzLGokgntkjuVJ-SXfsyv-XQftgQBtU6igISrP3V6V8nm0UuZkD1uQYWxjJNN_Os6EvStBySVSzlf-ZAAoqBj0FsMoZeTS3sPILG0dUj5xjmmmzeafB1KDtk-wv7xfLFOggb-yDsHkpBvIP03AxAhTnCszvxiNskXgr6xDnGU.CBUf5guU7v647H3AJvaYqbEv4tc1WXn3YYK3Tsq4Iyk&dib_tag=se&keywords=razer+keyboard&qid=1710506086&sprefix=razer%2Caps%2C68&sr=8-2-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1'
]


def check_prices():
    # Keep record of iterations so we know which URL wasn't extracted correctly
    i = 0

    for webpage in website_list:
        for element in container:

        i = i + 1
        driver.get(webpage)
        driver.implicitly_wait(30)

        rejected_cookies = False
        if not rejected_cookies:
            try:
                # wait for the webpage to load, then close the cookies window
                reject_cookies = driver.find_element(
                    By.XPATH, '//button[@id="W0wltc"]')
                reject_cookies.click()
                rejected_cookies = True
            except:
                print('failed to click reject cookies')

        try:
            # extract title
            title = driver.find_element(
                By.XPATH, '//span[@class="pymv4e"]').text
            print(title)

            shortened_title = shorten_title(title)
            print(shortened_title)
            # extract the price and format
            price = driver.find_element(
                By.XPATH, '//span[@class="e10twf ONTJqd"]').text
            print(price)

            # find and extract stock
            original_price = driver.find_element(
                By.XPATH, '//span@[class="hdYIY"]').text
            print(original_price)

            discount = int(original_price) - int(price)
            print(discount)

            date = datetime.date.today()

            header = ["Title", "Price", "Discount", "Date"]
            data = [shortened_title, price, discount, date]

            with open("google-scraper.csv", "W", newline="", encoding="UTF-8") as f:
                writer = csv.writer(f)
                writer.writerow(header)
                writer.writerow(data)

        except:
            print(
                f'Issue with iteration {i} of check prices')

    driver.close()


while (True):
    check_prices()
    break
    time.sleep(86400)
