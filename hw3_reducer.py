#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 20:44:23 2021

@author: ANDISHE
"""

import sys
import collections

counter = collections.Counter()
once = collections.Counter()

sum = 0
word_list = []

for line in sys.stdin:
    line = line.strip()
    word, count = line.split(" ", 2)
    
    counter[word] = counter[word] + int(count)
    
    once[word] = once[word]+int(count)
    
    if once[word] == 1:
        word_list.append(word)
        sum = sum+1
print(counter.most_common(10))