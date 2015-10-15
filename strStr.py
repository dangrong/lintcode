class Solution:
    def strStr(self, source, target):
        # write your code here
        
        #Input Validation
        if target is None:
            return -1
            
        if not target:
            return 0
        
        if not source:
            return -1
    
            
            
        for i in range(0,len(source)):
            index = 0
            for j in range(0,len(target)):
                if source[i + index] == target [j]:
                    index = index + 1
                    if index == len(target):
                        return 1
                else:
                    break
                
        return -1
        
        