def fibonacci(n):
   if n <=1:
      return n

   else:
    
      return fibonacci(n-1)+fibonacci(n-2)
   
print("enter the nth term of fibonacci : 10 ","\n",fibonacci(9))

