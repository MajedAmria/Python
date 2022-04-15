def Tribonacci(n):
    # t0=0
    # t1=1
    # t2=1
    if n==0:
        return 0
    elif n == 2 or n==1 :
        return 1 
    else:
        return Tribonacci(n-1)+Tribonacci(n-2)+Tribonacci(n-3)
        
print(Tribonacci(0))
print(Tribonacci(2))
print(Tribonacci(5))