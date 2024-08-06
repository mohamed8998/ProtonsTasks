number=[1,2,3,4,5]
max1= max(number[0], number[1])
max2= min(number[0],number[1])
n = len(number)
for i in range(2,n):
    if number[i] > max1 :
        max2 = max1
        max1 = number[i]
    elif number[i] > max2 and \
        max1 !=number[i]: 
        max2 = number[i]
    elif max1 == max2 and \
        max2 != number[i]:
        max2 = number[i]
 
print("second largest number : ",\
      str(max2))