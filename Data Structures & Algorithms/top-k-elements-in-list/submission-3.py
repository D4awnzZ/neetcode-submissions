class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1
        
        freq = [[] for _ in range(len(nums) + 1)]
        for n, cnt in count.items():
            freq[cnt].append(n)
        
        res = []
        for cnt in range(len(freq) - 1, 0 ,-1):
            for nums in freq[cnt]:
                res.append(nums)
                if len(res) == k:
                    return res

