from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from time import sleep

path = "D:/coding/python/test_7/driver/chromedriver.exe"

service = Service(path)
browser = webdriver.Chrome(service = service)

num = input("enter a whatsapp number without 0 at first and with country code")

browser.get(f"https://web.whatsapp.com/send/?phone={num}&text&type=phone_number&app_absent=0")
input("enter to run the code: ")

msg_box = browser.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div[1]/div[2]/div[1]/p')
msg_box.send_keys("hello")
sleep(0.05)
btn = browser.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div[2]/button')
btn.click()

input("enter to quit: ")