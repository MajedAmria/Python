def myfun(str):
    counter=1
    arr=''
    for i in range(0,len(str)-1):
            if str[i]==str[i+1]:
                counter=counter+1
                
                
            else:
                arr=str(counter)
                arr=str[i]
                counter=1
             
            
    return arr        



print(myfun("AAAABBBCCD"))
#AAAABBBCCD