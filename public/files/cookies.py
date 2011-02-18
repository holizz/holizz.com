#!/usr/bin/env python

import cookielib, sys, os, urllib2

class FakeRequest:
# ['/home/holizz/.config/uzbl/cookies.py', '/home/holizz/.config/uzbl/config', '12212', '48234499', '/tmp/uzbl_fifo_48234499', '/tmp/uzbl_socket_48234499', 'http://twitter.com/', 'Twitter: What are you doing?', 'GET', 'twitter.com', '/images/black.png']
# ['/home/holizz/.config/uzbl/cookies.py', '/home/holizz/.config/uzbl/config', '13068', '44040195', '/tmp/uzbl_fifo_44040195', '/tmp/uzbl_socket_44040195', 'gmail.com', '', 'PUT', 'www.google.com', '/accounts/ServiceLogin', 'GALX=25nl_AE-NIk; path=/accounts; domain=www.google.com; secure; HttpOnly']
    def __init__(self, argv):
        self.argv = argv
        self.cookies = None
        if len(self.argv) == 12:
            self.cookies = self.argv[11]
    def get_full_url(self):
        #TODO: this is a hack, fix in uzbl.c!
        u = self.get_host()+self.argv[10]
        if self.argv[6].startswith('https'):
            u = 'https://'+u
        else:
            u = 'http://'+u
        return u
    def get_host(self):
        return self.argv[9]
    def get_type(self):
        return self.get_full_url().split(':')[0]
    def is_unverifiable(self):
        return False
    def get_origin_req_host(self):
        return self.argv[9]
    def has_header(self, header):
        if header == 'Cookie':
            return self.cookies!=None
    def get_header(self, header_name, default=None):
        if header_name == 'Cookie' and self.cookies:
            return self.cookies
        else:
            return default
    def header_items(self):
        if self.cookies:
            return [('Cookie',self.cookies)]
        else:
            return []
    def add_unredirected_header(self, key, header):
        if key == 'Cookie':
            self.cookies = header

class FakeHeaders:
    def __init__(self, argv):
        self.argv = argv
    def getallmatchingheaders(self, header):
        if header == 'Set-Cookie' and len(self.argv) == 12:
            return ['Set-Cookie: '+self.argv[11]]
        else:
            return []
    def getheaders(self, header):
        if header == 'Set-Cookie' and len(self.argv) == 12:
            return [self.argv[11]]
        else:
            return []
class FakeResponse:
    def __init__(self, argv):
        self.argv = argv
    def info(self):
        return FakeHeaders(self.argv)

if __name__ == '__main__':
    jar = cookielib.MozillaCookieJar(os.environ['XDG_DATA_HOME']+'/uzbl/cookies.txt')
    try:
        jar.load()
    except:
        pass

    req = FakeRequest(sys.argv)

    action = sys.argv[8]

    if action == 'GET':
        jar.add_cookie_header(req)
        if req.cookies:
            print req.cookies
    elif action == 'PUT':
        res = FakeResponse(sys.argv)
        jar.extract_cookies(res,req)
        #jar.save(ignore_discard=True)
        jar.save()
