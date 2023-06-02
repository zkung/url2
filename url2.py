import requests
import re
from bs4 import BeautifulSoup
from lxml import etree
from autoscraper import AutoScraper
import json

class url2(object):
    """
    """
    def __init__(self, url, headers={'User-Agent':'Mozolla/5.0'}, encode=False, verify=True, redirect=True, form_data=None):
        self.url = url
        self.headers = headers
        self.encode = encode
        self.verify = verify
        self.redirect = redirect
        self.form_data = form_data
        self.html = self.url2html

    @property
    def url2html(self) -> str:
        """
        url2html
        """
        if isinstance(headers, str):
            self.headers = self.headers_handle(headers)
        if self.form_data == None:
            r = requests.get(self.url, headers=self.headers, verify=self.verify, allow_redirects=self.redirect)
            if self.encode == False:
                r.encoding = r.apparent_encoding
            else:
                r.encoding = self.encode
            r = requests.get(self.url, headers=self.headers, verify=self.verify, allow_redirects=self.redirect)
            if self.encode == False:
                r.encoding = r.apparent_encoding
            else:
                r.encoding = r.apparent_encoding
                r.encoding = 'utf-8'
            self.response = r
            return self.response.text
        else:
            form_data = self.form_data
            headers = self.headers
            r = requests.post(self.url,data=form_data, headers=headers, verify=self.verify, allow_redirects=self.redirect)
            self.response = r
            return self.response.text

    @staticmethod
    def headers_handle(headers: str) -> dict:
        '''
        Add quotes to the request header
        '''
        if headers[0] == '\n':
            headers = headers[1:]
        pattern = '^(.*?):[\s]*(.*?)$'

        dict_str = ''
        dict_str += '{'
        for line in headers.splitlines():
            dict_str += re.sub(pattern,'\'\\1\':\'\\2\',',line)
        dict_str += '}'
        
        dict_ = eval(dict_str)
        return dict_


    @property
    def json(self) -> dict: return json.loads(self.html)

    @property
    def soup(self) -> BeautifulSoup: return BeautifulSoup(self.html)
    
    @property
    def xpath(self) -> etree.HTML: return etree.HTML(self.html).xpath
    
    
    def build(self, wanted_dict, model_name=None):
        """
        url2autospider
        wanted_dict -> [Wanted]
        """
        html_ = self.html
        url = self.url
        scraper = AutoScraper()
        result = scraper.build(html=html_, wanted_dict=wanted_dict)
        if model_name:
            scraper.save(model_name)
        return result
        
    
    def build_load(self, url, model_name='1'):
        """
        Load build model
        """
        scraper = AutoScraper()
        scraper.load(model_name)
        html_ = requests.get(url)
        html_.encoding = html_.apparent_encoding
        html_ = html_.text
        data = scraper.get_result_similar(url, html=html_, group_by_alias=True)
        return data

if __name__ == '__main__':
  data = url2('https://api.github.com/users/zkung')
  print(data.json)
  print(data.response.url)
