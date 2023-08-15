from collections import defaultdict

class LFUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.frequency = defaultdict(int)  

    def get(self, key):
        if key in self.cache:
            self.frequency[key] += 1  # Increment access frequency
            return self.cache[key]
        else:
            return None

    def put(self, key, value):
        if self.capacity <= 0:
            return

        if key in self.cache:
            self.cache[key] = value  # Update existing key
            self.frequency[key] += 1  # Increment access frequency
        else:
            if len(self.cache) >= self.capacity:
                # Find the least frequently used page
                min_freq_key = min(self.frequency, key=self.frequency.get)
                del self.cache[min_freq_key]
                del self.frequency[min_freq_key]

            self.cache[key] = value
            self.frequency[key] = 1 

# Example usage:
cache = LFUCache(3)
cache.put('A', 1)
cache.put('B', 2)
cache.put('C', 3)
print(cache.get('A'))  # Output: 1
print(cache.get('B'))  # Output: 2
cache.put('D', 4)  
print(cache.get('C'))  
