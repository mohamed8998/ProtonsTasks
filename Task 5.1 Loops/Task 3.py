n=int(input("Enter the number of elements: "))
l=[]
for i in range(n):
    number=int(input("Enter the elements : " ))
    l.append(number)
print(l)

cumsum=[]
x=0
for i in range(n):
  x+=l[i]
  cumsum.append(x)

print(cumsum)



