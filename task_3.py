#######################
# * @author 44752     #
# * By Sang Tan Ngo   #
# * Stu id: 19037878  #
#######################

##############################################################
# * Python script to produce schedule shop & deli (database) #
##############################################################

#############
# * Task3 * #
#############

input1 = open(r'C:\VScode\DADSACode_and_pesudoCode\DATA CWK SHOPPING DATA WEEK 7 FILE A.csv')
input2 = open(r'C:\VScode\DADSACode_and_pesudoCode\DATA CWK SHOPPING DATA WEEK 7 FILE B.csv')


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

# addition of 2 dict
## Function to add 2 requirement
def add_dict(dic1,dic2):
    dic12 = {}
    for k,v in dic1.items():
        dic12[k] = v

    for k1,v1 in dic2.items():
        dic12[k1] = dic12.get(k1,0) + v1
    return dic12

### Function to get the remain product and it's quatity if the product do not
## sold in previous shop
def get_remain_dict(dic1,set1):
    remainDict = {}
    for element in set1:
        remainDict[element] = dic1[element]
    return remainDict


#### MAIN
###By and delever for the fisrt 5 Houses
Products = add_dict(HOUSE_dict['1A'],HOUSE_dict['1B'])
Products = add_dict(Products,HOUSE_dict['1C'])
Products = add_dict(Products,HOUSE_dict['1D'])
Products = add_dict(Products,HOUSE_dict['1E'])

print('Shopping Schedule\n')
print('Week7\n')
print('Monday\n')
print('Shop A, Shop B')
print()
print('Items,\n')
PLIST = []
for proName, proNum in Products.items():
    if proName in SHOP['A'] | SHOP['B']:
        print('%s %s' %(proName,proNum),end=', ')
        PLIST.append(proName)
print()
input("Press enter to continue…\n")

### Check the product do not have in SHOP-A and SHOP-B and need to buy in 2 ramining SHOPs
day2Prod_set = (x_1A | x_1B | x_1C | x_1D | x_1E) - (A | B)
day2Prod_dict = get_remain_dict(Products,day2Prod_set)

#### DAY2
Products_1 = add_dict(HOUSE_dict['2A'],HOUSE_dict['2B'])
Products_1 = add_dict(Products_1,HOUSE_dict['2C'])
Products_1 = add_dict(Products_1,HOUSE_dict['2D'])
Products_1 = add_dict(Products_1,HOUSE_dict['2E'])
Products = add_dict(Products_1,day2Prod_dict)

print('Tuesday\n')
print('Shop C, D')
print()
print('Items,\n')
for proName, proNum in Products.items():
    if proName in SHOP['C'] | SHOP['D']:
        print('%s %s' %(proName,proNum),end=', ')
print()

### Check the product do not have in SHOP-C and SHOP-D and need to buy in 2 ramining SHOPs
day2Prod_set = (x_2A | x_2B | x_2C | x_2D | x_2E) - (C | D)
day2Prod_dict = get_remain_dict(Products_1,day2Prod_set)


###DAY3
Products_1 = add_dict(HOUSE_dict['3A'],HOUSE_dict['3B'])
Products_1 = add_dict(Products_1,HOUSE_dict['3C'])
Products_1 = add_dict(Products_1,HOUSE_dict['3D'])
Products_1 = add_dict(Products_1,HOUSE_dict['3E'])
Products = add_dict(Products_1,day2Prod_dict)

print('Wednesday\n')
print('Shop A, B')
print()
print('Items,\n')
for proName, proNum in Products.items():
    if proName in SHOP['A'] | SHOP['B']:
        print('%s %s' %(proName,proNum),end=', ')
print()

### Check the product do not have in SHOP-C and SHOP-D and need to buy in 2 ramining SHOPs
day2Prod_set = (x_3A | x_3B | x_3C | x_3D | x_3E) - (A | B)
day2Prod_dict = get_remain_dict(Products_1,day2Prod_set)


###DAY4


print('Thursday\n')
print('Shop C, D')
print()
print('Items,\n')
for proName, proNum in day2Prod_dict.items():
    if proName in SHOP['C'] | SHOP['D']:
        print('%s %s' %(proName,proNum),end=', ')
print()



#### DELIVERY
print('Delivery Schedule\n')
print('Week 7\n')
print('Monday\n')
input("Press enter to continue…\n")
print('Tuesday\n')
print('1A, 1B, 1C, 1D, 1E\n')
input("Press enter to continue…\n")
print('Wednesday\n')
print('2A, 2B, 2C, 2D, 2E\n')
input("Press enter to continue…\n")
print('Thursday\n')
print('3A, 3B, 3C, 3D, 3E\n')


input1.close()
input2.close()
