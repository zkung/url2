import requests
import re
from bs4 import BeautifulSoup
from lxml import etree
from autoscraper import AutoScraper

class url2(object):
    """
    """
    def __init__(self, url, headers={'User-Agent':'Mozolla/5.0'}, encode=False, init=False, verify=True, cdx=True, form_data=None):
        self.url = url
        self.headers = headers
        self.encode = encode
        self.init = init
        self.verify = verify
        self.cdx = cdx
        self.form_data = form_data
        self.html = self.url2html

    @property
    def url2html(self):
        """
        url2html
        """
        if self.form_data == None:
            r = requests.get(self.url, headers=self.headers, verify=self.verify, allow_redirects=self.cdx)
            if self.init == False:
                if self.encode == False:
                    r.encoding = r.apparent_encoding
                else:
                    r.encoding = self.encode
                result = r.text
        else:
            def headers_handle(headers):
                '''
                对请求头加引号
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

            form_data = headers_handle(self.form_data)
            headers = headers_handle(self.headers)
            
            result = requests.post(self.url,data=form_data, headers=headers, verify=self.verify, allow_redirects=self.cdx).text
            
        return result

    @property
    def soup(self):
        """
        url2soup
        """
        html_ = self.html
        soup = BeautifulSoup(html_)
        return soup

    def html2xpath(html_):
        pass
    
    @property
    def xpath(self):
        """
        url2xpath
        """
        html_ = self.html
        return etree.HTML(html_).xpath
    
    
    def build(self, wanted_dict=None, model_name='1'):
        """
        url2autospider
        """
        html_ = self.html
        url = self.url
        scraper = AutoScraper()
        scraper.build(html=html_, wanted_dict=wanted_dict)
        # data = scraper.get_result_similar(url, html=html_, group_by_alias=True)
        scraper.save(model_name)
    
    def auto(self, url, model_name='1'):
        scraper = AutoScraper()
        scraper.load(model_name)
        html_ = requests.get(url)
        html_.encoding = html_.apparent_encoding
        html_ = html_.text
        data = scraper.get_result_similar(url, html=html_, group_by_alias=True)
        return data
