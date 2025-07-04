print("Pizza order bill")
size= input("Enter the size you want? s,m,l \n")
pepperoni= input("If you want to add pepperoni then type y for yes and no for n \n")
extra_cheese= input("If you want extra cheese then type y otherwise n \n")

bill=0
if size== "s":
    bill +=15
elif size =="m":
    bill +=20
elif size =="l":
    bill +=25
else:
    print("It's not a valid input")

if pepperoni== "y":
    if size == "s":
        bill +=2
    else:
        bill +=3
    

if extra_cheese=="y":
    bill +=1

print(f"The total bill is: ${bill}")