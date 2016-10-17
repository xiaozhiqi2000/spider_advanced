# -*- coding: utf-8 -*-

import requests

s = requests.get("http://www.12306.cn/mormhweb/")
with open("12306.html", "w") as fd:
    fd.write(s.content)
















# vim: set ts=4 sw=4 sts=4 tw=100 et:
