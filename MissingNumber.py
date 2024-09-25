def missingNumber(self, n, arr):
        
        sum = int(n*(n+1)/2)
        cal_sum=0
        for i in arr:
            cal_sum+=i
        return sum-cal_sum
##        # code here
