"""
LeetCode 706: Design HashMap
https://leetcode.com/problems/design-hashmap/

📝 Summary:

🧠 Thought Process:

✅ Solution Approach:

🐞 Mistakes & Gotchas:

🎓 What I Learned:
1. Use [-1 for _ in range(1000001)] to create a list with a specific size and default value. 
2. Linked list logic: Think of the first case (empty) first, then add conditions. 

🔁 Revisit: No
"""

# Linked List approach: Time and space, O(n/k), O(k+m), where n is the number of elements and k is the number of buckets, m is the number of unique keys
class ListNode: 
    def __init__(self, key = -1, value = -1, next = None): 
        self.key = key 
        self.value = value 
        self.next = next 

class MyHashMap: 
    def __init__(self): 
        self.max = 1000
        self.buckets = [ListNode() for _ in range(self.max)] 

    def put(self, key: int, value: int) -> None: 
        cur = self.buckets[key % self.max]
        while cur.next:  # the first one is just place holder, it's cur.next is the first value. 
            if cur.next.key == key:
                cur.next.value = value 
                return
            cur = cur.next
        cur.next = ListNode(key, value)  # next = None; last element 
                
    def get(self, key: int) -> int:
        cur = self.buckets[key % self.max]
        while cur.next: 
            if cur.next.key == key: 
                return cur.next.value
            cur = cur.next 
        return -1 

    def remove(self, key: int) -> None:
        cur = self.buckets[key % self.max]
        while cur.next: 
            if cur.next.key == key: 
                cur.next = cur.next.next
                return 
            cur = cur.next


# Neetcode: The index is already the key, so we can use a list to store values.
class MyHashMap:

    def __init__(self):
        self.map = [-1] * 1000001

    def put(self, key: int, value: int) -> None:
        self.map[key] = value

    def get(self, key: int) -> int:
        return self.map[key]

    def remove(self, key: int) -> None:
        self.map[key] = -1
    

# Time: O(1), Space: O(1000000) 
class MyHashMap:
    def __init__(self):
        self.max = 10**6 + 1
        # self.map = [[-1] * self.max]   - wrong.  
        # Or [-1] * (10**6 + 1)
        self.map = [-1 for _ in range(self.max)] 
         

    def put(self, key: int, value: int) -> None:
        # if key not in self.map:   Wrong, why? Because the key could be any integer, including negative numbers. 
            # self.map[key] = [key]
        if self.map[key] == -1:     # Lesson: You can use -1 to represent empty slots
            # Empty slot
            self.map[key] = [key, value]
        else:
            self.map[key][1] = value
        
    def get(self, key: int) -> int:
        if self.map[key] == -1: 
            return -1 
        else: 
            return self.map[key][1]   

    def remove(self, key: int) -> None:
        self.map[key] = -1 


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)