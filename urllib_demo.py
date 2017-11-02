# _*_ coding: utf-8 _*_
import urllib
from urllib import request,parse

URL_IP = 'http://httpbin.org/ip'
URL_GET = 'http://httpbin.org/get'

def use_simple_urllib():
    response = request.urlopen(URL_IP)
    print('>>>Response Headers:')
    print(response.info())
    print('>>>Response Body')
    print(response.read().decode('utf-8'))

def use_params_urllib():
    params = urllib.parse.urlencode({'param1':'hello','param2':'world'})
    print('>>>Request Params:')
    print(params)
    response = urllib.request.urlopen('?'.join([URL_GET,'%s'])% params)
    print('>>>Response Headers:')
    print(response.info())
    print(">>>Status Code:")
    print(response.getcode())
    print('>>>Response Body')
    print(response.read().decode('utf-8'))

if __name__ == '__main__':
    print('-----Use simple urllib-----')
    use_simple_urllib()

    print('-----Use params urllib-----')
    use_params_urllib()

