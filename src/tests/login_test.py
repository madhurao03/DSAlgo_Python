from selenium import webdriver

from src.pom.Login import Login
import pandas as pd

import pytest


def get_credentials():
    df = pd.read_excel("/Users/vijay/github_madhu/DSAlgo_Python/src/data/DSAlgo_Login_data.xlsx")
    return list(df.to_records())

@pytest.mark.parametrize("_,username,password",get_credentials())
def test_login(_,username,password):
    driver = webdriver.Chrome("/Users/vijay/Downloads/chromedriver_2")
    url= "https://dsportalapp.herokuapp.com/login"
    driver.get(url)
    l = Login(driver)
    l.login(username, password)
    driver.implicitly_wait(2)
    actual_url = driver.current_url

    assert actual_url == "https://dsportalapp.herokuapp.com/home"
    
    

