import requests

class Redirect:
    def __init__(self, url):
        self.url = url
        
        self.__model = requests.get(url)
        
    def __str__(self):
        return self.url
        
    def __repr__(self):
        return '<Response [{}]>'.format(self.__model.status_code)
