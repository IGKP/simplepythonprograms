a = float(input("Please enter English Marks: "))
b = float(input("Please enter Math score: "))
c= float(input("Please enter Computer Marks: "))
d= float(input("Please enter Physics Marks: "))
e= float(input("Please enter Chemistry Marks: "))

total = a + b + c + d + e
average = total / 5
percentage = (total / 500) * 100

print("\nTotal Marks = %.2f" % total)
print("Average Marks = %.2f" % average)
print("Marks Percentage = %.2f" % percentage)