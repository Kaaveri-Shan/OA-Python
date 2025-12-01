##num = 54321
##count = 0
##
##for i in range(20):
##    if num != 0:
##        count += 1
##        num //= 10
##
##print(count)

num = 1234
rev = 0

for i in range(10):     # enough iterations
    if num != 0:
        digit = num % 10
        rev = rev * 10 + digit
        num //= 10
print(rev)

