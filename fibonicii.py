def fibo(n):
    if(n<=1):
        return n
    return fibo(n-2)+fibo(n-1)
def non_rec_fibo(n):
    a,b=0,1
    if(n<=1):
        print(0)
    else:
        print(a,b,end=" ")
    for i in range(2,n):
        c=a+b
        print(c, end=" ")
        a=b
        b=c
n=int(input("Enter the number"))       
for i in range(n):
    print(fibo(i), end=" ")
print(end="\n")
if(n==0):
  pass
else:
    non_rec_fibo(n)
        
