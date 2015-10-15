import copy

class Solution:
    """
    @param nums: A list of integers.
    @return: A list of unique permutations.
    """
    def permuteUnique(self, nums):
        result =  []
        if not nums:
            return result
            
        self.permuteHelper(0, result, sorted(nums))
        
        return result
        
        
    def permuteHelper(self, pos, result, nums):
        if pos == len(nums) - 1:
            result.append(copy.deepcopy(nums))
            return
        
        # List will not be sorted after swap, may have same number
        # not beside each other => Use list to keep track
        num_list = []

        for i in range(pos, len(nums)):
            if i != pos and nums[i] in num_list:
                continue
            
            if not nums[i] in num_list:
                num_list.append(nums[i])
            
            temp = nums[pos]
            nums[pos] = nums[i]
            nums[i] = temp
            
            self.permuteHelper(pos + 1, result, nums)
            
            temp = nums[pos]
            nums[pos] = nums[i]
            nums[i] = temp