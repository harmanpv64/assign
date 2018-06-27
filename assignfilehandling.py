#Q1
f=open("file1.txt",encoding="utf8")
a=(f.readlines())
a.reverse()
n=int(input("Enter number of line:"))
for i in range(0,n):
    print(a[i])
f.close()
print("")

#Q2
a="i"
f=open("file2.txt","r")
z=f.read()
m=z.split()
print(z.count(a))
print("")

#Q3
try:
  e=open("file1.txt", encoding="utf8")
  h=open("file3.txt","r+")
  h.writelines(wordstring)
  e.close()
  h.close()
  print("COPY OPERATION PERFORMED")
except Exception:
  print("")

#Q4
a= open("file4.txt", "r+")
b = open("file2.txt", "r+")
print("Combined Lines:")
for line1, line2 in zip(a,b):
    print(line2+line1,end="")
a.close()
a.close()
print("")

#Q5
import random
list=[]
sortedlist=[]
for i in range(0,10):
    list.append(random.randint(1,10))
f=open("file5.txt","w")
for s in list:
    r="".join(str(s))
    f.write(r)
f.close()
f1=open("file5.txt","r")
t=f1.read()
for u in t:
    if(u.isdigit()):
        v="".join(u)
        sortedlist.append(v)
sortedlist.sort()
w=open("sorted.txt","w")
w.write(str(sortedlist))
f.close()
print("")
print("Sorted")