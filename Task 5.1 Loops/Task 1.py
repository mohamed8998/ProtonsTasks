def gitlist(n):
    l=[]
    for i in range(n):
     lst =input("Enter the elements: ")
     l.append(lst)

    return l
n1=int(input("Enter number of elements in list: "))
lst=gitlist(n1)

ele=""

for i in range (n1):
   if i == n1-1 and n1>1:
      ele+= " and "
   elif i>0 :
      ele += " ,"
   
   ele+=lst[i]
     
print(ele)
