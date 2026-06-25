from sortedcontainers import SortedDict

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

        timestamps = self.keyStore[key]
        if timestamp in self.keyStore[key]:
            return self.keyStore[key][timestamp]
        else:
            temp = [x for x in self.keyStore[key] if x[1] <= timestamp]
            
            if not temp: 
                return ""
            return max(temp, key = lambda x : x[1])[0]
        
        
