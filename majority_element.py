class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = {v: 0 for v in nums}
        for i in nums:
            dic[i] += 1
        for key, value in dic.items():
            if value >= len(nums)/2:
                return key
