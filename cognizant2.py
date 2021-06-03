'''T=int(input("enter no of test cases:"))           
arr=[]                               
for  j in range(T):
    L,R=input("enter the range:").split()
    L=int(L)    
    R=int(R)    
    for num in range(L,R+ 1):
         if num > 1:  
               for i in range(2,num):  
                   if (num % i) == 0:  
                       break  
               else:  
                   arr.append(num)
    if len(arr)>0:
       print(max(arr)-min(arr))
       arr.clear()
    else:
        print(-1)
        
        '''
T=int(input())           
arr=[]
def primes():
    for num in range(L,R+ 1):
            if num > 1:  
                for i in range(2,num):  
                    if (num % i) == 0:  
                        break  
                else:  
                    arr.append(num)                             
for  j in range(T):
        L,R=input().split()
        L=int(L)    
        R=int(R)    
        primes()
        if len(arr)>0:
            print(arr)
            print(arr[-1]-arr[0])
            arr.clear()
        else:
            print(-1)
        
    



      
                
    
    
    
    
            

