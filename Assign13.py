#Q1 ZeroDivisionError
try:
    a=3
    if a<4:
       a=a/(a-3)
       print(a)
except ZeroDivisionError:
       print("This is Zero Division Error")
       print(" ")
#OUTPUT:This is Zero Division Error
#2 Index Error
try:
    l=[1,2,3]
    print(l[3])
except IndexError:
    print("Index Error")
    print(" ")
#OUTPUT:Index error
#3 Raising Exception
#OUTPUT:An Excepition

#Ques4 Funtion which return a/b
#OUTPUT:-5.0
#a/b result in 0

#Ques 5
#Import Error
try:
    import man
except ImportError:
    print("File Not Found")
    print("Import Error")
    print(" ")
#Value Error
try:
    a=int(input("Enter no:"))
    b=10/a
    print(a)
except ValueError:
       print("Please Enter Only Integer")
       print("Value Error")
       print(" ")
#Index Error
try:
    l=[1,2,3]
    print(l[3])
except IndexError:
    print("Index Error")
    print(" ")
#Ques6
class AgeTooSmallError(Exception):
    pass
    try:
        a=int(input("Enter Age:"))
        if a<18:
          raise AgeTooSmallError
    except:
        print("Age is less than 18 ")

