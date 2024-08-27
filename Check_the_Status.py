def check_status(a, b, flag):
    ##Your code here
    ##Either True or False is returned
    
    if (((a>0 and b<0) or (a<0 and b>0)) and flag==False) or (a<0 and b<0 and flag==True):
        return True
    else:
        return False
    
