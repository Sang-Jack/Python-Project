input1 = "read data from file DADSA_CWK_SHOPPING_DATA_WEEK_1_File_A.csv"
input2 = "readt data from file DATA_CWK_SHOPPING_DATA_WEEK_1_FILE_B.csv"


# STORE
# Read data from file and save the products which shop sell into 3 variable for
# 3 shops store
A = a set
B = a set
C = a set

for line in each line of input1:
    pName = field2 of line
    a = field 4 of line
    b = field 5 of line
    c = field 6 of line
    if a not empty:
        Add a into set A
    if b is not empty:
        Add b into set B
    if c is not empty:
        Add C into set C


## HOUSE
# Read data from file and save the products requirement of 7 houses in to 7 variables
# we save data into set to know the product needs and save into dictionary to know
# for each product, the quantity needed

x_1A,x_1B,x_1C,x_1D,x_1E,x_2C,x_3E = a set,a set,a set,a set,a set,a set,a set
y_1A,y_1B,y_1C,y_1D,y_1E,y_2C,y_3E = a Dictionany, a Dictionary, a Dictionany, a Dictionany, a Dictionany, a Dictionany, a Dictionany


for line1 in each line of input2:
    hName = field 1 of line1
    h1,h2,h3,h4,h5,h6,h7 = field2, field3, field4, field5, field6, field7, field8 of line
    if h1 is not empty:
        add h1 into set x_1A
        save value h1 into dictionany y_1A with key equal to hName
    if h2 is not empty:
        add h2 into set x_1B
        save value h2 into dictionany y_1B with key equal to hName
    if h3 is not empty:
        add h3 into set x_1C
        save value h3 into dictionany y_1C with key equal to hName
    if h4 is not empty:
        add h4 into set x_1D
        save value h4 into dictionany y_1D with key equal to hName
    if h5 is not empty:
        add h5 into set x_1E
        save value h5 into dictionany y_1E with key equal to hName
    if h6 is not empty:
        add h6 intot set x_2C
        save value h6 into dictionany y_2C with key equal to hName
    if h7 is not empty:
        add h7 intot set x_3E
        save value h7 into dictionany y_3E with key equal to hName


HOUSE_set = Dictionany with key is string of Name of House, and value is the house set
HOUSE_dict = Dictionany with key is string of Name of House, and value is the house Dictionany
SHOP is Dictionany with key is string of Name of Shop, and value is the shop Dictionany

### Function to chose Shop to go
## we choose 2 shops which can support maximum products of the requirement by check the
## by compare the number of products which 2 shop does not have for the predefined requirement
def choose_shop(set1,set2,set3=''):
    get HOUSE_set variable as global variable
    get SHOP variable as global variable
    if set3:
        allHouse = union of 3 input set
    else:
        allHouse = union of 2 input set - set1 and set2

    pNum = 100
    sList = a list

    for x in 3 shop key ('A', 'B','C'):
        for y in 3 shop key ('A', 'B','C':
            if x != y:
                tmp = union of (SHOP[x], SHOP[y])
                l = len(allHouse - tmp)
                if l < pNum:
                    pNum = l
                    sList = [x,y]
    return sList

# addition of 2 dict
## Function to add 2 requirement
def add_dict(dic1,dic2):
    dic12 = a Dictionany
    for k,v in key, value of dict1 :
        dic12[k] = v

    for k1,v1 in key, value of dict2:
        dic12[k1] = value if k1 not in dic12
        dic12[k1] = dic12[k1] + v1 already present in dic12
    return dic12


#### MAIN
###Delivery for first 3 houses bying from 2 stores
sl = choose_house('1A','1C','2C')
Products = add_dict(HOUSE_dict['1A'],HOUSE_dict['1C'])
Products = add_dict(Products,HOUSE_dict['2C'])
print into screen ('Shopping Schedule\n')
print into screen('Week1\n')
print into screen('Monday\n')
print into screen('Shop %s' %sl[0])
print into screen('Items,\n')
PLIST = []
for proName, proNum in Products.items():
    if proName in SHOP[sl[0]]:
        print('%s %s' %(proName,proNum),end=', ')
        PLIST.append(proName)

input into screen("Press enter to continue…\n")
print into screen('Tuesday\n')
print into screen('Shop %s' %sl[1])
print into screen('Items,\n')
for proName, proNum in Products.items():
    if not proName in PLIST and proName in SHOP[sl[1]]:
        print('%s %s' %(proName,proNum),end=', ')


###Delivery for next 2 houses bying from 2 stores
sl = choose_shop('1B','3E')
Products = add_dict(HOUSE_dict['1B'],HOUSE_dict['3E'])
print into screen('Wednesday\n')
print into screen('Shop %s' %sl[0])
print into screen()
print into screen('Items,\n')
PLIST = []
for proName, proNum in Products.items():
    if proName in SHOP[sl[0]]:
        print into screen('%s %s' %(proName,proNum),end=', ')
        PLIST.append(proName)

input into screen ("Press enter to continue…\n")
print into screen('Thursday\n')
print into screen('Shop %s' %sl[1])

print into screen('Items,\n')
for proName, proNum in Products.items():
    if not proName in PLIST and proName in SHOP[sl[1]]:
        print('%s %s' %(proName,proNum),end=', ')


###Delivery for last 2 houses bying from 2 stores
sl = choose_shop('1D','1E')
Products = add_dict(HOUSE_dict['1D'],HOUSE_dict['1E'])

print into screen('Friday\n')
print into screen('Shop %s' %sl[0])

PLIST = []
for proName, proNum in Products.items():
    if proName in SHOP[sl[0]]:
        print into screen('%s %s' %(proName,proNum),end=', ')
        PLIST.append(proName)

print into screen("Press enter to continue…\n")
print into screen('Saturday\n')
print into screen('Shop %s' %sl[1])

print into screen('Items,\n')
for proName, proNum in Products.items():
    if not proName in PLIST and proName in SHOP[sl[1]]:
        print into screen('%s %s' %(proName,proNum),end=', ')

print into screen('Delivery Schedule\n')
print into screen('Week 1\n')
print into screen('Monday\n')
print into screen("Press enter to continue…\n")
print into screen('Tuesday\n')
print into screen('1A, 1C, 2C\n')
print into screen("Press enter to continue…\n")
print into screen('Wednesday\n')
input into screen("Press enter to continue…\n")
print into screen('Thursday\n')
print into screen('1B, 3E\n')
input into screen("Press enter to continue…\n")
print into screen('Friday\n')
input into screen("Press enter to continue…\n")
print into screen('Saturday\n')
print into screen('1D','1E')


input1.close()
input2.close()
