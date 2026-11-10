fname = input("what is your fname ?")
mname = input("what is your mname ?")
lname = input("what is your lname ?") 
age = int(input("what is your age ?"))
num = int(input("what is your num ?"))
city = input("what is your city ?")
country = input("what is your country ?")

info = {city: country}
ports = [22,80, 443]

print(f"hello : {fname} {mname} {lname} nice to meet you")
print(f"your age is : {age} and your number is {num}")
print(f"{city} is in {info[city]}")
print(f"second port in my list: {ports[1]}")
print(type(info))
