import re
import time
from bs4 import BeautifulSoup
from selenium import webdriver

class LiveBox():
    def __init__(self):
        self.site_url = 'https://watch.nba.com/'
    
    def get_today_game_urls(self):
        option = webdriver.ChromeOptions()
        option.add_argument("headless")
        driver = webdriver.Chrome(chrome_options=option)
        driver.get(f'{self.site_url}')
        source = driver.page_source
        time.sleep(2)
        driver.close()
        soup = BeautifulSoup(source,'html.parser')
        content = str(soup.find_all('a',onclick=True))
        pattern = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
        today_game_urls = []
        for game_url in re.findall(pattern,content):
            game_url = game_url.replace("')",'')
            today_game_urls.append(game_url)
        return today_game_urls
    
    def get_live_score(self,today_game_url):
        option = webdriver.ChromeOptions()
        option.add_argument("headless")
        driver = webdriver.Chrome(chrome_options=option)
        driver.get(today_game_url)
        source = driver.page_source
        time.sleep(2)
        driver.close()
        return source
    
    def yell_score_currently(self,today_game_url,source):
        soup = BeautifulSoup(source,'html.parser')
        away_score = soup.find(name='div',attrs={'class':'away-score'}).text
        home_score = soup.find(name='div',attrs={'class':'home-score'}).text
        game_quarter = soup.find(name = 'div',attrs = {'class':'game-quarter'}).text
        game_countdown = soup.find(name = 'div',attrs = {'class':'game-countdown'}).text
        away_team = today_game_url.split('/')[-1][0:3]
        home_team = today_game_url.split('/')[-1][3:]
        print(f"{game_quarter} {away_team}:{away_score} {game_countdown} {home_team}:{home_score}")