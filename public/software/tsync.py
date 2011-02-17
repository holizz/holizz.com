







#TODO: fork and run as a daemon
# Twitter
from xml.etree import ElementTree
from urllib2 import urlopen
from os import system as s
u = 'http://twitter.com/statuses/user_timeline.xml?count=1&id=' + 'holizz'
m = ElementTree.XML(urlopen(u).read()).find('status').find('text').text
status = m.encode('utf8')

# Facebook
import facebook
import yaml
auth = yaml.load(open('facebook.yaml').read())
fb = facebook.Facebook(auth['api'], auth['secret'])
fb.auth.createToken()
fb.login()
#TODO: recover from random: facebook.FacebookError
fb.auth.getSession()

if fb.users.hasAppPermission('status_update') != 0:
    #TODO: don't reset unless different
    fb.users.setStatus('"%s"'%status,0)
else:
    print 'Open the following URL to enable this application to make status'+\
          ' updates on your behalf:'
    print fb.get_ext_perm_url('status_update')
