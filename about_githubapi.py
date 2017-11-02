#!/usr/bin/env python3
# _*_ coding = utf-8 _*_

import requests
import json

URL = 'https://api.github.com'

def build_uri(endpoint):
    return '/'.join([URL,endpoint])

def better_print(json_str):
    # indent 缩进
    return json.dumps(json.loads(json_str),indent=4)

def request_method():
   response = requests.get(build_uri('user/emails'),auth = ('testfta',''))
   print(response.status_code)
   print(response.headers)
   print(better_print(response.text))

def params_request():
    response = requests.get(build_uri('users'),params={'since':11})
    print(better_print(response.text))
    print(response.request.headers)
    print(response.url)

def json_request():
    # 修改
    response = requests.patch(build_uri('user'),auth= ('testfta',''),json = {'name':'mytestfta'})
    print(better_print(response.text))
    print(response.request.headers)
    print(response.request.body)
    print(response.status_code)
    response.elapsed

def time_request():
    try:
        response = requests.get(build_uri('user/emails'),timeout = 0.10)
        response.raise_for_status()
    except requests.exceptions.Timeout as e:
        print(e)
    except requests.exceptions.HTTPError as e:
        print(e)
    else:
        print(response.text)

def hard_request():
    from requests import Request,Session
    s = Session()
    headers = {'User-Agent':'fake1.3.4'}
    req = Request('GET',build_uri('user/emails'),auth=('testfta',''),headers = headers)
    prepared = req.prepare()
    print(prepared.body)
    print(prepared.headers)

    resp = s.send(prepared,timeout = 5)
    print(resp.status_code)
    print(resp.text)

if __name__ == '__main__':
    # print('requests about github')
    # request_method()
    #
    # print('-----requests params-----')
    # params_request()

    # print(('------requests json request----'))
    # json_request()

    # print('-------requests time_request---------')
    # time_request()

    hard_request()