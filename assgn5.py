#Q1
year=int(input("Enter the year:"))
if(year%4==0 & year%400==0):
    print("The year is leap year")
elif(year%100!=0):
    print("Year is not leap year")
else:
    print("Year is not a leap year")

#Q2
lenth=int(input("Enter lenth:"))
breath=int(input("Enter breath:"))
if(lenth==breath):
    print("The dimension are of square")
else:
    print("The dimension are of rectangle")

#Q3
a=int(input("Enter age of first person:"))
b=int(input("Enter age of second person:"))
c=int(input("Enter age of third person:"))
if(a<b<c):
    print("The youngest is a %d"%(a))
elif(a>b>c):
    print("b youngest is %d" % (a))
else:
    print(" youngest is a%d" % (a))

#Q4
points=int(input("Enter the ponits scored:"))
if(points<=50):
    print("On prize")
elif(51<points<=150):
    print("Congrats!your prize is wooden dog")
elif(151<points<=180):
    print("Congrats!your prize is book")
else:
    print("Congrats your prize is choclates")

#Q5
q=int(input("Enter the cost:"))
if(q*100>1000):
    print("cost is:",q*100-0.10+q*100)
else:
    print(q*100)
