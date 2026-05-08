class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        k1, k2 = 0, 0
        
        for i in range(len(nums)):
            for j in range(len(nums)):
                if (nums[i] + nums[j] == target):
                    
                    k1, k2 = j, i
                    break

        return [k1, k2]