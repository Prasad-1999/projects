from datetime import datetime

name = input("Enter the name:")

# List for items
lists = '''
Rice     Rs 20/kg
sugar    Rs 10/kg
salt     Rs 20/kg
oil      Rs 70/kg
kaju     Rs 60/kg
yippe    Rs 20/kg
Horlicks Rs 30/each
Daburred Rs 20/each
'''
# Declaration variables for loops
price = 0
pricelist = []
totalprice = 0
Finalfinalprice = 0
ilist = []
qlist = []
plist = []

# Rates for items
items = {'Rice': 20, 'sugar': 10, 'salt': 20, 'oil': 70,
         'kaju': 60, 'yippe': 20, 'Horlicks': 30, 'Daburred': 20}
option = int(input("for list of items press1:"))
if option == 1:  # To display the items
    print(lists)
for i in range(len(items)):  # To take items as list
    inp1 = int(input("If you want to buy press1 (or) press2 for Exit:"))
    if inp1 == 2:  # Exit
        break
    if inp1 == 1:  # Buy
        item = input("Enter your items:")  # items name
        quantity = int(input("Enter quantity:"))  # quantity of item
        if item in items.keys():  # If items in items dictionary
            price = quantity*(items[item])  # quantity*items price
            pricelist.append((item, quantity, items, price)
                             )  # quantity*Multiple items
            totalprice += price  # To display total price
            ilist.append(item)  # items list
            qlist.append(quantity)  # quantity list
            plist.append(price)  # prices list
            gst = (totalprice*2)/100  # The items gst
            finalamount = gst+totalprice  # To display finalamount
        else:
            print("you entered item not avaliable")  # if item not available
    else:
        print("you entered wrong number")  # If you entered wrong inp

inp = input("can i bill the items yes (or) no:")
if inp == "yes":  # yes for stop (or) hold
    pass
    if finalamount != 0:  # If final amount not equal to zero
        print(25*"=", "victorybazar", 25*"=")  # shop name
        print(28*" ", "Yeleswaram")  # village name
        print("Name", name, 30*" ", "Date:", datetime.now())  # date and time
        print(75*"-")
        print("s.no", 8*" ", 'items', 8*" ", 'Quantity',
              3*" ", 'price')  # sno,quantity,price
        for i in range(len(pricelist)):  # Pricelist of totallist
            # for sno,itemslist,quantitylist,pricelist
            print(i, 8*" ", 8*" ", ilist[i], 3*" ", qlist[i], plist[i])
        print(75*"-")
        print(50*" ", 'TotalAmount:', 'Rs', totalprice)  # totalprice display
        print("gst amount", 50*" ", 'Rs', gst)  # gst display
        print(75*"-")
        print(50*" ", "finalamount:", 'Rs', finalamount)  # finalamount display
        print(75*"-")
        print(50*" ", "Thanks for visiting")  # Message
        print(75*"-")
