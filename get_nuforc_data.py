#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 21:44:36 2019

@author: helder
"""

import urllib.request
import time
import csv
from datetime import datetime as dt
from bs4 import BeautifulSoup


root_url = 'http://www.nuforc.org/webreports/ndxevent.html'


page = urllib.request.urlopen(root_url)

# parse the html using beautiful soup and store in variable `soup`
bs = BeautifulSoup(page, 'html.parser')


# get the initial list of month/year available
link_list = []
for link in bs.find_all('a', href=True):
    if 'ndxe' in link['href']:
        full_link = 'http://www.nuforc.org/webreports/{}'.format(link['href'])
        link_list.append(full_link)
        

# parse the initial list of link to recover the reports with all available data and save in CSV file
str_now = dt.now().strftime('%Y-%m-%d')
fn_final = 'output_{}.csv'.format(str_now)
with open(fn_final, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    
    for link in link_list:
        page = urllib.request.urlopen(link)
        bs = BeautifulSoup(page, 'html.parser')
        
        for l in bs.find_all('tr'):
            tmp_list = []
            
            for m in l.find_all('font'):
                tmp_list.append(m.text)
                
            writer.writerow(tmp_list)
            print(tmp_list[:4])
            
        time.sleep(2)
        
print('-- Finished!')
        
        
        
