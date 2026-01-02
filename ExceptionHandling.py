# try:
#     print("try block is working")
#     print(userName)
# except:
#     print("errorrrrrr")
# else:
#     print("else block is working")
# finally:
#     print("finally block is working")



try:
    print("try block is working")
    # print(userName)
    # print("10" + 40)
except NameError:
    print("userName is not provided")
except ValueError:
    print("error!!! while adding str + int")
else:
    print("else block is working")
finally:
    print("finally block is working")




def divideNos(a, b):
  return a/b # An exception might raise here if b is 0 (ZeroDivisionError)
try:
   a = 20
   b = 0
   print('after division', divideNos(a, b)) 
   a = [1, 2, 3]
   print(a[3]) # An exception will raise here as size of array ‘a’ is 3 hence is accessible only up until 2nd index
 
# if IndexError exception is raised
except IndexError:            
   print('index error')
# if ZeroDivisionError exception is raised
except ZeroDivisionError as ex:
   print('zero division error',ex)