#assinment6
#Q1
i=0
while(i<10):
    num=(input("Enter your no:"))
    print("enter no is:"+num)
    i=i+1

#Q2
i=0
while True:
      print("infinits")

#Q3
num=[]
sq=[]
for i in range(0,4):
   a=int(input("enter the num:"))
   num.append(a)
print(num)
for a in num:
    k=a*a
    sq.append(k)
print(sq)

#Q4
l=(1,2,"har",2.0)
a=[]
b=[]
c=[]
for i in l:
    if(type(i)==int):
        a.append(i)
    elif(type(i)==str):
        b.append(i)
    else:
        c.append(i)
print(a)
print(b)
print(c)

#Q5
even=[]
odd=[]
for i in range(1,101):
    if(i%2==0):
         even.append(i)
    else:
         odd.append(i)
print("Even numbers :",even)
print("Odd numbers :",odd)

#Q6
for i in range(0, 4):
    for j in range(0, i+1):
        print("* ",end="")
    print()

#Q7
a={'Name':'harman','Age':20,'Rollno':65}
for i in a:
    print(i,a[i])

#Q8
i=0
c=[]
while(i<5):
    a=int(input("Enter number:"))
    c.append(a)
    i=i+1
    a=int(input("Enter number to be searched:"))
for i in c:
        if(a==i):
            c.remove(i)
print(c)
