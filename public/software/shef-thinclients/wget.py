#!/usr/bin/env python

import sys, urllib2

def readurl(url):
    return urllib2.urlopen(url).read()

def download(url,target=None):
    if target==None:
        target=url.split('/')[-1]
    f = open(target,'w+')
    f.write(readurl(url))
    f.close()

if __name__ == "__main__":
    for arg in sys.argv[1:]:
        download(arg)
