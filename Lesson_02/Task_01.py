#task 1 for lesson 2 (about name)
print("Enter your the first name: ")
f_name = input(str())
print("Enter your the second name: ")
s_name = input(str())
full=f_name.title()+' '+s_name.title()

print("Your name is :")
print(full)
print("Please input the symbol that you want to replace in your full name and after click enter: ")
# user can input the symbol if want to change to another (a to b)
a = input(str())
print("Please input the new symbol with you want to see in your full name and after click enter: ")
b = input(str())
full2=full.replace(a,b)
print(f"I will try to help you remind your name: \nYour name is \n\tAnd you really know it \n{full2}")
print("Please input input 'YES' if you want delete spaces in you name and after click enter: ")
#we try to get user's answer
ans = input(str())
# change of register to use operator "if" in the future
ans = ans.upper()
if ans == "YES":
    print(f"After replace we have your new name : \n{full.replace(' ','')}")
else:
    print(f"Ok your old name is \n{full} \n\tbut for test \n\t{full.replace(' ','')}")