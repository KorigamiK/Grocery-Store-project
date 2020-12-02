import mysql.connector as sql

con = sql.connect(
    host="localhost",
    user=input("enter user (root)"),
    password=input("enter password"),
)
print("{: ^40}".format("Origami"))
cur = con.cursor()

cur.execute("CREATE DATABASE IF NOT EXISTS kushagra_project")
cur.execute("use kushagra_project")
d1 = ["Items", "Price"]
q = "CREATE TABLE {2}(Sno int, {0} Varchar(60), {1} int, Item_Code varchar(50));"
cur.execute(q.format(d1[0], d1[1], "Menu_1"))
cur.execute("alter table Menu_1 add primary key(Item_Code);")
con.commit()

dict_1 = {
    "Lacinato Kale": 30,
    "Baby Spinach": 34,
    "Cauliflower": 23,
    "Avocados": 24,
    "Apples": 43,
    "Strawberries": 12,
    "Organic Eggs": 30,
    "Kefir": 34,
    "Almond Milk": 23,
    "Yogurt": 24,
    "Sheep's Milk": 43,
}


def rq(x):
    return '"{}"'.format(x)


for i in range(len(dict_1)):
    cur.execute(
        "INSERT into Menu_1 Values({0}, {1}, {2}, ".format(
            i, rq(list(dict_1.keys())[i]), dict_1[list(dict_1.keys())[i]]
        )
        + rq("#GS{:03d}".format(i))
        + ");"
    )
con.commit()

d2 = [
    "SNACKS",
    "Price",
]
dict_2 = {"Popcorn": 30, "Hummus": 34, "Dark Chocolate": 23, "Dried Fruit": 24}

q = "CREATE TABLE {2}(Sno int, {0} Varchar(60), {1} int, Item_Code varchar(50));"
cur.execute(q.format(d2[0], d2[1], "Menu_2"))
cur.execute("alter table Menu_2 add primary key(Item_Code);")

for i in range(len(dict_2)):
    cur.execute(
        "INSERT into Menu_2 Values({0}, {1}, {2}, ".format(
            i, rq(list(dict_2.keys())[i]), dict_2[list(dict_2.keys())[i]]
        )
        + rq("#GS{:03d}".format(i + 11))
        + ");"
    )
con.commit()

quer1 = """CREATE TABLE cust_details(
CustID Varchar(30),
Name varchar(20),
Address varchar (40),
EmailID varchar(35),
pincode int,
PhoneNO varchar(40),
pass varchar(50)
);"""
cur.execute(quer1)
cur.execute("alter table cust_details add primary key(CustID);")
cur.execute(
    'insert into cust_details values("ADMIN", "origami", "asdf", "admin@asdf.com", 1234, "100", "origami");'
)
cur.execute(
    "create table gifts(Sno int, CustID varchar(60), Voucher_type varchar(60), Value int);"
)
cur.execute("alter table gifts add primary key(CustID);")
con.commit()
