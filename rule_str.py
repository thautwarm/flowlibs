import urllib.request as urlreq
import requests
from flowpython.fp import foreach, flow_map, andThen
from typing import Dict
from typepy import strict
re = urlreq.re
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
    "Accept": "image/webp,image/*,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, sdch, br",
    "Accept-Language": "zh-CN,zh;q=0.8"
}

class Rule:
    """ To match strings more easily. 
        It could be slower than `re` module, as a result, it could be more powerful and convenient.

        use a `re.compile` object to initial one Rule object.
        >>> main = re.compile("<link[\w\W]+?>")
        >>> relu = Relu(main)
        >>> relu.set_content_filters(dict(dns_filter = "dns", hashref = "href"))
        >>> relu.set_func_filters(dict(lenght_filter = . item -> len(item)>5  ))
    """
    
    def __init__(self, re_compile: re.compile):
        self.filters: str -> bool = dict()
        self.main_rule: str -> [str] = re_compile

    @strict.args(object, dict)
    def set_match_filters(self, filters: Dict[str, re.compile]):
        self.filters.update(filters -> flow_map(_)(. key ->
                                                   (key,  .item -> filters[key].match(item))) 
                                    -> andThen(list)(dict)(_))
        return self

    @strict.args(object, dict)
    def set_func_filters(self, filters: Dict[str, str -> bool]):
        self.filters.update(filters)
        return self

    @strict.args(object, dict)
    def set_content_filters(self, filters: Dict[str, str]):
        self.filters.update(filters -> flow_map(_)(. key -> 
                                                    (key,  .item -> filters[key] in item))    
                                    -> andThen(list)(dict)(_))
        return self

    @strict.args(object, str)
    def match(self, content):
        filter_composed = as-with item def SeeFollowing where:
            for filter_name in self.filters:
                if not self.filters[filter_name](item):
                    return False
            return True
        return self.main_rule.findall(content) -> filter(filter_composed, _) -> tuple(_)
