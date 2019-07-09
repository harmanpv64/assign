#Q1
r=int(input("Enter num:"))
def area():
    return 3.14*r*r
a=area()
print(a)

#Q2
n=int(input("Enter num:"))
def prefect(n):
    sum=0
    for i in range(1,n):
        if(n%i==0):
            sum=sum+i
    if (sum == n):
        print("Prefect number")
    else:
        print("It is not prefect number")
prefect (6)

#Q3
def mul_table(n, i=1):
    print (n,'*',i,'=',n*i)
    if i != 10:
        mul_table(n,i+1)
mul_table(12)

#Q4

a=int(input("Enter base:"))
b=int(input("Enter power raised:"))
def power(a,b):
  if (b == 1):
    return a
  else:
    return a*power(a,b-1)
print ("result is %s"%power(a,b))

#Q5
n = int(input("Enter number:"))
def factorial(n):
    if(n <= 1):
        return 1
    else:
        return(n*factorial(n-1))
d={}
d={n:factorial(n)}
print(d)
