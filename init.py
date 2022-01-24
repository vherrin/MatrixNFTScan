#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import glob
import numpy as np
import cloudscraper
import re
import math
import shutil
import os
import sys
import cfscrape
import time
import requests
import IPython
import webbrowser
import json
import logging

from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

from datetime import date
from IPython.display import HTML
from IPython.display import display
from IPython.display import clear_output
from urllib.request import urlopen
from bs4 import BeautifulSoup
              


# In[2]:


pd.set_option("display.max_rows", None)

dataDir = './data/'

#contractURLs=['ckw5j7pqf0011g4731pvaj6gm/']
#contractURLs=['ckw5j7pqf0011g4731pvaj6gm/', 'matrix-red-contract/', 'matrix-blue-contract/']
contractURLs=['matrix-red-contract/', 'matrix-blue-contract/']
#contractURLs='ckw5j7pqf0011g4731pvaj6gm/'
#contractURLs='matrix-red-contract/'


# In[3]:


attributeList = {}
dfDict = {}
contractColumnDict={}

for contractURL in contractURLs:
    contractPath = dataDir + contractURL
    
    if os.path.exists(contractPath + 'retrievedColumnsList.txt'):
        #print('path exists')
        with open(contractPath + 'retrievedColumnsList.txt', 'r') as filehandle:
            contractColumnDict[contractURL] = json.load(filehandle)
            #print(contractColumnDict[contractURL])
    
    attributeList[contractURL] = [contractPath + 'Attributes_1_5000.csv',
    contractPath + 'Attributes_5001_10000.csv',
    contractPath + 'Attributes_10001_15000.csv',
    contractPath + 'Attributes_15001_20000.csv',
    contractPath + 'Attributes_20001_25000.csv',
    contractPath + 'Attributes_25001_30000.csv', 
    contractPath + 'Attributes_30001_35000.csv',
    contractPath + 'Attributes_35001_40000.csv',
    contractPath + 'Attributes_40001_45000.csv', 
    contractPath + 'Attributes_45001_50000.csv', 
    contractPath + 'Attributes_50001_55000.csv', 
    contractPath + 'Attributes_55001_60000.csv',
    contractPath + 'Attributes_60001_65000.csv',
    contractPath + 'Attributes_65001_70000.csv',
    contractPath + 'Attributes_70001_75000.csv',
    contractPath + 'Attributes_75001_80000.csv',
    contractPath + 'Attributes_80001_85000.csv',
    contractPath + 'Attributes_85001_90000.csv',
    contractPath + 'Attributes_90001_95000.csv',
    contractPath + 'Attributes_95001_100000.csv']
    dfDict[contractURL] = pd.concat(map(pd.read_csv, attributeList[contractURL]))
    mci = contractColumnDict[contractURL].copy()
    mci.insert(0,'ID')
    dfDict[contractURL].columns = mci.copy()  
    print('Length of ' + contractURL + ' attributes added ', len(dfDict[contractURL].index))
    #print(dfDict[contractURL].columns)
    dfTemp = dfDict[contractURL]
    validCount = len(dfTemp.index) - len(np.where(pd.isnull(dfTemp['Background']))[0])
    print('Number of valid rows with ' + contractURL + ' attributes ', validCount)
    print('\n')
    


# In[ ]:




