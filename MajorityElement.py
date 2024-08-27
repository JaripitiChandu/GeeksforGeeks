def majorityElement(self, A, N):
        #Your code here
        
        count=0
        num=None
        for i in range(N):
            if count==0:
                num=A[i]
                count=1
            else:
                if A[i]==num:
                    count+=1
                else:
                    count-=1
        if count>0:
            num_count=0
            for i in A:
                if i==num:
                    num_count+=1
                    
            if num_count> N//2:
                return num
            else:
                return -1
        else:
            return -1
