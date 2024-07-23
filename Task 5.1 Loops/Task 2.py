def getlist (n):
    l=[]
    for i in range(n):
        lst=int(input("Enter the elements: "))
        l.append(lst)

    return l
n=int(input("Enter number of elements in list: "))
lst=getlist(n)
x=int(input("Enter number of outlier in list: "))

if (n < 4):
    print("Error As the length of list is less than 4")
else:
    slice_1=slice (x,len(lst)-x)
    print(lst[slice_1])