#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  2 11:40:38 2025

@author: ssteel
"""

import csv

data = []

with open("movie_list.txt", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)   # uses the first row as keys automatically
    
    for row in reader:
        data.append(dict(row))   # convert OrderedDict → dict

print(data)
