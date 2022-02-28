#problem7
sum = 0
count = 0


list1 = [11, 5, 17, 18, 23]


while (count < len(list1)):
    sum = sum + list1[count]
    count += 1


print("Sum of all elements in given list: ", sum)