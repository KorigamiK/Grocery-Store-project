import mysql.connector as sq
from prettytable import PrettyTable as pt
import math
e=input("New setup ? y/n:")
print()
if e!='y':
    con = sq.connect(host="localhost", user="root",database="project")
else:
    con = sq.connect(host="localhost", user=input("Enter user (root): "), password=input('Enter password: '), database="kushagra_project")

cur = con.cursor()

def table_print(y):
    cur.execute("Select * from {}".format(y))
    a = cur.fetchall()
    x = pt()
    cur.execute("desc {}".format(y))
    f = cur.fetchall()
    d = []
    for i in f:
        d += [list(i)[0]]

    g = [[] for i in range(len(a[0]))]
    for i in list(a):
        for j, k in enumerate(list(i)):
            g[j].append(k)
    for i, j in enumerate(g):
        x.add_column(d[i], j)
    x.title = y
    return x


# cur.execute("select * from Menu_1;")
# a=cur.fetchall()
# print(a)

ask = input("Are you already registered ? (Y/N)")
print()
a = 1
b = 1
while b == 1:
    if ask == "Y" or ask == "y":
        print("Please give your login details\n")
        # verifying the userid
        while a == 1:
            enterid = str(input("Enter your userid "))
            print()
            tup = (enterid,)
            cur.execute("Select CustID from cust_details")
            varc = cur.fetchall()
            # varc is a list of all CustID stored in Cust_details in tuple databases
            for c in varc:
                if c == tup:
                    print("UserID found\n")
                    a = 2
                    break
            else:
                print("No userid found\n")

        psswd = input('Enter you password: ')
        print()
        check = (enterid, psswd)
        cur.execute("Select CustID, pass from cust_details")
        varp = cur.fetchall()
        a = 1
        h = 1
        while a == 1:
            for j in varp:
                if j == check:
                    print('Password verified\n')
                    a = 2
                    break
            else:
                print("Incorrect Password\n")
                psswd = input("Please type the correct password : ")
                check = (enterid, psswd)
                h += 1
                if h > 2:
                    print("You entered the wrong password too many times, create a new id\n")
                    ask = "n"
        b = 2

    elif ask == "N" or ask == "n":
        print("Enter your details\n")
        name = input('Enter your name : ')
        print()
        phoneno = str(input('Enter your phone number : '))
        print()

        while True:
            if len(phoneno) == 10:
                print('phone number verified')
                break
            else:
                print('Invalid Phone No. :)(Your Phone number should contain 10 digits)\n')
                phoneno = str(input('Please enter a valid Phone No : '))
                print()
        email = input('Enter your email address : ')
        print()
        add = input('Enter your address : ')
        print()
        while True:
            pincode = input('Enter the pincode of your area : ')
            try:
                int(pincode)
                break
            except:
                print('enter correct pincode')            
        print()

        user_id = "GS" + name[0:3] + phoneno[0:4]
        print('Your Grocery Express Userid is', user_id+'\n')
        psswd = input('Enter your password: ')
        print()
        recheck = input('Please re-enter your password:')

        while True:
            if psswd == recheck:
                print('Password verified\n')
                break
            else:
                print('please renter your password\n')
                recheck = input('Renter your password: ')
                print()
        # Entering the data given by user into the Database
        query1 = ("Insert into cust_details values(%s, %s, %s, %s, %s, %s, %s)")
        cur.execute(query1, (user_id, name, add, email, pincode, phoneno, psswd))
        con.commit()  # veeeery important
        b = 2
    else:
        ask = input("Are you already registered ? (Please Enter either Y or N) ")
        print()
try:
    cur.execute('select name from cust_details where CustID="{}"'.format(enterid))
    z = cur.fetchall()
    name = z[0][0]
except:
    name=user_id

print("Hi! {}".format(name),'\n')
input("Please press enter")
print()
print(table_print("Menu_1"))
print()
print(table_print("Menu_2"))

cur.execute("select Items, Price from Menu_1;")
dict_1 = dict(cur.fetchall())
cur.execute("select SNACKS, Price from Menu_2;")
dict_2 = dict(cur.fetchall())

list_1 = []
ans = 'y'


def check(x):
    z = list(x.capitalize())
    w = ""
    for i in range(len(z)):
        try:
            if i == x.index(" "):
                z[i + 1] = z[i + 1].upper()
        except:
            continue
    for j in range(len(z)):
        w += z[j]
    x = w
    if x in dict_1:
        list_1.append(x)
    elif x in dict_2:
        list_1.append(x)
    else:
        print("Sorry sir, We do not have ", x, ' in stock yet, Leave your requests in the feedback section.\n')

while True:
    while ans == 'y':
        o = input("\nWhat do you want to purchase, Sir?  :-  ")
        print()
        check(o)
        ans = input("Want something else, Sir(Y/N) : ")
        print()
    else:
        yes=input('Do you want to continue shopping ? (y/n): ')
        if yes!='y':
            break
        else:
            ans=yes
            pass
print()

print(list_1)

print()


def quant(y):
    for i in range(len(y)):
        a = int(input('Quantity of item ' + y[i] + " "))
        print()
        list_2[i] = a


def feed():
    a = input("Please tell us about your visit, suggestions, complaints or requests : \n")
    print("Thank you for you cooperation, we will get back to you as soon as possible ")


def truncate(number, digits) -> float:
    stepper = 10.0 ** digits
    return math.trunc(stepper * number) / stepper


if len(list_1) != 0:

    list_2 = list(list_1)
    quant(list_1)

    list_3 = [[[] for b in range(6)] for a in range(len(list_1) + 1)]

    list_3[0][0] = "S. NO."
    list_3[0][1] = "NAME OF ITEMS (Price Per Item)"
    list_3[0][2] = "QUANTITY"
    list_3[0][3] = "TAX"
    list_3[0][4] = "PRICE"
    list_3[0][5] = "EFFECTIVE PRICE"

    sum = 0
    z = 18
    for n in range(1, len(list_1) + 1):

        list_3[n][0] = str(n)
        list_3[n][1] = str(list_1[n - 1])
        list_3[n][2] = list_2[n - 1]
        list_3[n][3] = str(z) + "%"
        try:
            str(list_1[n - 1]) in dict_1
            list_3[n][4] = list_2[n - 1] * dict_1[str(list_1[n - 1])]
            sum += list_2[n - 1] * dict_1[str(list_1[n - 1])] * (1 + (18 / 100))
            list_3[n][5] = "Rs." + str(list_2[n - 1] * dict_1[str(list_1[n - 1])] * (1 + (18 / 100)))[:13]
        except:
            list_3[n][4] = list_2[n - 1] * dict_2[str(list_1[n - 1])]
            sum += list_2[n - 1] * dict_2[str(list_1[n - 1])] * (1 + (18 / 100))
            list_3[n][5] = "Rs." + str(list_2[n - 1] * dict_2[str(list_1[n - 1])] * (1 + (18 / 100)))[:13]

    y = pt()

    b = []

    for i in range(len(list_3[0])):
        b.append(list_3[0][i])
    y.field_names = b
    
    for i in range(1,len(list_3)):
        try:
            list_3[i][1]+=' ({})'.format(str(dict_1[list_1[i-1]]))
        except:
            list_3[i][1]+=' ({})'.format(str(dict_2[list_1[i-1]]))
            
    for k in range(1, len(list_3)):
        y.add_row(list_3[k])

    print(y)
    print()
    print('Your total bill is Rs.', round(sum))
    print()
    print("Thank you for the visit", name+'\n')
    print("Please Enter feedback and you can cllect your bill \n ")
    with open("{}_bill.txt".format(name), "w") as f:
        f.writelines(['{:_^88s}\n\n'.format('Thank you for shopping with us !'),str(y)+'\n','The total payable amount is: '+str(round(sum))])
    feed()
print('\nLookin\' forward to you next visit !')