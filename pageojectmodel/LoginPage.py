from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By

class Loginpage:
    """class level varibles for locators"""
    textbox_username_ID="Email"
    textbox_password_ID="Password"
    button_login_XPATH="//button[normalize-space()='Log in']"
    link_logout_XPATH="//a[contains(.,'Logout')]"


    def __init__(self,driver):
        self.driver=driver

    def setusername(self,username):
        self.driver.find_element(By.ID,self.textbox_username_ID).clear()
        self.driver.find_element(By.ID, self.textbox_username_ID).send_keys(username)

    def setpassword(self,password):
        self.driver.find_element(By.ID, self.textbox_password_ID).clear()
        self.driver.find_element(By.ID, self.textbox_password_ID).send_keys(password)

    def clikinglogin(self):
        self.driver.find_element(By.XPATH, self.button_login_XPATH).click()

    def clikinglogout(self):
        self.driver.find_element(By.XPATH,self.link_logout_XPATH).click()









