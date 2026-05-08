class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []
        k = 0

        for i in range(len(nums)):
            k = 1
            for j in range(len(nums)):
                if i != j:
                    k *= nums[j]
            answer.append(k)

        return answer            