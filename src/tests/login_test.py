from selenium import webdriver

from src.pom.Login import Login

import pytest


def test_login():
    driver = webdriver.Chrome("/Users/vijay/Downloads/chromedriver_2")
    url= "https://dsportalapp.herokuapp.com/login"
    driver.get(url)
    l = Login(driver)
    l.login("dsalgo645","Password@12")
    driver.implicitly_wait(2)
    actual_url = driver.current_url

    assert actual_url == "https://dsportalapp.herokuapp.com/home"

    

