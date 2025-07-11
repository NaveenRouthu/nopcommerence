import pytest
from selenium import webdriver
from pageojectmodel.LoginPage import Loginpage
import time

from testcases.contest import setup


class Test_001_login:
    """locators values in class level"""
    baseURL="https://admin-demo.nopcommerce.com"
    username="admin@yourstore.com"
    password="admin"

    def test_homepagetittle(self,setup):
        self.driver=setup
        self.driver.get(self.baseURL)
        act_title=self.driver.title
        if act_title=="nopCommerce demo store. Login":
            assert True
            self.driver.close()

        else:
            self.driver.save_screenshot("../screenshots/homepage.png")
            self.driver.close()
            assert False


    def test_login(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp=Loginpage(self.driver)
        self.lp.setusername(self.username)
        self.lp.setpassword(self.password)
        self.lp.clikinglogin()
        time.sleep(10)
        act_title=self.driver.title
        if act_title=="Dashboard / nopCommerce administration25":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot("../screenshots/loginpage.png")
            self.driver.close()
            assert  False




