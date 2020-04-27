#!/usr/bin/env python3
with open("/tmp/String.txt") as fo:
    s=fo.read()
retu=''
for char in s:
    if char.isdigit():
        retu+=char
print(retu)
