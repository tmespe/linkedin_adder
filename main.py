import os
import time

from dotenv import load_dotenv
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException

load_dotenv()

driver = webdriver.Firefox()

LOGIN_URL = "https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin"

user_name = os.getenv("USER_NAME")
password = os.getenv("PASSWORD")


def sign_in(user_name=user_name, password=password):
    """
    Logs in to linkedin with username and password from arguments using selenium
    :param user_name: Linkedin username
    :param password: Linkedin password
    :return: None
    """
    driver.get(LOGIN_URL)

    username_field = driver.find_element_by_xpath('//*[@id="username"]')
    username_field.send_keys(user_name)

    password_field = driver.find_element_by_xpath('//*[@id="password"]')
    password_field.send_keys(password)

    sign_in_button = driver.find_element_by_xpath('/html/body/div/main/div[3]/div[1]/form/div[3]/button')
    sign_in_button.click()


def connect():
    """
    Opens a linkedin page using selenium and checks if connect button is clickable. If the button is clickable an
    invitation to connect is sent. If the button is not present and clickable prints message that person is most likely
    added.
    :return: None
    """
    name_xpath = "/html/body/div[7]/div[3]/div/div/div/div/div[3]/div/div/main/div/section[1]/div[2]/div[2]/div/div[1]/h1"
    try:
        # Set Xpath paths for name, connect button and send button pop-up
        name = driver.find_element_by_xpath(name_xpath)
        connect_xpath = '//*[@data-control-name="connect"]'
        send_xpath = "/html/body/div[3]/div/div/div[3]/button[2]/span"

        # Waits for page to load
        connect_button = driver.find_element_by_xpath(connect_xpath)
        time.sleep(1)
        connect_button.click()

        time.sleep(1)
        send_button = driver.find_element_by_xpath(send_xpath)
        send_button.click()
        print(f"Successfully connected with {name.text}")

    except (NoSuchElementException, ElementClickInterceptedException) as e:
        name = driver.find_element_by_xpath(name_xpath)
        print(f"{name.text} is probably already added or error occurred. See following debug {e}")


def main():
    with open("linkedin_urls.txt", "r") as linkedin_urls:
        urls = linkedin_urls.read().splitlines()

        sign_in()

        for url in urls:
            driver.get(url)
            connect()
            time.sleep(1)


main()
