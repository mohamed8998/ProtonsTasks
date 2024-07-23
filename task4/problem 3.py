loanamount=int(input("enter the loan amount: "))
age=int(input("enter your age: "))
monthlyincome=int(input("enter your monthly income: "))


employmentstatus=input("enter your employment status(employed or unemployed): ")  


creditscore=int(input("enter your credit score: "))
outstandingloan=input("Do you have outstanding loan?(yes/no): ")

reason=""
if age < 18:
   reason=reason + "not old enough"


if monthlyincome < (loanamount/12):
   reason=reason + " ,not income enough"


if employmentstatus == "unemployed":
   reason=reason + " ,unemployed"
  

if creditscore< 350 or creditscore >800  :
   reason=reason + " ,not enough creditscore"


if outstandingloan=="yes":
   reason=reason + " ,have outstandingloan"

if reason=="":
   print("congratulation you can get loan")
else:
   print("you cannot get loan")
   print( "reasons: " + reason)



    
    
   
   
