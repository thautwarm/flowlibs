#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 06:17:07 2017

@author: misakawa
"""
import urllib.request as urlreq
from ..typepy import strict, NEq
from urllib.error import HTTPError
from .rule_str import Rule
from typing import Dict
import pandas as pd
from flowpython.fp import foreach

re = urlreq.re
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
    "Accept": "image/webp,image/*,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, sdch, br",
    "Accept-Language": "zh-CN,zh;q=0.8"
}
class html_reader:
    def __init__(self, rule : Rule = None):
        self.rule = rule
        self.html = ""
        self.url  = ""
        
    @strict.args(object, str, headers = dict)
    def getfrom(self, url, headers  = headers):
        self.url =  url
        req      =  urlreq.Request(url, headers = headers)
        with urlreq.urlopen(req) as res:
            if res.status is not 200:
                raise HTTPError(url, res.code, res.msg, res.hdrs, res.fp)
            html = res.read()
        self.html = html
        return self.rule.match(html)
    
    

class img_downloader(html_reader):
    
    def getfrom(self, url, headers = headers):
        res = super(img_downloader, self).getfrom(url, headers = headers)
        def stream():
            for item in res:
                try:
                    req = urlreq.Request(url, headers = headers)
                except Exception as e:
                    print(e)
                    continue
                with urlreq.urlopen(req) as each_res_for_img:
                    ret = each_res_for_img.read()
                yield ret
        yield from stream()
        

    

    
        
    
        
    
        
        
