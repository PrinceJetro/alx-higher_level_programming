#!/usr/bin/python
def no_c(my_string):
    tr = str.maketrans('',''.'Cc')
    ns = my_string.translate(tr)
    return ns
