#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 07:40:40 2017

@author: misakawa
"""

from flowlibs.rule.rule_url import img_downloader, headers, html_reader
from flowlibs.rule.rule_str import Rule, re

#url = "http://www.apic.in/"
url = 'http://materializecss.com/icons.html'

#main = re.compile('<img[\w\W]+?>')
main = re.compile('<div class="icon-preview col s6 m3">[\w\W]?</span></div>')
rule = Rule(main)
res = html_reader(rule).getfrom(url)

#selector = img_downloader(rule)
#res  = selector.getfrom(url)
#for i in range(1):
#    r =  next(res)
































