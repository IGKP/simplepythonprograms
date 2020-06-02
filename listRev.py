def Reverse(lst):
    return [ele for ele in reversed(lst)]


# Driver Code
lst = []

n = int(input("Enter number of elements : "))
for i in range(0, n):
    ele = int(input())

    lst.append(ele)

print(Reverse(lst))