def palindrome(str):
    last=len(str)-1
    flag =True
    mid = int(len(str)/2)
    for i in range(0,mid,1):
        if str[i]!=str[last]:
            flag=False
            return flag
        last =last -1
    return flag
print(palindrome("malayalam")) 
print(palindrome("geeks"))
