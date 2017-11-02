#!/usr/bin/env python3
# _*_ coding = utf-8 _*_

import requests

def download_img():
    url = 'http://img.kuqin.com/upimg/allimg/140915/2209413P6-0.jpg'
    response = requests.get(url,stream = True)
    print(response.status_code,response.reason)
    with open('demo.jpg','wb') as fd:
        for chunk in response.iter_content(128):
            fd.write(chunk)
    # print(response.content)


def download_img_improved():
    url = 'http://img.kuqin.com/upimg/allimg/140915/2209413P6-0.jpg'
    response = requests.get(url, stream=True)
    from contextlib import closing
    with closing(requests.get(url,stream = True)) as response:
        with open('demo1.jpg','wb') as fd:
            for chunk in response.iter_content(128):
                fd.write(chunk)

if __name__ == '__main__':
    # download_img()
    download_img_improved()