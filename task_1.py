#######################
# * @author 44752     #
# * By Sang Tan Ngo   #
# * Stu id: 19037878  #
#######################

##############################################################
# * Python script to produce schedule shop & deli (database) #
##############################################################

#############
# * Task1 * #
#############

input1 = open(r'C:\VScode\DADSACode_and_pesudoCode\DADSA CWK SHOPPING DATA WEEK 1 File A.csv')
input2 = open(r'C:\VScode\DADSACode_and_pesudoCode\DATA CWK SHOPPING DATA WEEK 1 FILE B.csv')

# STORE
# Read data from file and save the products which shop sell into 3 variable for
# 3 shops store
A = set()
B = set()
C = set()

for line in input1.readlines()[1:]:
    line = line.strip()
    pName = line.split(',')[1]
    a,b,c = line.split(',')[3:]
    if a:
        A.add(pName)
    if b:
        B.add(pName)
    if c:
        C.add(pName)

## HOUSE
# Read data from file and save the products requirement of 7 houses in to 7 variables
# we save data into set to know the product needs and save into dictionary to know
# for each product, the quantity needed
x_1A,x_1B,x_1C,x_1D,x_1E,x_2C,x_3E = set(),set(),set(),set(),set(),set(),set()
y_1A,y_1B,y_1C,y_1D,y_1E,y_2C,y_3E = {},{},{},{},{},{},{}


HOUSE_set = {'1A':x_1A,'1B':x_1B,'1C':x_1C,'1D':x_1D,'1E':x_1E,'2C':x_2C,'3E':x_3E}
HOUSE_dict = {'1A':y_1A,'1B':y_1B,'1C':y_1C,'1D':y_1D,'1E':y_1E,'2C':y_2C,'3E':y_3E}
SHOP = {'A':A,'B':B,'C':C}

### Function to chose Shop to go
## I choose 2 shops which can support maximum products of the requirement by check the
## by compare the number of products which 2 shop does not have for the predefined requirement
def choose_shop(set1,set2,set3=''):
    global HOUSE_set
    global SHOP
    if set3:
        allHouse = HOUSE_set[set1] | HOUSE_set[set2] | HOUSE_set[set3]
    else:
        allHouse = HOUSE_set[set1] | HOUSE_set[set2]
    pNum = 40
    sList = []

    for x in ['A','B','C']:
        for y in ['A','B','C']:
            if x != y:
                tmp = SHOP[x] | SHOP[y]
                l = len(allHouse - tmp)
                if l < pNum:
                    pNum = l
                    sList = [x,y]
    return sList

# addition of 2 dict
## Function to add 2 requirement
def add_dict(dic1,dic2):
    dic12 = {}
    for k,v in dic1.items():
        dic12[k] = v

    for k1,v1 in dic2.items():
        dic12[k1] = dic12.get(k1,0) + v1
    return dic12


#### MAIN
###Delivery for first 3 houses bying from 2 stores
sl = choose_shop('1A','1C','2C')
Products = add_dict(HOUSE_dict['1A'],HOUSE_dict['1C'])
Products = add_dict(Products,HOUSE_dict['2C'])

print('Shopping Schedule\n')
print('Week1\n')
print('Monday\n')
print('Shop %s' %sl[0])
print()
print('Items,\n')
PLIST = []
for proName, proNum in Products.items():
    if proName in SHOP[sl[0]]:
        print('%s %s' %(proName,proNum),end=', ')
        PLIST.append(proName)
print()

input("Press enter to continue…\n")
print('Tuesday\n')
print('Shop %s' %sl[1])
print()
print('Items,\n')
for proName, proNum in Products.items():
    if not proName in PLIST and proName in SHOP[sl[1]]:
        print('%s %s' %(proName,proNum),end=', ')
print()

###Delivery for next 2 houses bying from 2 stores
sl = choose_shop('1B','3E')
Products = add_dict(HOUSE_dict['1B'],HOUSE_dict['3E'])
print('Wednesday\n')
print('Shop %s' %sl[0])
print()
print('Items,\n')
PLIST = []
for proName, proNum in Products.items():
    if proName in SHOP[sl[0]]:
        print('%s %s' %(proName,proNum),end=', ')
        PLIST.append(proName)
print()

input("Press enter to continue…\n")
print('Thursday\n')
print('Shop %s' %sl[1])
print()
print('Items,\n')
for proName, proNum in Products.items():
    if not proName in PLIST and proName in SHOP[sl[1]]:
        print('%s %s' %(proName,proNum),end=', ')
print()

###Delivery for last 2 houses bying from 2 stores
sl = choose_shop('1D','1E')
Products = add_dict(HOUSE_dict['1D'],HOUSE_dict['1E'])

print('Friday\n')
print('Shop %s' %sl[0])
print()

PLIST = []
for proName, proNum in Products.items():
    if proName in SHOP[sl[0]]:
        print('%s %s' %(proName,proNum),end=', ')
        PLIST.append(proName)
print()

input("Press enter to continue…\n")
print('Saturday\n')
print('Shop %s' %sl[1])
print()
print('Items,\n')
for proName, proNum in Products.items():
    if not proName in PLIST and proName in SHOP[sl[1]]:
        print('%s %s' %(proName,proNum),end=', ')
print()

print('Delivery Schedule\n')
print('Week 1\n')
print('Monday\n')

input("Press enter to continue…\n")
print('Tuesday\n')
print('1A, 1C, 2C\n')

input("Press enter to continue…\n")
print('Wednesday\n')

input("Press enter to continue…\n")
print('Thursday\n')
print('1B, 3E\n')

input("Press enter to continue…\n")
print('Friday\n')

input("Press enter to continue…\n")
print('Saturday\n')
print('1D','1E')


input1.close()
input2.close()
