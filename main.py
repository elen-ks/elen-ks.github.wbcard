from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from config import *
import time

options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get(SEARCH_URL)
time.sleep(2)

for _ in range(SCROLL_COUNT):
    driver.execute_script("window.scrollBy(0, 1200)")
    time.sleep(1)

cards = driver.find_elements(By.XPATH, "//article[@data-nm-id]")

for card in cards:
    if card.get_attribute("data-nm-id") == NEEDED_ID:
        link = card.find_element(By.XPATH, ".//a").get_attribute("href")
        driver.get(link)
        break

time.sleep(2)
driver.quit()
