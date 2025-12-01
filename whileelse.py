for i in range(5):
    if i == 2:
        continue
    print(i)

for i in range(5):
    if i == 2:
        break
    print(i)


for i in range(5):
    if i == 2:
        break
    print(i)
else:
    print("else block is working")



count = 5
startValue = 1


for i in range(5):
    pass

while startValue <= count:
    print(startValue)
    startValue += 1
else:
    print("Else block executed (no break encountered).")


while startValue <= count:
    if startValue == 3:
        print(startValue)
    startValue += 1