def number_of_occurrences(number , n , x):
    first=-1
    last=-1
    for i in range(0,n):
        if (x != number[i]):
            continue
        if (first == -1):
            first =i
        last=i    

    if (first != -1):
        print("First index: ",(first),"\n Last index: ",(last))
    else:
        print("Not found")

number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
n = len(number)
x = 10
number_of_occurrences(number , n , x)

def Occurrences (lst, x):
    count = 0
    for element in lst:
        if (element == x):
            count = count + 1
    return count


lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
x = 10
print("Occurrences: " ,Occurrences(lst, x))
