#!/usr/bin/env python
# visit https://tool.lu/pyc/ for more information
# Version: Python 2.7

print 'Welcome to Re World!'
print 'Your input1 is your flag~'
l = len(input1)
for i in range(l):
    num = ((input1[i] + i) % 128 + 128) % 128
    code += num

for i in range(l - 1):
    code[i] = code[i] ^ code[i + 1]

print code
code = [
    '%1f',
    '%12',
    '%1d',
    '(',
    '0',
    '4',
    '%01',
    '%06',
    '%14',
    '4',
    ',',
    '%1b',
    'U',
    '?',
    'o',
    '6',
    '*',
    ':',
    '%01',
    'D',
    ';',
    '%',
    '%13']
