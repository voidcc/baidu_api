# -*- coding: utf-8 -*-
import sys, urllib, urllib2, json


def get_apikey():
    f = open('apikey.txt','r')
    apikey = f.readline()
    f.close()
    return apikey

def generate_url():
    url = 'http://apis.baidu.com/apistore/weatherservice/citylist?'
    #phone_num = raw_input('Please input your phone number --> ')
    params = {'cityname': '朝阳'}
    url += urllib.urlencode(params)
    print url
    return url

def request_baidu(url, apikey):
    headers = {'apikey': apikey}
    req = urllib2.Request(url, headers = headers)
    resp = urllib2.urlopen(req)
    if resp.getcode() == 200:
        content = resp.read()
        #content = content.encode('utf-8')
        if(content):
            print(json.loads(content))

if __name__ == "__main__":
    apikey = get_apikey()
    url = generate_url()
    request_baidu(url, apikey)
