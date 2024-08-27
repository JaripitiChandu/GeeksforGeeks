class Solution:
    def subArraySum(self,arr, n, s): 
       #Write your code here
        start=0;
        end=0
        sum=0
        for i in range(n):
            sum+=arr[i]
            end=i
            while(sum>s and start<end):
                sum=sum-arr[start]
                start=start+1
            if sum == s:
                return [start+1,end+1]
        return [-1]
