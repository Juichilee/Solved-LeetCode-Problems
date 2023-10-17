class Twitter:

    def __init__(self):
        self.count = 0 # for python max heap sort, count decrements following a unit of time
        self.tweetMap = defaultdict(list)
        self.followMap = defaultdict(set)

    # Time Complexity: O(1) 
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1

    # Time Complexity: O(10 * k) k = num of followers
    def getNewsFeed(self, userId: int) -> List[int]:
        res = [] # ordered starting from recent
        minHeap = []

        self.followMap[userId].add(userId) # add user to own list of followers
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap: # check if followee has at least one tweet
                index = len(self.tweetMap[followeeId]) - 1 # get last index o flist
                count, tweetId = self.tweetMap[followeeId][index]
                minHeap.append([count, tweetId, followeeId, index - 1])
            heapq.heapify(minHeap)
        while minHeap and len(res) < 10: # get 0 - 10 most recent tweets
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)
            # get next post to add to min heap
            if index >= 0: # make sure followee still has posts left
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])
        return res

    # Time Complexity: O(1) 
    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)
    
    # Time Complexity: O(1)
    def unfollow(self, followerId: int, followeeId: int) -> None:
        # update user's news feed
        if followeeId in self.followMap[followerId]: # remove() set will throw issue if not in set
            self.followMap[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)

    # Space Complexity: O(n + m) n, m = num_posts, num_followers
    # Datastructure(s): Max Heap, HashTable, HashSet
    # Algorithm(s): None
    # Pattern: Heap
    
    # Link: https://leetcode.com/problems/design-twitter/