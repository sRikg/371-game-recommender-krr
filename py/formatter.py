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

for i in range(len(lines_1)):
  if 'gameDeveloper' in lines_1[i]:
    temp = lines_1[i].replace(')\n', "").split(" ")
    lines_1[i] = ' '.join(temp[0:2]) + ' gameDeveloper_' + temp[2] + ')\n'

  if 'gamePublisher' in lines_1[i]:
    temp = lines_1[i].replace(')\n', "").split(" ")
    lines_1[i] = ' '.join(temp[0:2]) + ' gamePublisher_' + temp[2] + ')\n'

  if 'gameLanguage' in lines_1[i]:
    temp = lines_1[i].replace(')\n', "").split(" ")
    lines_1[i] = ' '.join(temp[0:2]) + ' gameLanguage_' + temp[2] + ')\n'

  if 'gameGenre' in lines_1[i]:
    temp = lines_1[i].replace(')\n', "").split(" ")
    lines_1[i] = ' '.join(temp[0:2]) + ' gameGenre_' + temp[2] + ')\n'

with open('game_facts1.txt', 'w') as f:
    for item in lines_1:
      for element in item:
        f.write("%s" % element)
        
for i in range(len(lines_2)):
  if 'gameDeveloper' in lines_2[i]:
    temp = lines_2[i].replace(')\n', "").split(" ")
    lines_2[i] = ' '.join(temp[0:2]) + ' gameDeveloper_' + temp[2] + ')\n'

  if 'gamePublisher' in lines_2[i]:
    temp = lines_2[i].replace(')\n', "").split(" ")
    lines_2[i] = ' '.join(temp[0:2]) + ' gamePublisher_' + temp[2] + ')\n'

  if 'gameLanguage' in lines_2[i]:
    temp = lines_2[i].replace(')\n', "").split(" ")
    lines_2[i] = ' '.join(temp[0:2]) + ' gameLanguage_' + temp[2] + ')\n'

  if 'gameGenre' in lines_2[i]:
    temp = lines_2[i].replace(')\n', "").split(" ")
    lines_2[i] = ' '.join(temp[0:2]) + ' gameGenre_' + temp[2] + ')\n'

with open('game_facts2.txt', 'w') as f:
    for item in lines_2:
      for element in item:
        f.write("%s" % element)
        
for i in range(len(lines_3)):
  if 'gameDeveloper' in lines_3[i]:
    temp = lines_3[i].replace(')\n', "").split(" ")
    lines_3[i] = ' '.join(temp[0:2]) + ' gameDeveloper_' + temp[2] + ')\n'

  if 'gamePublisher' in lines_3[i]:
    temp = lines_3[i].replace(')\n', "").split(" ")
    lines_3[i] = ' '.join(temp[0:2]) + ' gamePublisher_' + temp[2] + ')\n'

  if 'gameLanguage' in lines_3[i]:
    temp = lines_3[i].replace(')\n', "").split(" ")
    lines_3[i] = ' '.join(temp[0:2]) + ' gameLanguage_' + temp[2] + ')\n'

  if 'gameGenre' in lines_3[i]:
    temp = lines_3[i].replace(')\n', "").split(" ")
    lines_3[i] = ' '.join(temp[0:2]) + ' gameGenre_' + temp[2] + ')\n'

with open('game_facts3.txt', 'w') as f:
    for item in lines_3:
      for element in item:
        f.write("%s" % element)

for i in range(len(lines_4)):
  if 'gameDeveloper' in lines_4[i]:
    temp = lines_4[i].replace(')\n', "").split(" ")
    lines_4[i] = ' '.join(temp[0:2]) + ' gameDeveloper_' + temp[2] + ')\n'

  if 'gamePublisher' in lines_4[i]:
    temp = lines_4[i].replace(')\n', "").split(" ")
    lines_4[i] = ' '.join(temp[0:2]) + ' gamePublisher_' + temp[2] + ')\n'

  if 'gameLanguage' in lines_4[i]:
    temp = lines_4[i].replace(')\n', "").split(" ")
    lines_4[i] = ' '.join(temp[0:2]) + ' gameLanguage_' + temp[2] + ')\n'

  if 'gameGenre' in lines_4[i]:
    temp = lines_4[i].replace(')\n', "").split(" ")
    lines_4[i] = ' '.join(temp[0:2]) + ' gameGenre_' + temp[2] + ')\n'

with open('game_facts4.txt', 'w') as f:
    for item in lines_4:
      for element in item:
        f.write("%s" % element)

for i in range(len(lines_5)):
  if 'gameDeveloper' in lines_5[i]:
    temp = lines_5[i].replace(')\n', "").split(" ")
    lines_5[i] = ' '.join(temp[0:2]) + ' gameDeveloper_' + temp[2] + ')\n'

  if 'gamePublisher' in lines_5[i]:
    temp = lines_5[i].replace(')\n', "").split(" ")
    lines_5[i] = ' '.join(temp[0:2]) + ' gamePublisher_' + temp[2] + ')\n'

  if 'gameLanguage' in lines_5[i]:
    temp = lines_5[i].replace(')\n', "").split(" ")
    lines_5[i] = ' '.join(temp[0:2]) + ' gameLanguage_' + temp[2] + ')\n'

  if 'gameGenre' in lines_5[i]:
    temp = lines_5[i].replace(')\n', "").split(" ")
    lines_5[i] = ' '.join(temp[0:2]) + ' gameGenre_' + temp[2] + ')\n'

with open('game_facts5.txt', 'w') as f:
    for item in lines_5:
      for element in item:
        f.write("%s" % element)
        
for i in range(len(lines_6)):
  if 'gameDeveloper' in lines_6[i]:
    temp = lines_6[i].replace(')\n', "").split(" ")
    lines_6[i] = ' '.join(temp[0:2]) + ' gameDeveloper_' + temp[2] + ')\n'

  if 'gamePublisher' in lines_6[i]:
    temp = lines_6[i].replace(')\n', "").split(" ")
    lines_6[i] = ' '.join(temp[0:2]) + ' gamePublisher_' + temp[2] + ')\n'

  if 'gameLanguage' in lines_6[i]:
    temp = lines_6[i].replace(')\n', "").split(" ")
    lines_6[i] = ' '.join(temp[0:2]) + ' gameLanguage_' + temp[2] + ')\n'

  if 'gameGenre' in lines_6[i]:
    temp = lines_6[i].replace(')\n', "").split(" ")
    lines_6[i] = ' '.join(temp[0:2]) + ' gameGenre_' + temp[2] + ')\n'

with open('game_facts6.txt', 'w') as f:
    for item in lines_6:
      for element in item:
        f.write("%s" % element)

for i in range(len(lines_7)):
  if 'gameDeveloper' in lines_7[i]:
    temp = lines_7[i].replace(')\n', "").split(" ")
    lines_7[i] = ' '.join(temp[0:2]) + ' gameDeveloper_' + temp[2] + ')\n'

  if 'gamePublisher' in lines_7[i]:
    temp = lines_7[i].replace(')\n', "").split(" ")
    lines_7[i] = ' '.join(temp[0:2]) + ' gamePublisher_' + temp[2] + ')\n'

  if 'gameLanguage' in lines_7[i]:
    temp = lines_7[i].replace(')\n', "").split(" ")
    lines_7[i] = ' '.join(temp[0:2]) + ' gameLanguage_' + temp[2] + ')\n'

  if 'gameGenre' in lines_7[i]:
    temp = lines_7[i].replace(')\n', "").split(" ")
    lines_7[i] = ' '.join(temp[0:2]) + ' gameGenre_' + temp[2] + ')\n'

with open('game_facts7.txt', 'w') as f:
    for item in lines_7:
      for element in item:
        f.write("%s" % element)
        
with open('game_ontology_additional.krf') as fx:
  lines_additional = fx.readlines()
  
for i in range(len(lines_additional)):
  if 'Language' in lines_additional[i]:
    temp = lines_additional[i].replace(')\n', "").split(" ")
    lines_additional[i] = '(isa ' + 'gameLanguage_' + temp[1] + ' Language)\n'

  if 'ComputerGameProgramTypeByGenre' in lines_additional[i]:
    temp = lines_additional[i].replace(')\n', "").split(" ")
    lines_additional[i] = '(isa ' + 'gameGenre_' + temp[1] + ' ComputerGameProgramTypeByGenre)\n'

  if i > 54 and i < 461 and 'SoftwareVendor' in lines_additional[i]:
    temp = lines_additional[i].replace(')\n', "").split(" ")
    lines_additional[i] = '(isa ' + 'gamePublisher_' + temp[1] + ' SoftwareVendor)\n'

  if i > 462 and 'SoftwareVendor' in lines_additional[i]:
    temp = lines_additional[i].replace(')\n', "").split(" ")
    lines_additional[i] = '(isa ' + 'gameDeveloper_' + temp[1] + ' SoftwareVendor)\n'


with open('game_ontology_additional.txt', 'w') as f:
    for item in lines_additional:
      for element in item:
        f.write("%s" % element)
