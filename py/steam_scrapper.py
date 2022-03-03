# -*- coding: utf-8 -*-
"""

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16RTQqm14okpqylLwDA65bNFNuFwo4bY_
"""

import json
from urllib.request import urlopen
import requests,json,os,sys,time,re
from google.colab import files

jsons = list()
n1 = 0 # change the n1 to 10, 20, 30, 40, 50, 60 and 80 *1000 depending on the run
n2 = n1 + 10000 # change the 10000 to 20000 after n1 is 60000
for i in range(n1,n2,1):
  req = requests.get(
      'https://steamspy.com/api.php?request=appdetails&appid=' + 
      str(i)
      )
  jsons.append(req.json())
  if(((i-n1+1) % 500) == 0):
    print(str((i-n1+1)*100/(n2-n1)) + "% are done")

def list_outputter(jsons, hcs=None):
  if hcs is None: hcs = list()
  start = '('
  end = ')'
  quote = '"'
  space = ' '

  for i in range(len(jsons)):
    if ((i+1) % 1000 == 0): print(i+1)
    hcs.append(list())
    appid_name = 'appid' + str(jsons[i]['appid'])
    hcs[i].append(
        start + 'isa' + space + appid_name + space + 
        'ComputerGameProgram' + end
        )
    hcs[i].append(
        start + 'gameTitleString' + space + appid_name + 
        space + quote + str(jsons[i]['name']) + quote + end
        )
    hcs[i].append(
        start + 'gameDeveloper' + space + appid_name + space + 
        quote + str(jsons[i]['developer']) + quote + end
        )
    hcs[i].append(
        start + 'gamePublisher' + space + appid_name + space + 
        quote + str(jsons[i]['publisher']) + quote + end
        )
    hcs[i].append(
        start + 'gamePositiveRatings' + space + appid_name + 
        space + str(jsons[i]['positive']) + end
        )
    hcs[i].append(
        start + 'gameNegativeRatings' + space + appid_name + 
        space + str(jsons[i]['negative']) + end
        )
    hcs[i].append(
        start + 'gamePrice' + space + appid_name + space + 
        str(jsons[i]['discount']) + end
        )
    hcs[i].append(
        start + 'gameDiscount' + space + appid_name + space + 
        str(jsons[i]['discount']) + end
        )
    hcs[i].append(
        start + 'gameConcurrentlyConnectedUsers' + space + 
        appid_name + space + str(jsons[i]['ccu']) + end
        )
    temp_langs = jsons[i]['languages']
    if temp_langs:
      temp_langs = temp_langs.split(", ")  
      for lang in temp_langs:
        hcs[i].append(
            start + 'gameLanguage' + space + appid_name + space + 
            str(lang) + end
            )
    temp_genres = jsons[i]['genre']
    if temp_genres:
      temp_genres = temp_genres.split(", ")
      for genre in temp_genres:
        hcs[i].append(
            start + 'gameGenre' + space + appid_name + space + 
            str(genre) + end
            )
  
  return(hcs)

hcs = list_outputter(jsons)

vals = list()
for i in range(len(hcs)):
  if(len(hcs[i]) <= 9):
    vals.append(i)


with open('gameclausesxx.txt', 'w') as f:
    for item in hcs:
        f.write("%s\n" % item)
