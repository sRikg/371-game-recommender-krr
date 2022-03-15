with open('game_facts1.krf') as f1:
  lines_1 = f1.readlines()

with open('game_facts2.krf') as f2:
  lines_2 = f2.readlines()

with open('game_facts3.krf') as f3:
  lines_3 = f3.readlines()

with open('game_facts4.krf') as f4:
  lines_4 = f4.readlines()

with open('game_facts5.krf') as f5:
  lines_5 = f5.readlines()

with open('game_facts6.krf') as f6:
  lines_6 = f6.readlines()

with open('game_facts7.krf') as f7:
  lines_7 = f7.readlines()

flat_list = [item for sublist in [lines_1, lines_2, lines_3, lines_4, lines_5, lines_6, lines_7] for item in sublist]
len(flat_list)

devs = [element for element in flat_list if "gameDeveloper" in element]

devs_1 = list()
for devs_rule in devs:
  temp = devs_rule.replace(')\n', "").split(" ")
  devs_1.append(" ".join(item for item in temp[2:len(temp)]))

devs_2 = list(set(devs_1))

devs_2.sort()
n = 700
devs_2[n:n+50]

text = 'CertainAffinity'
temp_1 = [element for element in lines_1 if text in element]
temp_2 = [element for element in lines_2 if text in element]
temp_3 = [element for element in lines_3 if text in element]
temp_4 = [element for element in lines_4 if text in element]
temp_5 = [element for element in lines_5 if text in element]
temp_6 = [element for element in lines_6 if text in element]
temp_7 = [element for element in lines_7 if text in element]

[temp_1, temp_2, temp_3, temp_4, temp_5, temp_6, temp_7]

print(len(lines_1))
print(len(lines_2))
print(len(lines_3))
print(len(lines_4))
print(len(lines_5))
print(len(lines_6))
print(len(lines_7))

languages = [element for element in flat_list if "gameLanguage" in element]

langauges_1 = list()
for language_rule in languages:
  temp = language_rule.replace(')\n', "").split(" ")
  langauges_1.append(" ".join(item for item in temp[2:len(temp)]))

languages_2 = list(set(langauges_1))

languages_2.sort()

languages_3 = list()
for language in languages_2:
  languages_3.append("(isa " + language + " Language)")

languages_3

genres = [element for element in flat_list if "gameGenre" in element]

genres_1 = list()
for genre_rule in genres:
  temp = genre_rule.replace(')\n', "").split(" ")
  genres_1.append(" ".join(item for item in temp[2:len(temp)]))

genres_2 = list(set(genres_1))

genres_2.sort()
genres_2

ccus = [element for element in flat_list if "gameConcurrentlyConnectedUsers" in element]

ccus_1 = list()
for ccus_rule in ccus:
  temp = ccus_rule.replace(')\n', "").split(" ")
  ccus_1.append(int(" ".join(item for item in temp[2:len(temp)])))

ccus_1.sort()
print(min(ccus_1))
print(max(ccus_1))
print(sum(ccus_1)/len(ccus_1))

discounts = [element for element in flat_list if "gameDiscount" in element]

discounts_1 = list()
for discounts_rule in discounts:
  temp = discounts_rule.replace(')\n', "").split(" ")
  discounts_1.append(int(" ".join(item for item in temp[2:len(temp)])))

discounts_1.sort()
print(min(discounts_1))
print(max(discounts_1))
print(sum(discounts_1)/len(discounts_1))

prices = [element for element in flat_list if "gamePrice" in element]

prices_1 = list()
for prices_rule in prices:
  temp = prices_rule.replace(')\n', "").split(" ")
  prices_1.append(int(" ".join(item for item in temp[2:len(temp)])))

prices_1.sort()
print(min(prices_1))
print(max(prices_1))
print(sum(prices_1)/len(prices_1))

nrs = [element for element in flat_list if "gameNegativeRatings" in element]

nrs_1 = list()
for nrs_rule in nrs:
  temp = nrs_rule.replace(')\n', "").split(" ")
  nrs_1.append(int(" ".join(item for item in temp[2:len(temp)])))

nrs_1.sort()
print(min(nrs_1))
print(max(nrs_1))
print(sum(nrs_1)/len(nrs_1))

prs = [element for element in flat_list if "gamePositiveRatings" in element]

prs_1 = list()
for prs_rule in prs:
  temp = prs_rule.replace(')\n', "").split(" ")
  prs_1.append(int(" ".join(item for item in temp[2:len(temp)])))

prs_1.sort()
print(min(prs_1))
print(max(prs_1))
print(sum(prs_1)/len(prs_1))

with open('game_facts1.krf') as f1:
  lines_1 = f1.readlines()

for i in range(len(lines_1)):
  if "gameDeveloper" in lines_1[i]:
    temp = lines_1[i].split(' ')
    if ' ' in ' '.join(temp[2:len(temp)]):
      lines_1[i] = lines_1[i].replace(' ', '-').replace('Developer-', 'Developer ').replace('-"', ' "').replace('-', '').replace('"','')
    else:
      lines_1[i] = lines_1[i].replace('"','')

with open('game_facts_edited1.txt', 'w') as f: # change the number at game_ontology<number>
    for item in lines_1: # change the numbers in the list from 0:400 in the multiples of 400 till the len(new_list)
      for element in item:
        f.write("%s" % element)
        
with open('game_facts2.krf') as f2:
  lines_2 = f2.readlines()

for i in range(len(lines_2)):
  if "gameDeveloper" in lines_2[i]:
    temp = lines_2[i].split(' ')
    if ' ' in ' '.join(temp[2:len(temp)]):
      lines_2[i] = lines_2[i].replace(' ', '-').replace('Developer-', 'Developer ').replace('-"', ' "').replace('-', '').replace('"','')
    else:
      lines_2[i] = lines_2[i].replace('"','')

with open('game_facts_edited2.txt', 'w') as f: # change the number at game_ontology<number>
    for item in lines_2: # change the numbers in the list from 0:400 in the multiples of 400 till the len(new_list)
      for element in item:
        f.write("%s" % element)

with open('game_facts3.krf') as f3:
  lines_3 = f3.readlines()

for i in range(len(lines_3)):
  if "gameDeveloper" in lines_3[i]:
    temp = lines_3[i].split(' ')
    if ' ' in ' '.join(temp[2:len(temp)]):
      lines_3[i] = lines_3[i].replace(' ', '-').replace('Developer-', 'Developer ').replace('-"', ' "').replace('-', '').replace('"','')
    else:
      lines_3[i] = lines_3[i].replace('"','')

with open('game_facts_edited3.txt', 'w') as f: # change the number at game_ontology<number>
    for item in lines_3: # change the numbers in the list from 0:400 in the multiples of 400 till the len(new_list)
      for element in item:
        f.write("%s" % element)
        
with open('game_facts4.krf') as f4:
  lines_4 = f4.readlines()

for i in range(len(lines_4)):
  if "gameDeveloper" in lines_4[i]:
    temp = lines_4[i].split(' ')
    if ' ' in ' '.join(temp[2:len(temp)]):
      lines_4[i] = lines_4[i].replace(' ', '-').replace('Developer-', 'Developer ').replace('-"', ' "').replace('-', '').replace('"','')
    else:
      lines_4[i] = lines_4[i].replace('"','')

with open('game_facts_edited4.txt', 'w') as f: # change the number at game_ontology<number>
    for item in lines_4: # change the numbers in the list from 0:400 in the multiples of 400 till the len(new_list)
      for element in item:
        f.write("%s" % element)
        
with open('game_facts5.krf') as f5:
  lines_5 = f5.readlines()

for i in range(len(lines_5)):
  if "gameDeveloper" in lines_5[i]:
    temp = lines_5[i].split(' ')
    if ' ' in ' '.join(temp[2:len(temp)]):
      lines_5[i] = lines_5[i].replace(' ', '-').replace('Developer-', 'Developer ').replace('-"', ' "').replace('-', '').replace('"','')
    else:
      lines_5[i] = lines_5[i].replace('"','')

with open('game_facts_edited5.txt', 'w') as f: # change the number at game_ontology<number>
    for item in lines_5: # change the numbers in the list from 0:400 in the multiples of 400 till the len(new_list)
      for element in item:
        f.write("%s" % element)
        
with open('game_facts6.krf') as f6:
  lines_6 = f6.readlines()

for i in range(len(lines_6)):
  if "gameDeveloper" in lines_6[i]:
    temp = lines_6[i].split(' ')
    if ' ' in ' '.join(temp[2:len(temp)]):
      lines_6[i] = lines_6[i].replace(' ', '-').replace('Developer-', 'Developer ').replace('-"', ' "').replace('-', '').replace('"','')
    else:
      lines_6[i] = lines_6[i].replace('"','')

with open('game_facts_edited6.txt', 'w') as f: # change the number at game_ontology<number>
    for item in lines_6: # change the numbers in the list from 0:400 in the multiples of 400 till the len(new_list)
      for element in item:
        f.write("%s" % element)
        
with open('game_facts7.krf') as f7:
  lines_7 = f7.readlines()

for i in range(len(lines_7)):
  if "gameDeveloper" in lines_7[i]:
    temp = lines_7[i].split(' ')
    if ' ' in ' '.join(temp[2:len(temp)]):
      lines_7[i] = lines_7[i].replace(' ', '-').replace('Developer-', 'Developer ').replace('-"', ' "').replace('-', '').replace('"','')
    else:
      lines_7[i] = lines_7[i].replace('"','')

with open('game_facts_edited7.txt', 'w') as f: # change the number at game_ontology<number>
    for item in lines_7: # change the numbers in the list from 0:400 in the multiples of 400 till the len(new_list)
      for element in item:
        f.write("%s" % element)
