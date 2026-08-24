class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #dic = defaultdict(int)
        #for task in tasks: 
        #    dic[task] += 1
        
        count = Counter(tasks)
        print(count)
        #heap = [(-num, key) for key, num in dic.items()]
        heap = [-cnt for cnt in count.values()]
        print(heap)
        heapq.heapify(heap)
        

        time = 0
        q = deque() 

        while heap or q: 
            time += 1

            if not heap: 
                time = q[0][1]
            else: 
                cnt = 1 + heapq.heappop(heap)
                if cnt: 
                    q.append([cnt, time + n])
            if q and q[0][1] == time: 
                heapq.heappush(heap, q.popleft()[0])
        
        return time


        