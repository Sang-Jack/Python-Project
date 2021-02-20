#######################
# * @author 44752     #
# * By Sang Tan Ngo   #
# * Stu id: 19037878  #
#######################

##############################################################
# * Python script to produce schedule shop & deli (database) #
##############################################################

#############
# * Task2 * #
#############

input1 = open(r'C:\VScode\DADSACode_and_pesudoCode\DATA CWK SHOPPING DATA WEEK 4 FILE A.csv')
input2 = open(r'C:\VScode\DADSACode_and_pesudoCode\DATA CWK SHOPPING DATA WEEK 4 FILE B.csv')


# STORE
# Read data from file and save the products which shop sell into 3 variable for
# 3 shops store
A = set()
B = set()
C = set()
D = set()

for line in input1.readlines()[1:]:
    line = line.strip()
    pName = line.split(',')[1]
    a,b,c,d = line.split(',')[3:]
    if a:
        A.add(pName)
    if b:
        B.add(pName)
    if c:
        C.add(pName)
    if d:
        D.add(pName)


## HOUSE
# Read data from file and save the products requirement of 7 houses in to 7 variables
# we save data into set to know the product needs and save into dictionary to know
# for each product, the quantity needed
x_1A,x_1B,x_1C,x_1D,x_1E = set(),set(),set(),set(),set()
y_1A,y_1B,y_1C,y_1D,y_1E = {},{},{},{},{}
x_2A,x_2B,x_2C,x_2D,x_2E = set(),set(),set(),set(),set()
y_2A,y_2B,y_2C,y_2D,y_2E = {},{},{},{},{}
x_3A,x_3B,x_3C,x_3D,x_3E = set(),set(),set(),set(),set()
y_3A,y_3B,y_3C,y_3D,y_3E = {},{},{},{},{}
for line1 in input2.readlines()[2:]:
    line1 = line1.strip()
    hName = line1.split(',')[0]
    h1,h2,h3,h4,h5,h6,h7,h8,h9,h10,h11,h12,h13,h14,h15 = line1.split(',')[-15:]
    if h1:
        x_1A.add(hName)
        y_1A[hName] = y_1A.get(hName,0) + int(h1)
    if h2:
        x_1B.add(hName)
        y_1B[hName] = y_1B.get(hName,0) + int(h2)
    if h3:
        x_1C.add(hName)
        y_1C[hName] = y_1C.get(hName,0) + int(h3)
    if h4:
        x_1D.add(hName)
        y_1D[hName] = y_1D.get(hName,0) + int(h4)
    if h5:
        x_1E.add(hName)
        y_1E[hName] = y_1E.get(hName,0) + int(h5)
    if h6:
        x_2A.add(hName)
        y_2A[hName] = y_2A.get(hName,0) + int(h6)
    if h7:
        x_2B.add(hName)
        y_2B[hName] = y_2B.get(hName,0) + int(h7)
    if h8:
        x_2C.add(hName)
        y_2C[hName] = y_2C.get(hName,0) + int(h8)
    if h9:
        x_2D.add(hName)
        y_2D[hName] = y_2D.get(hName,0) + int(h9)
    if h10:
        x_2E.add(hName)
        y_2E[hName] = y_2E.get(hName,0) + int(h10)
    if h11:
        x_3A.add(hName)
        y_3A[hName] = y_3A.get(hName,0) + int(h11)
    if h12:
        x_3B.add(hName)
        y_3B[hName] = y_3B.get(hName,0) + int(h12)
    if h13:
        x_3C.add(hName)
        y_3C[hName] = y_3C.get(hName,0) + int(h13)
    if h14:
        x_3D.add(hName)
        y_3D[hName] = y_3D.get(hName,0) + int(h14)
    if h15:
        x_3E.add(hName)
        y_3E[hName] = y_3E.get(hName,0) + int(h15)



HOUSE_set = {'1A':x_1A,'1B':x_1B,'1C':x_1C,'1D':x_1D,'1E':x_1E,'2A':x_2A,'2B':x_2B,
'2C':x_2C,'2D':x_2D,'2E':x_2E,'3A':x_3A,'3B':x_3B,'3C':x_3C,'3D':x_3D,'3E':x_3E}
HOUSE_dict = {'1A':y_1A,'1B':y_1B,'1C':y_1C,'1D':y_1D,'1E':y_1E,'2A':y_2A,'2B':y_2B,
'2C':y_2C,'2D':y_2D,'2E':y_2E,'3A':y_3A,'3B':y_3B,'3C':y_3C,'3D':y_3D,'3E':y_3E}

SHOP = {'A':A,'B':B,'C':C,'D':D}

### Function to chose Shop to go
## we choose 2 shops which can support maximum products of the requirement by check the
## by compare the number of products which 2 shop does not have for the predefined requirement
def choose_shop(set1,set2,set3,set4,set5,set6,set7,set8=''):
    global HOUSE_set
    global SHOP
    if set8:
        allHouse = HOUSE_set[set1] | HOUSE_set[set2] | HOUSE_set[set3] | HOUSE_set[set4]\
        | HOUSE_set[set5] | HOUSE_set[set6] | HOUSE_set[set7] | HOUSE_set[set8]
    else:
        allHouse = HOUSE_set[set1] | HOUSE_set[set2] | HOUSE_set[set3] | HOUSE_set[set4]\
        | HOUSE_set[set5] | HOUSE_set[set6] | HOUSE_set[set7]
    pNum = 70
    sList = []

    for x in ['A','B','C','D']:
        for y in ['A','B','C','D']:
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
###Delivery for first 8 houses bying from 2 stores
sl = choose_shop('1A','1C','2A','2D','2E','3A','3B','3E')
Products = add_dict(HOUSE_dict['1A'],HOUSE_dict['1C'])
for h in ['2A','2D','2E','3A','3B','3E']:
    Products = add_dict(Products,HOUSE_dict[h])

print('Shopping Schedule\n')
print('Week4\n')
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

###Delivery for first 7 houses bying from 2 stores
sl = choose_shop('1B','1D','1E','2B','2C','3C','3D')
Products = add_dict(HOUSE_dict['1B'],HOUSE_dict['1D'])
for h in ['1E','2B','2C','3C','3D']:
    Products = add_dict(Products,HOUSE_dict[h])

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
print()

print('Delivery Schedule\n')
print('Week 4\n')
print('Monday\n')
input("Press enter to continue…\n")
print('Tuesday\n')
print('1A, 1C, 2A, 2D, 2E, 3A, 3B, 3E\n')
input("Press enter to continue…\n")
print('Wednesday\n')
input("Press enter to continue…\n")
print('Thursday\n')
print('1B, 1D , 1E, 2B , 2C , 3C, 3D\n')


input1.close()
input2.close()
