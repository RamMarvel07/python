status=input("Enter your status (married/unmarried):")
gender=input("Enter your gender (male/female):")
age=int(input("Enter your age:"))
if status=="married":
    print("driver insured")
elif status=="unmarried" and gender=="male" and age>30:
    print("driver insured")
elif status=="unmarried" and gender=="female" and age>25:
    print("driver insured")
else:
    print("driver not insured")
