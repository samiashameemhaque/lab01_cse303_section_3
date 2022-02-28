#problem9
def largest_number_2019_1_60_053(NumList,Number):
 largest = NumList[0]
 for j in range(1, Number):
     if (largest < NumList[j]):
         largest = NumList[j]

 print("The Largest Element in this List is : ", largest)


def smallest_number_2019_1_60_053(NumList,Number):
 smallest = NumList[0]
 for j in range(1, Number):
     if (smallest > NumList[j]):
        smallest = NumList[j]

 print("The Smallest Element in this List is : ", smallest)

def Main():
    NumList = []
    Number = int(input("Please enter the Total Number of List Elements: "))
    for i in range(1, Number + 1):
     value = int(input("Please enter the Value of %d Element : " % i))
     NumList.append(value)
     smallest = largest = NumList[0]

    largest_number_2019_1_60_053(NumList,Number)
    smallest_number_2019_1_60_053(NumList,Number)



if __name__ == "__main__":
 Main()