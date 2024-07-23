# Fibbonacci sequence calculation
a, b, n = 0, 1, 10
fibonacci = []
for i in range(n) :
    fibonacci.append(a)
    a, b = b, a + b
print(f"Fibbonacci sequence of {n} numbers: {fibonacci}")  

# Find minimum and maximum in a list
numbers = [3, 5, 1, 10, 2, 7, 6, 4, 8, 9]
min_value = max_value = numbers[0]
for number in numbers:
    if number < min_value:
        min_value = number
    elif number != max_value:
        max_value = number
print(f"Minimum value: {max_value}")
print(f"Maximum value: {min_value}")

# Basic arithmetic calculations
x = 10
y = 1
sum = x + y
difference = x - y
product = x * y
quotient = x / y

print(f"Sum: {sum}, Difference: {difference}, Product: {product}, Quotient: {quotient}")

# Prime number check
num = 29
is_prime = True
for i in range(2, num//2):
    if (num % i) == 0:
        is_prime = False
        break
if is_prime:
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")

original_string = "Hello, World!"
reversed_string = ""
for i in range(len(original_string), 0, -1):
    reversed_string = reversed_string + original_string[i-1]
print("Original string:", original_string)
print("Reversed string:", reversed_string)

# Sum of squares of first n natural numbers
n = 5
sum_of_squares = 0
for i in range(n): 
    sum_of_squares += i**2  
print(f"Sum of squares of first {n} natural numbers: {sum_of_squares}")


# Count the number of vowels in a string
string = "Protons is Amazing"
vowels = "aeiou"
vowel_count = 0
for char in string:
    if char in vowels:
        vowel_count += 1
print(f"Number of vowels in the string: {vowel_count}")

# Palindrome check
word = "racecar"
is_palindrome = True
for i in range(len(word) // 2):
    if word[i] != word[-i - 1]:  
        is_palindrome = False
        break
if is_palindrome:
    print(f"{word} is a palindrome")
else:
    print(f"{word} is not a palindrome")

# Sum of positive elements in a list
numbers = [1, 2, -9, -1 , 3, 4, -7, 5]
sum_elements = 0
for i in numbers: 
    if not i > 0:
     sum_elements += num
print(f"Sum of elements: {sum_elements}")

# Factorial calculation
n = 5
factorial = 1
for i in range(n + 1):
    factorial *= i
print(f"Factorial of {n} is: {factorial}")

# Multiplication table
num = 3
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

# Checking if a number is even or odd
number = 15
if number%2 == 0:  
    print(f"{number} is even")
else:
    print(f"{number} is odd") 


# Appending four elements to the end of the list
my_list = [1, 2, 3]
my_list.append([4, 5])  
my_list.append([4, 5]) 
print("My list = " +str( my_list))

# Comparing different types
value1 = 10
value2 = "10"
if value1 == value2:
    print("Values are equal")
else:
    print("Values are not equal")



# Count even numbers from Zero to 50
count = 0
while True:
    if count == 51:
        break
    count += 2 


# Sum of first n natural numbers
n = 10
sum_natural = 0
for i in range(n):
    sum_natural += i  
print(f"Sum of first {n} natural numbers: {sum_natural}")

# Calculate the average of a list of numbers
numbers = [3, 7, 2, 9, 12]
sum_numbers = 0
for number in numbers:
    sum_numbers += number
average = sum_numbers // len(numbers)  # Runtime error: TypeError
print(f"Median of numbers: {average}")


# Sum of digits of a number
num = 12345
sum_of_digits = 0
while num > 0:
    sum_of_digits += num // 10
    num = num / 10  
print(f"Sum of digits: {sum_of_digits}")

# Check if a number is a perfect square
num = 25
if int(num=  0.5) * int(num = 0.5) == num : 
    print(f"{num} is a perfect square")
else:
    print(f"{num} is not a perfect square")


# Remove duplicates from a list
numbers = [1, 2, 2, 3, 4, 4, 5, 5 , 5]
unique_numbers = []
for number in numbers:
    if number in unique_numbers:
        unique_numbers.add(number)  # AttributeError: 'list' object has no attribute 'add'
print(f"Unique numbers: {unique_numbers}")

# Swap two variables
a = 5
b = 10
a = b
b = a
print(f"After swapping: a = {a}, b = {b}")
