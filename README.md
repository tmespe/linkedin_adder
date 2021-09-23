# Linkedin adder
Adds connections on Linkedin based from a list of linkeding profile URLs.

Starting a new graduate program I was faced with adding a lot of people on Linkedin. This script automates connecting with people using selenium. 

# Requirements
* Python 3.8 or higher
* Selenium
* Geckodriver, chromedriver og another Selenium compatible webdriver
* Requests
* Python-dotenv

# Instructions 
In order to run the script you need to have Python 3.8 or higher installed. You'll also need to have a webdriver installed (chromedriver, geckodriver etc.) and added to PATH. Optionally you can set the PATH manually as an argument for driver on line #10. 

You'll also need to have a "linkedin_urls.txt" file with one url per line.  

The script will look for your linkedin username and password in .env. You could also modify line 70 to add your username and password as parameters. 
