input1 = "read data from file DATA_CWK_SHOPPING_DATA_WEEK_7_FILE_A.csv"
input2 = "readt data from file DATA_CWK_SHOPPING_DATA_WEEK_7_FILE_B.csv"


# STORE
# Read data from file and save the products which shop sell into 3 variable for
# 3 shops store
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

### Function to get the remain product and it's quatity if the product do not
## sold in previous shop
def get_remain_dict(dic1,set1):
    remainDict = a Dictionany
    for element in set1:
        remainDict[element] = dic1[element]
    return remainDict


#### MAIN
###By and delever for the fisrt 5 Houses
Products = add_dict(HOUSE_dict['1A'],HOUSE_dict['1B'])
Products = add_dict(Products,HOUSE_dict['1C'])
Products = add_dict(Products,HOUSE_dict['1D'])
Products = add_dict(Products,HOUSE_dict['1E'])

print into screen('Shopping Schedule\n')
print into screen('Week7\n')
print into screen('Monday\n')
print into screen('Shop A, Shop B')
print into screen('Items,\n')
PLIST = []
for proName, proNum in Products.items():
    if proName in SHOP['A'] | SHOP['B']:
        print('%s %s' %(proName,proNum),end=', ')
        PLIST.append(proName)
input into screen("Press enter to continue…\n")

### Check the product do not have in SHOP-A and SHOP-B and need to buy in 2 ramining SHOPs
day2Prod_set = (x_1A | x_1B | x_1C | x_1D | x_1E) - (A | B)
day2Prod_dict = get_remain_dict(Products,day2Prod_set)

#### DAY2
Products_1 = add_dict(HOUSE_dict['2A'],HOUSE_dict['2B'])
Products_1 = add_dict(Products_1,HOUSE_dict['2C'])
Products_1 = add_dict(Products_1,HOUSE_dict['2D'])
Products_1 = add_dict(Products_1,HOUSE_dict['2E'])
Products = add_dict(Products_1,day2Prod_dict)

print into screen('Tuesday\n')
print into screen('Shop C, D')
print into screen('Items,\n')
for proName, proNum in Products.items():
    if proName in SHOP['C'] | SHOP['D']:
        print into scree('%s %s' %(proName,proNum),end=', ')

### Check the product do not have in SHOP-C and SHOP-D and need to buy in 2 ramining SHOPs
day2Prod_set = (x_2A | x_2B | x_2C | x_2D | x_2E) - (C | D)
day2Prod_dict = get_remain_dict(Products_1,day2Prod_set)


###DAY3
Products_1 = add_dict(HOUSE_dict['3A'],HOUSE_dict['3B'])
Products_1 = add_dict(Products_1,HOUSE_dict['3C'])
Products_1 = add_dict(Products_1,HOUSE_dict['3D'])
Products_1 = add_dict(Products_1,HOUSE_dict['3E'])
Products = add_dict(Products_1,day2Prod_dict)

print into screen('Wednesday\n')
print into screen('Shop A, B')
print into screen('Items,\n')
for proName, proNum in Products.items():
    if proName in SHOP['A'] | SHOP['B']:
        print into screen('%s %s' %(proName,proNum),end=', ')

### Check the product do not have in SHOP-C and SHOP-D and need to buy in 2 ramining SHOPs
day2Prod_set = (x_3A | x_3B | x_3C | x_3D | x_3E) - (A | B)
day2Prod_dict = get_remain_dict(Products_1,day2Prod_set)


###DAY4


print into screen('Thursday\n')
print into screen('Shop C, D')
print into screen('Items,\n')
for proName, proNum in day2Prod_dict.items():
    if proName in SHOP['C'] | SHOP['D']:
        print into screen('%s %s' %(proName,proNum),end=', ')


#### DELIVERY
print into screen('Delivery Schedule\n')
print into screen('Week 7\n')
print into screen('Monday\n')
input into screen ("Press enter to continue…\n")
print into screen('Tuesday\n')
print into screen('1A, 1B, 1C, 1D, 1E\n')
input into screen("Press enter to continue…\n")
print into screen('Wednesday\n')
print into screen('2A, 2B, 2C, 2D, 2E\n')
input into screen("Press enter to continue…\n")
print into screen('Thursday\n')
print into screen('3A, 3B, 3C, 3D, 3E\n')


input1.close()
input2.close()
