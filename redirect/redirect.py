import requests

class Redirect:
    def __init__(self, url):
        self.url = url
        
        self.__model = requests.get(url)
        
    def __str__(self):
        return self.url
        
    def __repr__(self):
        return '<Response [{}]>'.format(self.__model.status_code)

    def is_redirect(self):
        return self.url != self.__model.url

    def redirect_url(self):
        if not self.is_redirect:
            return False
        return self.__model.url

    def is_secure(self):
        return self.__model.url.split(':')[0].lower() == 'https'

    def cookies(self):
        return dict(self.__model.raw.headers)['Set-Cookie']

    is_redirect = property(is_redirect)
    redirect_url = property(redirect_url)
    is_secure = property(is_secure)
    cookies = property(cookies)
