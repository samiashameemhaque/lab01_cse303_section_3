#problem8
NumList = []
Even_Sum = 0

j = 0

Number = int(input("Please enter the Total Number of List Elements: "))
for i in range(1, Number + 1):
    value = int(input("Please enter the Value of %d Element : " %i))
    NumList.append(value)

while(j < Number):
    if(NumList[j] % 2 == 0):
        Even_Sum = Even_Sum + NumList[j]

    j = j+ 1

print("\nThe Sum of Even Numbers in this List =  ", Even_Sum)
