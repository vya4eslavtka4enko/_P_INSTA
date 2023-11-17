from selenium import webdriver
import time
from selenium.webdriver.common.by import By
CHROME_DRIVER_PATH = '/Applications/Google Chrome.app'
SIMILAR_ACCOUNT = ''
USER_NAME = ''
USER_PASS = ""

class InstaFollower():
    def __init__(self):
        chrome_option = webdriver.ChromeOptions()
        chrome_option.add_experimental_option('detach', True)
        self.driver = webdriver.Chrome(options=chrome_option)

    def login(self):
        self.driver.get('https://www.instagram.com')
        time.sleep(3)
        self.button_accept = self.driver.find_element(By.XPATH,'/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[1]')
        self.button_accept.click()
        self.input_name = self.driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[1]/div/label/input')
        self.input_name.send_keys('tkachenko.vyacheslav.2@gmail.com')
        self.input_last_name = self.driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[2]/div/label/input')
        self.input_last_name.send_keys(USER_PASS)
        time.sleep(4)
        self.input_login = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')
        self.input_login.click()
        time.sleep(3)
        self.save_info = self.driver.find_element(By.CSS_SELECTOR, '._ac8f')
        self.save_info.click()
        time.sleep(2)
        self.save_notification = self.driver.find_element(By.CSS_SELECTOR, '._a9-- _ap36 _a9_1')
        self.save_notification.click()



    def find_followers(self):
        self.button_following = self.driver.find_element(By.CLASS_NAME,'.x1i10hfl')
        self.button_following.click()
        time.sleep(5)

    def follow(self):
        pass



insta_follower = InstaFollower()
insta_follower.login()
insta_follower.find_followers()
# insta_follower.follow()