class TimeMap:

    def __init__(self):
        self.keyStore = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyStore: 
            self.keyStore[key] = []
        self.keyStore[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.keyStore: 
            return ""

        res = "" 
        timestamps = self.keyStore[key]

        l = 0
        r = len(timestamps) - 1

        while l <= r: 
            m = (l+r)//2
        
            if timestamps[m][1] <= timestamp: 
                res = timestamps[m][0]
                l = m + 1
            else: 
                r = m - 1
        return res
        
        
