import copy

class Solution:
    """
    @param S: The set of numbers.
    @return: A list of lists. See example.
    """
    def subsets(self, S):
        # write your code here
        return self.subsetsHelper(0, sorted(S), [], [])
        
    def subsetsHelper(self, pos, S, curr, return_array):
        return_array.append(copy.deepcopy(curr))
        i = pos
        for i in range(pos,len(S)):
            curr.append(S[i])
            return_array = self.subsetsHelper(i+1, S, curr, return_array)
            curr.remove(S[i])
            
        return return_array