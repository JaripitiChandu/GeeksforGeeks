def leaders(self,n, arr):
        #Code here
        res=[]
        max=0
        for i in range(n):
            if i==0 :
                res.append(arr[n-i-1])
                max=arr[n-i-1]
            elif max<=arr[n-i-1]:
                max=arr[n-i-1]
                res.append(arr[n-i-1])
        return res[::-1]
