import random
letters= ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
          'A','B','C','D','E','F','G','H','I','J','K',
          'L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','#','%','&','*','+','$']
print("Welcome to password generator!")
letter=int(input("How many letters you want in password: \n"))
number=int(input("How many numbers you want in password: \n"))
symbol=int(input("How many symbols you want in password: \n"))
password_list = [ ]
for i in range(1,letter+1):
    char=random.choice(letters)
    password_list += char

for i in range(1,number+1):
    char=random.choice(numbers)
    password_list += char

for i in range(1,symbol+1):
    char=random.choice(symbols)
    password_list += char

print(password_list)
random.shuffle(password_list)
print(password_list)

password= ""
for char in password_list:
    password += char
print(password)

