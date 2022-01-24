#!/usr/bin/env python
# coding: utf-8

# In[ ]:


readFiles = False
get_ipython().run_line_magic('run', './init.ipynb')


# In[ ]:


def in_notebook():
    """
    Returns ``True`` if the module is running in IPython kernel,
    ``False`` if in IPython shell or other Python shell.
    """
    return 'ipykernel' in sys.modules

def ipython_info():
    ip = False
    if 'ipykernel' in sys.modules:
        ip = 'notebook'
    elif 'IPython' in sys.modules:
        ip = 'terminal'
    return ip


# In[ ]:


def renameFileIfExist(fileName):
    if os.path.exists(fileName):
        os.rename(fileName,'old_' + fileName)


# In[ ]:


def saveDictionary(dataDictionary, filename, path):
    if not os.path.exists(path):
        os.makedirs(path)

    renameFileIfExist(fileName)
    fileAndPath = path + filename
    print(fileAndPath)
    dataDictionary.to_csv(fileAndPath)


# In[ ]:


get_ipython().run_cell_magic('time', '', "\nstartRange = 1\nstopRange = 100001\nmodulo = 5000\n\nprint(ipython_info()) \n\n#logging.basicConfig(level=logging.DEBUG)\n\nif (ipython_info() == 'terminal'):\n    if len(sys.argv) > 0:\n        print('in sys if statement')\n        startRange = int(sys.argv[1])\n        stopRange = int(sys.argv[2])\n        modulo = int(sys.argv[3])\n        print('start range is ' + str(startRange))\n        print('stop range is ' + str(stopRange))\n        print('modulo is ' + str(modulo))\n\n\nbaseURL='https://aggregator.api.niftys.com/v1/metadata/contracts/'\n#contractURL='ckw5j7pqf0011g4731pvaj6gm/'\n#contractURL='matrix-red-contract/'\n\nretrievedColumns=[]\n\nfor contractURL in contractURLs:\n    rowAttributes = {}\n    listing = {}\n    blankOutputList = []\n    retrievedColumns.clear()\n    refStartx = startRange\n\n    print('startRange = ' + str(startRange) + ' and stopRange = ' + str(stopRange))\n\n    for avatarNumber in range(startRange, stopRange):\n\n        s = requests.Session()\n        retries = Retry(total=5, backoff_factor=1, status_forcelist=[ 502, 503, 504 ])\n        s.mount('https://', HTTPAdapter(max_retries=retries))\n\n        lineItemJson = s.get(baseURL + contractURL + str(avatarNumber)).text\n        \n        #lineItemJson = requests.get(baseURL + contractURL + str(avatarNumber)).text\n        \n        metadata = json.loads(lineItemJson)\n        output_list=[]\n        \n        for k,v in metadata.items():\n            if type(v) is list:\n                if (len(retrievedColumns) == 0):\n                    coulumnsNameAndLocation = './data/' + contractURL + 'retrievedColumnsList.txt'\n                    if os.path.exists(coulumnsNameAndLocation):\n                        #print('path exists')\n                        with open(coulumnsNameAndLocation, 'r') as filehandle:\n                            retrievedColumns = json.load(filehandle)\n                    else:\n                        #print('in else')\n                        for i in v:\n                            attributeNameList=list(i.values())\n                            retrievedColumns.append(attributeNameList[0]) # name or key of the attribute\n                            blankOutputList.append('')  # fill empty string to match the same size total\n                         # open output file for writing\n                        if (len(retrievedColumns) > 0):\n                            #print('length of retrievedColumns is ' + str(len(retrievedColumns)))\n                            \n                            try:\n                                with open(coulumnsNameAndLocation, 'w') as filehandle:\n                                    json.dump(retrievedColumns, filehandle)\n                            except:\n                                print('made it to except')\n                for attributes in v:\n                    valueList=list(attributes.values())\n                    cleanTextAttribute = valueList[0]\n                    if (len(valueList[1]) > 0):\n                        cleanTextValue = valueList[1]\n                    else:\n                        cleanTextValue = ''\n                    rowAttributes[cleanTextAttribute] = cleanTextValue\n                output_list = [(rowAttributes[key]) for key in (retrievedColumns) if key in rowAttributes]\n        if len(output_list) == 0:\n            listing[str(avatarNumber)] = blankOutputList.copy()\n        else:\n            listing[str(avatarNumber)] = output_list.copy()\n\n        output_list.clear()\n        clear_output(wait=True)\n        print(contractURL, avatarNumber)\n        if(avatarNumber % modulo == 0):\n            if refStartx == 1:\n                refStartx = 0\n            data_dictionary =  pd.DataFrame.from_dict(listing, orient='index', columns=retrievedColumns)  #pd.DataFrame(listing, orient='index')\n            fileName = 'Attributes_' + str(refStartx + 1) + '_' + str(avatarNumber) + '.csv'\n            saveDictionary(data_dictionary, fileName, './data/' + contractURL )\n            refStartx = avatarNumber\n            listing.clear()")


# In[ ]:


#fileName = 'Attributes_' + str(refStartx + 1) + '_' + str(x) + '.csv'
#renameFileIfExist(fileName)
#data_dictionary =  pd.DataFrame.from_dict(listing, orient='index', columns=manualColumns)  #pd.DataFrame(listing, orient='index')
#data_dictionary.to_csv(fileName)


# In[ ]:


#for count in range(0, len(manualColumns)):
#    print(count)
#    print(data_dictionary[manualColumns[count]].value_counts())
#    data_dictionary[manualColumns[count]].value_counts(normalize=True)
#    print('---------------------------------')


# In[ ]:


print('done')


# In[ ]:




