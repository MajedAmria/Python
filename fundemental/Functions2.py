"""
def Countdown(number):
    for i in range(number,-1,-1):
        print(i)
Countdown(5)"""
"""
def print_and_return(list):
    print(list[0])
    return list[1]

print(print_and_return([1,2])) 
"""
"""
sum=0
def Length(list):
  sum=list[0]+len(list)
  return sum

print(Length([1,2,3,4,5]))
"""

def values_greater_than_second(list):
    if len(list)<2:
        return False
    newList = []

    for val in list:
        if val>list[1]:
            newList.append(val)
    print(len(newList))    
    return newList
print(values_greater_than_second([55,6,2,3,99,78,20,1]))
print(values_greater_than_second([55,0,2,3,99,78,20,1]))
print(values_greater_than_second([1]))



"""
new = []
def value_and_length(size,value):

  for i in range(size):
     new.append(value)
  return new

print(value_and_length(4,7))
"""