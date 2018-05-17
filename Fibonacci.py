#!/usr/bin/python

import sys

mydb = {}

def func(n):
    if n not in mydb:
        if n == 0 or n == 1:
            ret = 1
        else:
            ret = func(n-1) + func(n-2)

        mydb[n] = ret
    else:
        ret = mydb[n]

    return ret


print func(int(sys.argv[1]))
