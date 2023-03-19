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


root_url = 'https://nuforc.org/webreports/ndxevent.html'


page = urllib.request.urlopen(root_url)

# parse the html using beautiful soup and store in variable `soup`
bs = BeautifulSoup(page, 'html.parser')


# get the initial list of month/year available
link_list = []
for link in bs.find_all('a', href=True):
    
    if 'ndxe' in link['href']:
        #print(link['href'])
        full_link = 'https://nuforc.org/webreports/{}'.format(link['href'])
        link_list.append(full_link)
        

# parse the initial list of link to recover the reports with all available data and save in CSV file
str_now = dt.now().strftime('%Y-%m-%d')
fn_final = 'output_{}.csv'.format(str_now)
with open(fn_final, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    
    for link in link_list:
        #print(link)
        page = urllib.request.urlopen(link)
        bs = BeautifulSoup(page, 'html.parser')
        
        for l in bs.find_all('tr'):
            tmp_list = []
            
            #print(l)
            for m in l.find_all('td'):
                tmp_list.append(m.text.encode('UTF-8'))

            print(tmp_list[:4])    
            writer.writerow(tmp_list)
            
        time.sleep(2)
        
print('-- Finished!')
        
        
        
