import requests
import re

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
import time

driver = webdriver.Chrome('.')

with open("linkedin_urls.txt", "r") as linkedin_urls:
    
    urls = linkedin_urls.read().splitlines()
    
    for url in urls[:2]:
        driver.get(url)
