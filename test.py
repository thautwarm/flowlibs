#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 07:40:40 2017

@author: misakawa
"""

from rule.rule_url import img_downloader
from rule.rule_str import Rule, re

url = "http://www.apic.in/"

main = re.compile('<img[\w\W]+?>')
selector = img_downloader(Rule(main))
res = selector.getfrom(url)