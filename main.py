Name = input("Enter your name: ")
Age = int(input("Enter your age: "))
Gpa = float(input("Enter your GPA (0 - 5): "))
Field_of_interest= input("Enter your field of interest: ")
Graduated = input("Have you graduated? (yes/no): ")

if Age < 25 and Gpa >= 3.5 and Graduated == "yes":
    print("You are eligible for a Scholarship.")

elif Age < 30 and Gpa >= 2.5:
    print("You are eligible for an internship.")

else:
    print("sorry,please apply again later . ")
    