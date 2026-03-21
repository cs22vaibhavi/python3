name = input("Enter student name: ")

m1 = int(input("Enter marks of subject 1: "))
m2 = int(input("Enter marks of subject 2: "))
m3 = int(input("Enter marks of subject 3: "))
m4 = int(input("Enter marks of subject 4: "))
m5 = int(input("Enter marks of subject 5: "))

total = m1 + m2 + m3 + m4 + m5
average = total / 5

print("Total Marks =", total)
print("Average =", average)

if average >= 90:
    print("Grade: A+")
elif average >= 75:
    print("Grade: A")
elif average >= 60:
    print("Grade: B")
elif average >= 50:
    print("Grade: C")
else:
    print("Grade: Fail")
