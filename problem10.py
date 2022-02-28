#problem10
def second_largest_number(NumList,Number):

        secondLargest = NumList[0]
        largest = NumList[0]
        for i in range(len(NumList)):
            if NumList[i] > largest:
                largest = NumList[i]

        for i in range(len(NumList)):
            if NumList[i] > secondLargest and NumList[i] != largest:
                secondLargest = NumList[i]

        return secondLargest



def Main():
    NumList = []
    Number = int(input("Please enter the Total Number of List Elements: "))
    for i in range(1, Number + 1):
     value = int(input("Please enter the Value of %d Element : " % i))
     NumList.append(value)

    smallest = largest = NumList[0]
    second_largest_number(NumList,Number)
    print(second_largest_number(NumList,Number))




if __name__ == "__main__":
 Main()