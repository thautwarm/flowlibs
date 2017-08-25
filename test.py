#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 07:40:40 2017

@author: misakawa
"""

from flowlibs.rule.rule_url import img_downloader, headers
from flowlibs.rule.rule_str import Rule, re

url = "http://www.apic.in/"

main = re.compile('<img[\w\W]+?>')
rule = Rule(main)
selector = img_downloader(rule)
res  = selector.getfrom(url)
for i in range(1):
    r =  next(res)
































