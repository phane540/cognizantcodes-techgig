from math import sqrt
T=int(input())           
arr=[]                  
for  j in range(T):
        L,R=input().split()
        L=int(L)    
        R=int(R)    
        for num in range(L,R+ 1):
            if num > 1:
                for i in range(2,int(sqrt(num+1))+1):
                    if (num % i) == 0:
                        break  
                else:  
                    arr.append(num)   
        if len(arr)>0:
            print(arr[-1]-arr[0])
            arr.clear()
        else:
            print(-1)

