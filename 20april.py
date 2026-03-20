name = input("Enter your name: ")
m1 = int(input("Enter marks in subject 1: "))
m2 = int(input("Enter marks in subject 2: "))
m3 = int(input("Enter marks in subject 3: "))

total = m1 + m2 + m3
average = total / 3

print("Student Name:", name)
print("Total Marks:", total)
print("Average Marks:", average)

if average >= 50:
    print("Result: Pass")
else:
    print("Result: Fail")
