from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com/")

import time

print("inicio")

time.sleep(60) # Sleep for 1000 seconds

print("3 segundos")

import smtplib 
   
my_email="jess_xxx@gmail.com"
password_key="xxxxx"

# SMTP Server and port no for GMAIL.com
gmail_server= "smtp.gmail.com"
gmail_port= 587


# Starting connection
my_server = smtplib.SMTP(gmail_server, gmail_port)
my_server.ehlo()
my_server.starttls()

# Login with your email and password
my_server.login(my_email, password_key)
