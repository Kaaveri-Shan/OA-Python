import os

print("1.Read")
file = open("data.txt", "r")
content = file.read()
print(content)
file.close()

print("2.Write")
file = open("data.txt", "w")
file.write("Welcome to Python File Handling")
file.close()

print("3.Append")
file = open("data.txt", "a")
file.write("\nThis is appended text")
file.close()

print("4.Reading line by line")
file = open("data.txt", "r")
for line in file:
    print(line)
file.close()

# print("5.Rename")
# os.rename("data.txt", "data1.txt")

# print("6.Remove")
# os.remove("data1.txt")

print("7.Make Directory")
os.mkdir("MyFolder")


