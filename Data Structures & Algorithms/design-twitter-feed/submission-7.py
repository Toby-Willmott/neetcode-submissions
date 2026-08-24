class Twitter:

    def __init__(self):
        self.users = []
        self.tweets = []
        heapq.heapify(self.tweets)
        self.follows = defaultdict(list)
        self.recent_count = -1
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        heapq.heappush(self.tweets, (self.recent_count, tweetId, userId))
        self.recent_count -= 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        temp = [] 
        output = [] 
        
        while len(output) < 10 and self.tweets: 
            recency, tweetId, posterId = heapq.heappop(self.tweets)
            if userId in self.follows[posterId] or posterId == userId: 
                output.append(tweetId) 
            temp.append((recency, tweetId, posterId))
        
        
        while temp:
            curr = temp.pop() 
            heapq.heappush(self.tweets, curr)
        
        return output 



        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.follows[followeeId]: 
            self.follows[followeeId].append(followerId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follows[followeeId]: 
            self.follows[followeeId].remove(followerId)
        
        
