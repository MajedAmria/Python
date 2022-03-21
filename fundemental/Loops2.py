
def big(list):
    for i in range(0,len(list)):
        if list[i]>=0:
           list[i]="big"

    return list



def count_positives(list):
    counter=0
    for i in range(0,len(list)):
        if list[i]>=0:
           counter=counter+1
        list[-1]=counter
    return list



def sum_total(list):
    sum=0
    for i in range(0,len(list)):
           sum=sum+list[i]
        
    return sum



def avarge(list):
    sum=0
    avg=0
    for i in range(0,len(list)):
           sum=sum+list[i]
    avg=sum/len(list) 
    return avg



def length(list): 
    return len(list)



def max(list):
    if len(list)==0:
        return "false"
    else:    
     max=list[0]
     for i in range(0,len(list)):
           if max<list[i]:
               max=list[i]
     return max
           
               


def min(list):
    if len(list)==0:
        return "false"
    else:    
     min=list[0]
     for i in range(0,len(list)):
           if min>list[i]:
               min=list[i]
     return min
  
           

def ultimate_analysis(list):
    dictionary ={'sumTotal': sum_total(list),
      'average': avarge(list),
       'minimum': min(list), 
       'maximum': max(list),
       'length': length(list)}
    return dictionary
print(ultimate_analysis([37,2,1,-9]))

def revers(list):
    if len(list)==0:
        return "list is empty!"
    else:    
        length=len(list)
        for i in range(int(length/2)):
          temp=list[length-1-i]
          list[length-1-i]=list[i]
          list[i]=temp
        return list
       
         
       
     
print(revers([1,2,3,4,5]))