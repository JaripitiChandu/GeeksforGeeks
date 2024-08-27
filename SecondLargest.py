def print2largest(self, arr):
        # Code Here
    
        first= - 2**31
        second = -2**31
        
        for i in arr:
            if first < i :
                second = first
                first =i
            elif i>second and i!=first :
                second = i
        return second  
