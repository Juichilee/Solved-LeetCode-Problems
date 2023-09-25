class MyHashSet:
    def __init__(self):
        self.size = 10007 # prime number to prevent collisions
        self.buckets = [[] for _ in range(self.size)]

    def add(self, key):
        bucket, idx = self._index(key)
        if idx >= 0:
            return
        bucket.append(key)

    def remove(self, key):
        bucket, idx = self._index(key)
        if idx < 0:
            return
        bucket.remove(key)

    def contains(self, key):
        _, idx = self._index(key)
        return idx >= 0

    def _hash(self, key):
        return key % self.size

    # Retrieves the bucket and index of key if it exists
    def _index(self, key):
        hash = self._hash(key)
        bucket = self.buckets[hash]
        for i, k in enumerate(bucket):
            if k == key:
                return bucket, i
        return bucket, -1

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)

    # Time Complexity: On average, constant time (Add, Contains, Remove)
        # O(n) due to chaining, however same hashes are unlikely to occur
    # Space Complexity: O(n)
    # Datastructure(s): HashSet
    # Algorithm(s): Division Hashing Function
    # Pattern: None

### 
# Solution Description: Solution referenced from: 
#   https://leetcode.com/problems/design-hashset/solutions/152654/python-hash-set-with-trivial-hash-function/
###

# Link: https://leetcode.com/problems/design-hashset/description/