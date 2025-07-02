from math import floor
from time import time, sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
cookie_monster = webdriver.Chrome() # Yes, a reference to the Sesame Street character.
cookie_monster.get("https://ozh.github.io/cookieclicker/")

# Dismiss the language pop-up.
sleep(2) # time for pop-up to load
me_speak_english = cookie_monster.find_element(By.ID, "langSelect-EN")
me_speak_english.click()

# Dismiss the cookie banner because it intercepts clicks to product divs.
me_know_you_use_cookies = cookie_monster.find_element(By.CLASS_NAME, "cc_btn")
me_know_you_use_cookies.click()

# Me want cookies!
cookie = cookie_monster.find_element(By.ID, "bigCookie")

# Yum yum yum yum yum!
five_minutes = time() + 60 * 5
cookies_per_second = 0

while time() < five_minutes:
    cookie.click()
    # Purchase the most expensive upgrade possible every five seconds.
    if floor(five_minutes - time()) % 5 == 0:
        cookies_raw_text = cookie_monster.find_element(By.ID, "cookies").text
        number_of_cookies = int(cookies_raw_text.split("\n")[0].split(" ")[0])
        cookies_per_second = float(cookies_raw_text.split("\n")[1].split(" ")[2])

        buy_buttons = cookie_monster.find_elements(By.CSS_SELECTOR, ".product.unlocked.enabled")

        price_elements = cookie_monster.find_elements(By.CSS_SELECTOR, ".product.unlocked.enabled .price")
        prices_ascending = [int(price_element.text.replace(",", "")) for price_element in price_elements]
        prices_descending = prices_ascending[::-1]

        for i in range(len(prices_descending)):
            if number_of_cookies > prices_descending[i]:
                buy_button = buy_buttons[i]
                buy_button.click()
                break

print(cookies_per_second)
cookie_monster.quit()