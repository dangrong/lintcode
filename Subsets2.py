import copy

class Solution:
    """
    @param S: A set of numbers.
    @return: A list of lists. All valid subsets.
    """
    def subsetsWithDup(self, S):
        # write your code here
        result =[]
        
        # Input Validations
        if S is None or len(S) == 0:
            return result
            
        return self.subsetsHelper(0, sorted(S), [], result)
    
    def subsetsHelper(self, pos, S, curr, ra):
        ra.append(copy.deepcopy(curr))
        
        for i in range(pos, len(S)): 
            if i!=pos and S[i] == S[i-1]:
                continue
            curr.append(S[i])
            ra = self.subsetsHelper(i+1, S, curr, ra)
            curr.remove(S[i])
        
        return ra