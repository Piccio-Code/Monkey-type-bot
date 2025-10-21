import time
from warnings import catch_warnings

from selenium import webdriver
from selenium.webdriver.common.by import By

def cookie_accept(driver):
    time.sleep(3)
    cookie_btn = driver.find_element(By.XPATH, "/html/body/div[10]/dialog/div[2]/div[2]/div[2]/button[1]")
    welcome_btn = driver.find_element(By.XPATH, "/html/body/div[13]/div[2]/div[2]/div[2]/div[2]/button[1]")

    cookie_btn.click()
    time.sleep(1)
    welcome_btn.click()

driver = webdriver.Firefox()
driver.get("https://monkeytype.com")

cookie_accept(driver)

key_input = driver.find_element(By.XPATH, '//*[@id="wordsInput"]')

i = 0

while True:
    time_div = driver.find_element(By.XPATH, '//*[@id="liveStatsMini"]/div[1]')
    if time_div.text == "1":
        break

    current_word = driver.find_element(By.CSS_SELECTOR, "#words > div.word.active").text


    for char in current_word:
        key_input.send_keys(char)
        time.sleep(0.001)

    key_input.send_keys(" ")

    i += 1

time.sleep(10)

driver.close()