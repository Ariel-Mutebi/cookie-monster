from time import time
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
cookie_monster = webdriver.Chrome() # Yes, a reference to the Sesame Street character.
cookie_monster.get("https://ozh.github.io/cookieclicker/")

# Dismiss the language pop-up.
sleep(1) # time for pop-up to load
me_speak_english = cookie_monster.find_element(By.ID, "langSelect-EN")
me_speak_english.click()

# Me want cookies!
cookie = cookie_monster.find_element(By.ID, "bigCookie")

# Yum yum yum yum yum!
stop_time = time() + 60 * 5
while time() < stop_time:
    cookie.click()

# cookie_monster.quit()