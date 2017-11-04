#!/usr/bin/env python3
# _*_ coding = utf-8 _*_

import requests

BASIC_URL = 'https://api.github.com'

def construct_url(end_point):
    return '/'.join([BASIC_URL,end_point])

def basic_auth():
    '''
    基本认证
    :return:
    '''
    response = requests.get(construct_url('user'),auth = ('testfta',''))
    print(response.status_code)
    print(response.text)
    print(response.request.headers)

def basic_oauth():
    headers = {'Authorization':'token 0974f97df4a6ad247c881d9b4af4778357b90f5d '}
    response = requests.get(construct_url('user/emails'),headers = headers)
    print(response.request.headers)
    print(response.status_code)

from requests.auth import AuthBase
class GithubAuth(AuthBase):
    def __init__(self,token):
        self.token = token
    def __call__(self, r):
        # requests 加 headers
        r.headers['Authorization'] = ' '.join(['token',self.token])
        return r

def oauth_advanced():
    auth = GithubAuth('0974f97df4a6ad247c881d9b4af4778357b90f5d ')
    response = requests.get(construct_url('user/emails'),auth = auth)
    print(response.text)
    print(response.status_code)


if __name__ == '__main__':
    oauth_advanced()