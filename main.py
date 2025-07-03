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
start_time = time()
end_time = start_time + 60 * 5
current_time = start_time

while current_time < end_time:
    cookie.click()

    # Purchase best upgrade every five seconds
    # (every five seconds determined by whether the elapsed number of seconds is a multiple of five).
    if round(current_time - start_time) % 5 == 0:
        # The project specification says: "purchase the most expensive [upgrade].
        # You'll need to check how much money (cookies) you have against the price of each upgrade."

        # But, from my observation of the game, this is not at all the best solution.
        # Upgrades are only unlocked once you have enough cookies to afford them,
        # so there's no need to compare the number of cookies to the prices
        # in order to determine which is the most expensive purchasable.
        # The most expensive purchasable is usually the last unlocked upgrade.
        # We can save a significant amount of processing time by just clicking the last unlocked upgrade.

        # Additionally, the most expensive purchasable might not be the most high-ROI upgrade.
        # For example, if you buy a lot of cursors, they can become more expensive than the grandma, and yet the grandma
        # has a higher-ROI in the sense that she increases your cookies per second more for fewer cookies.
        # So this is the second reason why it's best to just buy the last unlocked upgrade:
        # it always has the highest ROI.

        upgrades = cookie_monster.find_elements(By.CSS_SELECTOR, ".product.unlocked.enabled")
        if len(upgrades) > 0:
            upgrades[-1].click()

    # Refresh current time
    current_time = time()

cookies_per_second = float(cookie_monster.find_element(By.ID, "cookies").text.split("\n")[1].split(" ")[2])
print("Closing cookies per second: ", cookies_per_second)

cookie_monster.quit()