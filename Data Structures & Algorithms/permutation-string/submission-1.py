class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        r = defaultdict(int)
        for letter in s1:
            r[letter] += 1

        for index in range(len(s2)-len(s1)+1):
            print(s2[index:index+len(s1)])
            r2 = defaultdict(int)
            for letter in s2[index:index+len(s1)]:
                r2[letter] += 1
            if r == r2: 
                return True
        
        return False
        