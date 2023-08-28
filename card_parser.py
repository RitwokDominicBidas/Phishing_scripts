#!/usr/bin/env python3

import re

questions = re.compile(r"\S.+cardnumber\=(?P<cardnumber>\S.+)\&cardname\=(?P<cardname>\S.+)\&cardexpiry\=(?P<cardexpiry>\S.+)\&cardverification\=(?P<cardverification>\S.+)\sHTTP\S.+")
log = open("/var/log/apache2/access.log", "r")
array = []

for l in log:
    u = questions.findall(l)
    if u:
        print(u)
    else:
        exit
