n = []

l = int(input("Please enter the Total Number of List Elements: "))
for i in range(1, l + 1):
    value = int(input("Please enter the Value of %d Element : " %i))
    n.append(value)

n.sort()


print("Element After Sorting List in Ascending Order is : ", n)