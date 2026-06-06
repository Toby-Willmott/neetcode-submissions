class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq = defaultdict(list)

        for index, string in enumerate(strs): 
            count = [0] * 26
            for c in string: 
                count[ord(c) - ord("a")] += 1
            freq[tuple(count)].append(string)
        
        return(list(freq.values()))



