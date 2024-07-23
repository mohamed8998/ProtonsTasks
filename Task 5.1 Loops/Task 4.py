l=[1,2,3,4,5]
ans=True
for i in range (len(l)-1):
    if l[i] >l[i+1]:
        ans = False
print(ans)
    