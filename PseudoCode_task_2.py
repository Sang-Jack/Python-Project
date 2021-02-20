input1 = "read data from file DATA_CWK_SHOPPING_DATA_WEEK_4_FILE_A.csv"
input2 = "readt data from file DATA_CWK_SHOPPING_DATA_WEEK_4_FILE_B.csv"


# STORE
# Read data from file and save the products which shop sell into 3 variable for
# 3 shops store
A = a set
B = a set
C = a set
D = a set

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
x_1A,x_1B,x_1C,x_1D,x_1E = a set,a set,a set,a set,a set
y_1A,y_1B,y_1C,y_1D,y_1E = a Dictionany, a Dictionary, a Dictionany, a Dictionany, a Dictionany
x_2A,x_2B,x_2C,x_2D,x_2E = a set,a set,a set,a set,a set
y_2A,y_2B,y_2C,y_2D,y_2E = a Dictionany, a Dictionary, a Dictionany, a Dictionany, a Dictionany
x_3A,x_3B,x_3C,x_3D,x_3E = a set,a set,a set,a set,a set
y_3A,y_3B,y_3C,y_3D,y_3E = a Dictionany, a Dictionary, a Dictionany, a Dictionany, a Dictionany

for line1 in input2.readlines()[2:]:
    hName = field 1 of line1
    h1,h2,h3,h4,h5,h6,h7,h8,h9,h10,h11,h12,h13,h14,h15 = field2, field3, field4, field5, field6, field7, field8,field9, field10, field11, field12, field13, field14, field15 of line
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
        add h6 intot set x_2A
        save value h6 into dictionany y_2A with key equal to hName
    if h7 is not empty:
        add h7 intot set x_2B
        save value h7 into dictionany y_2B with key equal to hName
    if h8 is not empty:
        add h8 intot set x_2C
        save value h8 into dictionany y_2C with key equal to hName
    if h9 is not empty:
        add h9 intot set x_2D
        save value h9 into dictionany y_2D with key equal to hName
    if h10 is not empty:
        add h9 intot set x_2E
        save value h10 into dictionany y_2E with key equal to hName
    if h11 is not empty:
        add h11 intot set x_3A
        save value h11 into dictionany y_3A with key equal to hName
    if h12 is not empty:
        add h12 intot set x_3B
        save value h12 into dictionany y_3B with key equal to hName
    if h13 is not empty:
        add h13 intot set x_3C
        save value h13 into dictionany y_3C with key equal to hName
    if h14 is not empty:
        add h14 intot set x_3D
        save value h14 into dictionany y_3D with key equal to hName
    if h15 is not empty:
        add h15 intot set x_3E
        save value h15 into dictionany y_3E with key equal to hName


HOUSE_set = Dictionany with key is string of Name of House, and value is the house set
HOUSE_dict = Dictionany with key is string of Name of House, and value is the house Dictionany
SHOP is Dictionany with key is string of Name of Shop, and value is the shop Dictionany


### Function to chose Shop to go
## we choose 2 shops which can support maximum products of the requirement by check the
## by compare the number of products which 2 shop does not have for the predefined requirement
def choose_shop(set1,set2,set3,set4,set5,set6,set7,set8=''):
    global HOUSE_set
    global SHOP
    if set8:
        allHouse = union of 8 input set
    else:
        allHouse = union of 7 input set - set1 to set2
    pNum = 70
    sList = []

    for x in 4 shop key ('A', 'B','C','D'):
        for y in 4 shop key ('A', 'B','C','D'):
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
###Delivery for first 8 houses bying from 2 stores
sl = choose_house('1A','1C','2A','2D','2E','3A','3B','3E')
Products = add_dict(HOUSE_dict['1A'],HOUSE_dict['1C'])
for h in ['2A','2D','2E','3A','3B','3E']:
    Products = add_dict(Products,HOUSE_dict[h])

print into screen ('Shopping Schedule\n')
print into screen ('Week4\n')
print into screen ('Monday\n')
print into screen ('Shop %s' %sl[0])
print into screen ('Items,\n')
PLIST = []
for proName, proNum in Products.items():
    if proName in SHOP[sl[0]]:
        print into screen ('%s %s' %(proName,proNum),end=', ')
        PLIST.append(proName)

input to screen("Press enter to continue…\n")
print into screen ('Tuesday\n')
print into screen ('Shop %s' %sl[1])

print into screen ('Items,\n')
for proName, proNum in Products.items():
    if not proName in PLIST and proName in SHOP[sl[1]]:
        print into screen ('%s %s' %(proName,proNum),end=', ')

###Delivery for first 7 houses bying from 2 stores
sl = choose_shop('1B','1D','1E','2B','2C','3C','3D')
Products = add_dict(HOUSE_dict['1B'],HOUSE_dict['1D'])
for h in ['1E','2B','2C','3C','3D']:
    Products = add_dict(Products,HOUSE_dict[h])

print into screen ('Wednesday\n')
print into screen ('Shop %s' %sl[0])
print into screen ('Items,\n')
PLIST = []
for proName, proNum in Products.items():
    if proName in SHOP[sl[0]]:
        print into screen ('%s %s' %(proName,proNum),end=', ')
        PLIST.append(proName))
input to screen("Press enter to continue…\n")
print into screen ('Thursday\n')
print into screen ('Shop %s' %sl[1])
print into screen ('Items,\n')
for proName, proNum in Products.items():
    if not proName in PLIST and proName in SHOP[sl[1]]:
        print into screen ('%s %s' %(proName,proNum),end=', ')

print into screen ('Delivery Schedule\n')
print into screen ('Week 4\n')
print into screen ('Monday\n')
input to screen("Press enter to continue…\n")
print into screen ('Tuesday\n')
print into screen ('1A, 1C, 2A, 2D, 2E, 3A, 3B, 3E\n')
input to screen("Press enter to continue…\n")
print into screen ('Wednesday\n')
input to screen("Press enter to continue…\n")
print into screen ('Thursday\n')
print into screen ('1B, 1D , 1E, 2B , 2C , 3C, 3D\n')


input1.close()
input2.close()
