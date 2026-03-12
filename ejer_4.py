# 4. Cine: entrada según edad

print("WELCOME TO CINECOLOMBIA")

age = int(input("Enter your age: "))

if age < 12:
    print("ticket value: $8000")

elif age >= 12 and age < 60:
    print("ticket value: $12000")

elif age >= 60:
    print("ticket value: $9000")