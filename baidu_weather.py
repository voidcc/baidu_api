# -*- coding: utf-8 -*-
import sys, urllib, urllib2, json

def get_apikey():
    f = open('apikey.txt','r')
    apikey = f.readline()
    f.close()
    return apikey

def generate_url():
    url = 'http://apis.baidu.com/heweather/weather/free?'
    params = {'city': 'hefei'}
    url += urllib.urlencode(params)
    return url

def request_baidu(url, apikey):
    headers = {'apikey': apikey}
    try:
        req = urllib2.Request(url, headers = headers)
        resp = urllib2.urlopen(req)
    except urllib2.HTTPError, e:
        print(e.code)
    except urllib2.URLError, e:
        print(e.reason)
    else:
        content = resp.read()
        content = json.loads(content)
        #print content.keys()
        content = content.get("HeWeather data service 3.0")[0]
        if content is not None and content.get('status') == 'ok':
            print content['status']
        """
        if content.get('errNum') == 0:
            for item in content['retData']:
                for k,v in item.iteritems():
                    print k, v
        """



if __name__ == "__main__":
    apikey = get_apikey()
    url = generate_url()
    request_baidu(url, apikey)
