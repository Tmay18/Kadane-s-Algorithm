def maxSubArraySum(arr,N):
        import math
        ##Your code here
        """
        sumstore=[]
        temp=[]
        sumstore.append(max(arr))
        sumstore.append(max(arr))
        i=2
        while i<=N:
            temp=[]
            j=0
            while j<N:
                k=0
                ax=0
                while k<i:
                    if(j+k)<N:
                        ax=ax+arr[(j+k)]
                        k+=1
                    else:
                        break
                temp.append(ax)
                j+=1
            #print("temp for length ",i,temp)
            sumstore.append(max(temp))
            #print("sumstore for length ",i,sumstore)
            i+=1
        maxx=max(sumstore)
        return maxx
        """
        localmax=0
        globalmax=-math.inf
        i=0
        while i<N:
            localmax=max(arr[i],arr[i]+localmax)
            if localmax>globalmax:
                globalmax=localmax
            i+=1
        return globalmax
n=int(input("Enter a Natural number"))
array=[]
for i in range(0,n):
    element=int(input("Enter the number"))
    array.append(element)
Soln=maxSubArraySum(array,n)
print("Maximum sum is:",Soln)


