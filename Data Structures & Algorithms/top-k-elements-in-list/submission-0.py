class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)

        for num in nums:
            d[num] += 1
    
        freq = [[] for _ in range(len(nums)+1)]

        for num in d:
            freq[d[num]].append(num)
        
   
        output = []
        for index in range(len(nums), 0, -1):
         
            for num in freq[index]:
                output.append(num)
                if len(output) == k:
                    return output
        return output