def missing_number(n, numbers):
    x = [0] * (n + 1)
    for num in numbers:
        x[num] +=1

    for i in range (1, n+1):
        if x[i]==0:
            return i
       
       
numbers = [1, 2, 3, 4, 6, 7, 8]
n=8
print(missing_number(n,numbers))