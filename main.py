import json
import os
import random
# from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
# from selenium.webdriver.chrome.self.options import Options
# from selenium.webdriver.chrome.service import Service
import time
import undetected_chromedriver as uc 

class Google_scraper():
    def __init__(self , url , detach=False):



        self.url = url
        self.detach = detach
        self.start()
        self.soups = []

        self.full_data = []


    def init_driver(self , detach):
        with open("config.json" , "r") as f:
            config = json.load(f)

        
        detach = config.get('detach', detach)       

        self.options = uc.ChromeOptions()

        

        directory =  config.get('user_directory', "C:/Users/rajvendra rahi/AppData/Local/Google/Chrome/User Data")
        user_data_dir = os.path.normpath(directory)
        profile_dir = config.get('profile_directory', "default")

        self.options.add_argument(f"--user-data-dir={user_data_dir}")
        self.options.add_argument(f"--profile-directory={profile_dir}")

        # Preferences
        prefs = {
            "profile.default_content_setting_values.notifications": 2,
            "profile.default_content_setting_values.geolocation": 1,
            "download.default_directory": "NUL",
            "download.prompt_for_download": False
        }
        self.options.add_experimental_option("prefs", prefs)

        # User-Agent (optional, usually inherited from profile)
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.180 Safari/537.36"
        self.options.add_argument(f"user-agent={user_agent}")

        # Other flags
        self.options.add_argument("--disable-infobars")
        self.options.add_argument("--start-maximized")
        self.options.add_argument("--no-sandbox")
        self.options.add_argument("--disable-dev-shm-usage")
        self.options.add_argument("--disable-blink-features=AutomationControlled")

        # self.options.add_experimental_option("detach" , False)
        # Start driver
        self.driver = uc.Chrome(options=self.options , enable_cdp_events=detach)
        self.driver.set_page_load_timeout(60)


       
    def type_text(self, keywords):
        self.keywords = keywords

        for k in keywords:
            self.key = k

            search_box = self.driver.find_element(By.NAME, "q")

            time.sleep(2)

            for char in self.key :
                search_box.send_keys(char)
                time.sleep(random.uniform(0.1, 0.8))
            time.sleep(random.uniform(0.1, 0.8))
            search_box.send_keys(Keys.ARROW_DOWN)
            time.sleep(random.uniform(0.1, 0.8))
            search_box.send_keys(Keys.RETURN)

            time.sleep(5) 

        

            # Wait for search results to load
            wait = WebDriverWait(self.driver, 10)
            wait.until(EC.presence_of_element_located((By.ID, "search")))

            # Get page source and create soup object
            page_source = self.driver.page_source
            soup = BeautifulSoup(page_source, 'html.parser')

            self.soups.append(soup)

            # Open new tab
            self.driver.execute_script("window.open('');")
            self.driver.switch_to.window(self.driver.window_handles[-1])
            self.driver.get(self.url)
            time.sleep(2)
       
    def start(self):
        self.init_driver(self.detach)
        self.driver.get(self.url)
        self.driver.implicitly_wait(10)

    def get_data_from_soups(self):

        for k , soup in zip( self.keywords ,  self.soups):
            
            data = {
                "keyword" : k,
                "Ads" : []
            }

            new_soup = soup


            webs = new_soup.find_all('div', class_='uEierd')


            for index, web in enumerate(webs):
                

                sub_urls = []
            
                small_urls = []

                sub_webs = web.find_all('div', class_='iCzAIb') or  web.find_all('div', class_='Ktlw8e') or web.find_all('div', class_='nS9mjd E8hWLe lndKif SVMeif OcpZAb')

                for sub_web in sub_webs:
                    
                    
                    t = sub_web.find_all('div', class_='DkX4ue') or sub_web.find_all('div' , class_ = "aFn4tc DZm15c MBeuO")


                    for  index , sub_t  in enumerate(t) :
                        try :

                            sub_url = sub_web.find("a" )['href']

                        except :
                            sub_url = []

                        try:
                            des = sub_web.find_all('div', class_='wHYlTd dFcyOb')[index].text or []
                        except:
                            des = []
                        sub_urls.append({
                            "Link_display_text":sub_t.text,
                            "Link" :sub_url ,
                            "Description": des

                        })        

                


                title = web.find('span', class_='pKWwCd yUTMj').text
                url = web.find('span', class_='x2VHCd OSrXXb ob9lvb')
                try:
                    ad_title = web.find('div', class_= 'CCgQ5 vCa9Yd QfkTvb N8QANc Va3FIb EE3Upf').text
                except:
                    ad_title =[]
                des = web.find('div', class_='p4wth').text
                
                anchor_div = web.find('div', class_='bOeY0b')

                try:
                    anchors = anchor_div.find_all('a')
                except:
                    anchors = []

                for anchor in anchors:
                    small_urls.append({
                        "Link_display_text":anchor.text,
                        "Link":anchor['href']
                    })



                data["Ads"].append( {"Post_owner":title ,  "Link":"https://"+url['data-dtld'] ,"Ad_title " : ad_title , "Ad_text":des , "Direct_links" : sub_urls, "Small_links" : small_urls, "Ad_position" : index + 1} )

            self.full_data.append(data)
        return json.dumps(self.full_data , indent=4)


g =  Google_scraper("https://www.google.com/" , detach=False)



keywords = ["genrative ai courses" , "emp monitor" , "almabetter" ]
g.type_text(keywords)







with open('output.json', 'w') as f:
    f.write(g.get_data_from_soups())







