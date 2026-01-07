print("1.Sum of even numbers from 1 to 20")
def exmp1():
    try:
        total = 0
        for i in range(1, 21):
            if i % 2 == 0:          
                total += i
    except Exception as e:
        print("Error:", e)
    else:
        print("Sum of even numbers:", total,)
    finally:
        print("Completed Question 1\n")

exmp1()


print("2.Multiplication table of 7 till 7 x 5 = 35")
def exmp2():
    try:
        for i in range(1, 6):
            if i > 0:              
                print("7 x", i, "=", 7 * i)
    except Exception as e:
        print("Error:", e)
    else:
        print("Table printed successfully")
    finally:
        print("Completed Question 2\n")

exmp2()


print("3.Sum of the digits of number")
def exmp3():
    try:
        num = 123456789
        s = 0
        while num > 0:
            if num >= 0:           
                digit = num % 10
                s += digit
                num //= 10
    except Exception as e:
        print("Error:", e)
    else:
        print("Sum of digits:", s)
    finally:
        print("Completed Question 3\n")

exmp3()


print("4.Check number is prime or not")
def exmp4():
    try:
        num = 7
        count = 0
        if num > 1:               
            for i in range(1, num + 1):
                if num % i == 0:
                    count += 1
        else:
            count = 0
    except Exception as e:
        print("Error:", e)
    else:
        if count == 2:
            print(num, "is a Prime number")
        else:
            print(num, "is Not a Prime number")
    finally:
        print("Completed Question 4\n")

exmp4()


print("5.Print star pattern 3 Star")
def exmp5():
    try:
        for i in range(1, 4):
            if i <= 3:             
                print("*" * i)
    except Exception as e:
        print("Error:", e)
    else:
        print("Star pattern printed")
    finally:
        print("Completed Question 5\n")

exmp5()
