def revers(str):
    newstr=""
    for i in range(len(str)):
        if str[i]==" ":
           temp=str[:i]
           newstr.join(temp)
           break
         

revers("hello hh hi")