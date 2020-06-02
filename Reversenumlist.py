maximum = int(input("Please Enter the Maximum integer Value : "))
minimum = int(input("Please Enter the Minimum integer Value : "))

print("List of Natural Numbers from {0} to {1} : ".format(maximum, minimum))

while ( maximum >= minimum):
    print (maximum, end = '  ')
    maximum = maximum - 1
