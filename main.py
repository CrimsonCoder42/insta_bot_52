from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import time
import os

load_dotenv()

# instagram info from .env file
INSTA_EMAIL = os.getenv("INSTA_EMAIL")
INSTA_PASSWORD = os.getenv("INSTA_PASSWORD")
INSTA_URL = 'https://www.instagram.com/'

similar_account = 'techburner'
WINDOW_TIME = 60 * 60
start_time = time.time()

# Create a class called InstaFollower

class InstaFollower:
    # In the init() method, create the Selenium driver.
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.actions = {
            "find_click_xpath": lambda x: self.driver.find_element(By.XPATH, x).click(),
            "find_write_xpath": lambda x, text: self.driver.find_element(By.XPATH, x).send_keys(text),
            "find_text_xpath": lambda x: self.driver.find_element(By.XPATH, x).text
        }

    # safeguard against errors when running the code
    def handle_exceptions(self, action, *args):
        try:
            result = self.actions[action](*args)
            return result if result is not None else True
        except Exception as e:
            print(f"Exception: {e}")
            return False

    # Create three methods - login() and find_followers() and follow().
    def login(self):
        # Open the Instagram login page.
        self.driver.get(INSTA_URL)
        time.sleep(2)
        # Find and fill in the info for the username and password fields.
        self.handle_exceptions("find_write_xpath", '//*[@id="loginForm"]/div/div[1]/div/label/input', INSTA_EMAIL)
        self.handle_exceptions("find_write_xpath", '//*[@id="loginForm"]/div/div[2]/div/label/input', INSTA_PASSWORD)
        # Find and click the login button.
        time.sleep(4)
        if self.handle_exceptions("find_click_xpath", '//*[@id="loginForm"]/div/div[3]/button'):
            # Find and click the "Not Now" button.
            time.sleep(10)
            self.handle_exceptions("find_click_xpath", '//*[@id="mount_0_0_id"]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div')
    def find_followers(self):
        pass

    def follow(self):
        pass


# Outside of the class , initialise the object and call the three methods in order.
insta_bot = InstaFollower()
insta_bot.login()
insta_bot.find_followers()
insta_bot.follow()


while True:
    current_time = time.time()
    elapsed_time = current_time - start_time
    minutes_left = int(WINDOW_TIME - elapsed_time) // 60
    seconds_left = int((WINDOW_TIME - elapsed_time) % 60)

    if elapsed_time > WINDOW_TIME:
        break

    print(f"Program is running! {minutes_left}:{seconds_left} left.")


    time.sleep(5)