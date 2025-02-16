import requests
from loguru import logger
from bs4 import BeautifulSoup


class Parser:
    def init(self, title, url):
        self.title = title
        self.url = url
        self.chapters = {}
        self.chapter = 1

    def get_novel(self):
        page = self.get_webpage(self.url)

    def get_webpage(self, url):
        response = requests.get(url)
        if response.status_code == 200:
            response.encoding = response.apparent_encoding
            logger.info(f"Страница по адресу {url} доступна")
            return BeautifulSoup(response.text, 'html.parser')
        else:
            logger.error(f"Сервер вернул {response.status_code} статус")
            