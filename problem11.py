#problem11
string= input("enter your string: ")
for index in range(len(string)):

    if index % 2 == 0:

        print(string[index], end='')
