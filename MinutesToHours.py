#!/usr/bin/env python3
import sys
def Hours(minutes):
    if minutes<0:
        print("Input number cannot be negative")
        #raise ValueError("Input number cannot be negative")
    else:
        print("{} H,{} M".format(int(minutes/60),int(minutes%60)))

try:
    ar=sys.argv[1]
    Hours(int(sys.argv[1]))
except:
    print("Parameter Error")

