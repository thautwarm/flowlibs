#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 07:40:40 2017

@author: misakawa
"""

#from flowlibs.rule.rule_url import img_downloader, headers
#from flowlibs.rule.rule_str import Rule, re
#
#url = "http://www.apic.in/"
#
#main = re.compile('<img[\w\W]+?>')
#rule = Rule(main)
#selector = img_downloader(rule)
#res  = selector.getfrom(url)
#for i in range(1):
#    r =  next(res)




from flowpython.fp import  flat_map, flow_reduce #flow_map ,andThen, fastmap
a = [[1,2,3],[3,4,6], [2,3,4,5,6,7,8],[2,[3,4],[5],[1,[2],3] ]]
#fast_flat_map = lambda f: andThen(flatten)(fastmap(f))
res = a ->> flat_map(.x->x+1) => list 
res     ->> print
res     ->> flow_reduce(.x,y->x-y) => print


































