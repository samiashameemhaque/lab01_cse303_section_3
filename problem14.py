def palindrome_checker_2019_1_60_053(str):

    for i in range(0, int(len(str) / 2)):
        if str[i] != str[len(str) - i - 1]:
            return False
    return True




s = input("Enter the word : ")
ans = palindrome_checker_2019_1_60_053(s)

if (ans):
    print("Yes")
else:
    print("No")