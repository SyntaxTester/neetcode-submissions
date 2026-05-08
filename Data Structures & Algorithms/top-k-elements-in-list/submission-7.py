class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums.sort(reverse = True)
        indexes = []
        counter = 0
        filtered = list(dict.fromkeys(nums))
        answer = []

        for i in range(len(nums)):
            if i == len(nums) - 1 and nums[i] != nums[i - 1]:
                indexes.append(counter)
                counter = 0
                # del indexes[0]
            if i == len(nums) - 1:
                counter += 1
                indexes.append(counter)
                del indexes[0]
            elif nums[i] == nums[i - 1]:
                counter += 1
            else:
                indexes.append(counter)
                counter = 0

        if len(nums) == k == 2:
            answer = nums.copy()
        elif len(indexes) != 0:
            for i in range(k):
                print(nums)
                print(indexes)
                print(filtered)
                answer.append(filtered[indexes.index(max(indexes))])
                indexes[indexes.index(max(indexes))] = -1
        else:
            answer.append(nums[len(indexes)])


        return answer