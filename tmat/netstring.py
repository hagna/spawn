#!/usr/bin/python
 
import sys
prefix = sys.argv[1]
 
def printns(s):
    sys.stdout.write('%d:%s\n' % (len(s), s))
 
while True:
    line = sys.stdin.readline()
    if not line:
        break
    printns(prefix)
    printns(line)
