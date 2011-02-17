#!/usr/bin/env python

import subprocess, urllib2

def execurl(url):
    exec urllib2.urlopen(url).read()

def readurl(url):
    return urllib2.urlopen(url).read()

def download(url,target=None):
    if target==None:
        target=url.split('/')[-1]
    f = open(target,'w+')
    f.write(readurl(url))
    f.close()

if __name__ == "__main__":
    # Dvorak and ctrl:nocaps emulation
    xmm=subprocess.Popen(['xmodmap','-'],stdin=subprocess.PIPE)
    pke=readurl('http://holizz.com/software/shef-thinclients/dvorak_nocaps.pke')
    xmm.communicate(pke)
