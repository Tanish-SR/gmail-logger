from tkinter import Button
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from getpass import getpass

print ("Please enter your Email")
username = input(str())
print ("Enter your password")
password = input(str)

browser = webdriver.Chrome("./chromedriver")
browser.get("https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin")

try: 
    writeusername = browser.find_element_by_xpath()
    writeusername.send_keys(username)

    nextbutton = browser.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/div[1]")
    nextbutton.click()

    writepass = browser.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input")
    writepass.send_keys()

    nextbutton = browser.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/div[3]")
    nextbutton.click()

    print("logged in ....")
except:
    print("Something went wrong \n try again later")