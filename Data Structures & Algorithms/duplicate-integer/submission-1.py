class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        table = {}
        for key in nums:
            if key in table:
                table[key] += 1
            else:
                table[key] = 1
        result = any(value >= 2 for value in table.values())
        return result 