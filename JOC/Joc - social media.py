import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver.common.action_chains import ActionChains


class Tests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        # navigate to the application home page
        self.driver.get("https://www.justonecookbook.com/")





    def test_link_to_facebook(self):
            self.driver.get('https://www.justonecookbook.com/')
            self.driver.fullscreen_window()
            time.sleep(3)
            facebook_button = self.driver.find_element(By.ID, "menu-item-74647")
            facebook_button.click()
            time.sleep(10)
            p = self.driver.current_window_handle
            parent = self.driver.window_handles[0]
            chld = self.driver.window_handles[1]
            self.driver.switch_to.window(chld)
            assert self.driver.current_url == "https://www.facebook.com/justonecookbook"
            self.driver.quit()


    def test_link_to_instagram(self):
        instagram_button = self.driver.find_element(By.XPATH, '//*[@id="menu-item-74651"]/a')
        instagram_button.click()
        time.sleep(10)
        p = self.driver.current_window_handle
        parent = self.driver.window_handles[0]
        chld = self.driver.window_handles[1]
        self.driver.switch_to.window(chld)
        assert self.driver.current_url == "https://www.instagram.com/justonecookbook/"

    def test_link_to_pinterest(self):
        self.driver.get('https://www.justonecookbook.com/')
        self.driver.fullscreen_window()
        time.sleep(3)
        pinterest_button = self.driver.find_element(By.XPATH, '//*[@id="menu-item-74650"]/a')
        pinterest_button.click()
        time.sleep(10)
        p = self.driver.current_window_handle
        parent = self.driver.window_handles[0]
        chld = self.driver.window_handles[1]
        self.driver.switch_to.window(chld)
        assert self.driver.current_url == "https://www.pinterest.com/justonecookbook/"
        self.driver.quit()


    def test_link_to_twitter(self):
            self.driver.get('https://www.justonecookbook.com/')
            self.driver.fullscreen_window()
            time.sleep(3)
            twitter_button = self.driver.find_element(By.ID, 'menu-item-74648')
            twitter_button.click()
            time.sleep(10)
            p = self.driver.current_window_handle
            parent = self.driver.window_handles[0]
            chld = self.driver.window_handles[1]
            self.driver.switch_to.window(chld)
            assert self.driver.current_url == "https://twitter.com/i/flow/login?redirect_after_login=%2Fjustonecookbook"

    def test_link_to_youtube(self):
            self.driver.get('https://www.justonecookbook.com/')
            self.driver.fullscreen_window()
            time.sleep(3)
            youtube_button = self.driver.find_element(By.XPATH, '//*[@id="menu-item-74649"]/a')
            youtube_button.click()
            time.sleep(10)
            p = self.driver.current_window_handle
            parent = self.driver.window_handles[0]
            chld = self.driver.window_handles[1]
            self.driver.switch_to.window(chld)
            assert self.driver.current_url == "https://www.youtube.com/user/justonecookbook"
            self.driver.quit()

    def tearDown(self):
    # close the browser window
     self.driver.quit()
