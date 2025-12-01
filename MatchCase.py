amount = 6000
match amount:
    case 2500 :
        print("Your bill amount is 2500")
    case 2000:
        print("Your bill amount is 2000")
    case 1000:
        print("Your bill amount is 1000")
    case _ :
        print("mismatch")

totalMark = 470

match (True):
    case _ if (totalMark >= 400):
        print("pass")
    case _:
        print("fail")


age = 15

match True:
    case _ if 18 <= age <= 30:
        print("Young adult")
    case _ if age > 30:
        print("Adult")
    case _:
        print("Minor")

age1 = 22
income = 45000

match True:
    case _ if age1 < 25 and income < 50000:
        print("Low-income young adult")
    case _ if age1 >= 25 and income < 50000:
        print("Low-income adult")
    case _:
        print("Other category")
