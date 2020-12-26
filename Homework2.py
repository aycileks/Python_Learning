# GlobalAIHub Python Introduction Homework2

print("User Identification Program\n")
first_name = str(input("First Name : "))
last_name = str(input("Last Name : "))
age = int(input("Age : "))
dob = int(input("Date of Birth (YYYY) :"))
user = [first_name, last_name, age, dob]
for i in user:
    print(i)
if age < 18:
    print("\n You cannot go out becuse it is too dangerous!")
else:
    print("\n You can go out to the street.")
