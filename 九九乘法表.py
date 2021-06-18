#!/bin/bash
# -*- coding: UTF-8 -*-

for x in range(1, 10):
    for y in range(1, x+1):
        print( "{} * {} = {:<5}".format(x, y, x*y),end = " " )
    print("")