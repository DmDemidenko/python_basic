#task 3 - money exchange
print("Input please USD exchange rate (the value of 1 th dollar)")
a = input()
#replace "," to "." to avoid errors
a = a.replace(",",".")
a = float(a)
print("Input how many USD do you want to exchange")
b = input()
#replace "," to "." to avoid errors
b = b.replace(",",".")
b = float(b)
c = b * a
c = round(c, 2)
print (f'current currency is: \n{round(a,2)} UAH to 1 USD \nYou want exchange {round(b,2)} USD and it is {c} UAH ')