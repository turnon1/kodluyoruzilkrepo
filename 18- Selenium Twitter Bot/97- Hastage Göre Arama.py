
from UserInfo import username, password
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class Twitter:
    def __init__(self, username, password):
        self.browserProfile = webdriver.ChromeOptions()
        self.browserProfile.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})
        self.browser = webdriver.Chrome('C:/Users/veyse/OneDrive/Masaüstü/Yazılım/Python/16- Bot Yazımı/chromedriver.exe', chrome_options=self.browserProfile)
        self.username = username
        self.password = password
    
    def signIn(self):
        self.browser.get("https://twitter.com/i/flow/login")
        time.sleep(2)

        usernameInput = self.browser.find_element_by_xpath("//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[5]/label/div/div[2]/div/input")
        
        usernameInput.send_keys(self.username, Keys.ENTER)
        #btnSubmit = self.browser.find_elements_by_xpath("//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[6]/div/span/span")
        #btnSubmit.click()
        time.sleep(2)
        PasswordInput = self.browser.find_element_by_xpath("//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input")
        PasswordInput.send_keys(self.password, Keys.ENTER)
        time.sleep(2)

    def search(self, hashtag):
        searchInput = self.browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/label/div[2]/div/input")
        searchInput.send_keys(hashtag, Keys.ENTER)
        time.sleep(3)

        #atılan tweetlerin yazı kısımlarını alıyoruz
        #list =  self.browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/section/div/div/div[5]/div/div/article/div/div/div/div[2]/div[2]/div[2]/div[1]/div/div")
        list =  self.browser.find_element_by_xpath("//article[@data-testid='tweet']/div/div/div/div[2]/div[2]/div[2]/div[1]/div/div")
        #for item in list:
        for list in list:
            print(list.text)

        
twitter = Twitter(username,password)
#login
twitter.signIn()
twitter.search("python")

