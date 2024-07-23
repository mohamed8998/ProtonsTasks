purchaseamount=int(input("What is the total purchase amount? "))
year=int(input("How many years have you been a member of the book store? "))
complaints=int(input("How many complaints they have fild in the past year? "))
purchases=int(input("How many purchases they have made in the past year? "))
discount=0
if year>10:
    discount=(10/100)
elif year >=6 and year <=10:
    discount= (8/100)
elif year < 6:
    discount = (5/100)

if complaints > 5:
    discount=0    
else:
    discount=discount-(complaints*(2/100))
    if discount <=0:
        discount=0
     

if purchases > 20:
    discount = discount + (5/100)

purchaseamount = purchaseamount - purchaseamount * discount
print("The discount is "  ,discount)

print("the total purchase" ,purchaseamount)