from selenium.webdriver.common.by import By

class Login():
    def __init__(self, driver):
        self.driver = driver
        self.username_field = driver.find_element(By.XPATH,"//input[@name= 'username']")
        self.password_field = driver.find_element(By.XPATH,"//input[@name= 'password']")
        self.loginbutton = driver.find_element(By.XPATH,"//input[@type= 'submit']")

    def login(self,username, password):
        self.username_field.send_keys(username)
        self.password_field.send_keys(password)
        self.loginbutton.click()
        




