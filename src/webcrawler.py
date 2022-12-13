import requests
import lxml
import re
import os
from bs4 import BeautifulSoup
from dotenv import load_dotenv


load_dotenv()

class Webcrawler:
    headers = {
        'User-Agent': os.getenv("USER_AGENT")
    }

    # format custom atribut "nameAttr:value"
    condition = {}
    soup = ""
    list = []

    def __init__(self, url, condition=None):
        self.url = url
        self.condition = condition

        # soup beautiful
        f = requests.get(url, headers = self.headers)
        self.soup = BeautifulSoup(f.content, 'lxml')



    def run(self):
        href = self.condition['href']

        targetRoot = self.soup.find_all(href['tag'], {'class' : href['class']})


        return targetRoot



    # def callback(self, content):c
