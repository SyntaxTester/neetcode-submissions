class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        k = 0
        nums.sort()
        answer = []


        for i in range(len(nums) - 1):
            if nums[i] + 1 == nums[i + 1]:
                k += 1
            elif nums[i] + 2 <= nums[i + 1]:
                answer.append(k)
                k = 0
            print(answer, k)
        answer.append(k)
            

        if len(nums) != 0:
            return max(answer) + 1
        return max(answer)