import string
import random
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.common.exceptions import ElementNotInteractableException

driver = webdriver.Firefox()
driver.get("https://monkeytype.com")


def home_page():
    driver.find_element(By.XPATH, '//*[@id="logo"]').click()
    time.sleep(1)

def cookie_accept():
    time.sleep(3)
    cookie_btn = driver.find_element(By.XPATH, "/html/body/div[10]/dialog/div[2]/div[2]/div[2]/button[1]")
    welcome_btn = driver.find_element(By.XPATH, "/html/body/div[13]/div[2]/div[2]/div[2]/div[2]/button[1]")

    cookie_btn.click()
    time.sleep(1)
    welcome_btn.click()

def take_test(time_to_sleep):
    key_input = driver.find_element(By.XPATH, '//*[@id="wordsInput"]')

    i = 0
    try:
        while True:
            current_word = driver.find_element(By.CSS_SELECTOR, "#words > div.word.active").text

            for char in current_word:
                key_input.send_keys(char)

                variation = time_to_sleep * 0.8
                sleep_time = random.uniform(time_to_sleep - variation, time_to_sleep + variation)

                time.sleep(sleep_time)

            key_input.send_keys(" ")

            i += 1

    except ElementNotInteractableException:
        return


def select_test(type_index, mode_index):
    type_btn = driver.find_element(By.XPATH, f'/html/body/div[11]/main/div/div[1]/div/div[3]/button[{type_index}]')
    type_btn.click()
    time.sleep(.7)

    mode_btn = driver.find_element(By.XPATH, f'/html/body/div[11]/main/div/div[1]/div/div[{4 + type_index}]/button[{mode_index + 1 if type_index == 3 else mode_index}]')
    mode_btn.click()
    time.sleep(.9)

def access_account(email, password):
    profile_btn = driver.find_element(By.XPATH, "/html/body/div[11]/header/nav/a[5]")
    profile_btn.click()

    time.sleep(1)

    email_field = driver.find_element(By.XPATH, "/html/body/div[11]/main/div[2]/div[4]/form/input[1]")
    email_field.send_keys(email)

    password_field = driver.find_element(By.XPATH, "html/body/div[11]/main/div[2]/div[4]/form/input[2]")
    password_field.send_keys(password)

    login_btn = driver.find_element(By.XPATH, "html/body/div[11]/main/div[2]/div[4]/form/button")
    login_btn.click()
    time.sleep(3)