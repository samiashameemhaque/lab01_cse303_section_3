str = input("Enter The String: ")
substr = "cse303"
l = len(str)
count = 0
es = ''
for i in range (l):
    es += str[i]
    if es == substr:
       if str[i+1] != ' ':
          count = 0
        else:
            count += 1
            es = ''
print (count)
