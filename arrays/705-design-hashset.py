"""
LeetCode 705: Design HashSet
https://leetcode.com/problems/design-hashset/

📝 Summary:

🧠 Thought Process:

✅ Solution Approach:

🐞 Mistakes & Gotchas:

🎓 What I Learned:
1. In Python, remove(element) vs pop(index) 
2. Read the size limits (So you can use some tricks)

🔁 Revisit: No
"""


# Naive approach 
# O(n) for each function call, and Space: O(n)
# Time: add and remove scans through whole; Space: store each once
class MyHashSet:

    def __init__(self):
        self.arr = []

        

    def add(self, key: int) -> None:
        if key not in self.arr: 
            self.arr.append(key) 
        

    def remove(self, key: int) -> None:
        # self.arr.pop(key)
        if key in self.arr:
            self.arr.remove(key)
        

    def contains(self, key: int) -> bool:
        for k in self.arr:
            if key == k:
                return True 
        return False

        # return key in self.arr

"""
At most 10^4 (add, remove, contains). We will map each of the value (key) into 
one of the 10000 buckets. Easiest: key % 10000. 

We can use linked list to handle collisions. 
E.g. Index: 1. Value: 10,001 -> 1 -> 20,001 

Add: 1 -> 10,001. Remove: you point 10,001 to 20,001. Contains: you traverse from 10,001 to 20,001.

Time: Average O(1). Why? Because we are using a fixed number of buckets (10000), 
and each bucket will have a linked list to handle collisions. The average length of
 the linked list will be very short (ideally 1).
Space: O(n), where n is the number of elements in the hash set. 
Why? Because we are storing each element in the hash set, and in the worst case,
 all elements could be in the same bucket (though this is unlikely with a good hash function).
"""
# Linked List approach
# Linked List Structure: (key, next) -> (key, next) -> (key, next) ... 
class ListNode:
    def __init__(self, key): 
        self.key = key 
        self.next = None 

class MyHashSet:
    def __init__(self):
        # Constraints: 10^4
        self.buckets = [ListNode(0) for _ in range(10**4)] 

    def add(self, key: int) -> None:
        index = key % len(self.buckets)     # Hash function to place key in bucket 
        curr = self.buckets[index]   # each bucket is ListNode(0) - key = 0, so it points to the head.
        while curr.next:
            if curr.next.key == key:  # Duplicates 
                return 
            curr = curr.next 
        
        # Goes to the end of the linked list 
        curr.next = ListNode(key)
      

    def remove(self, key: int) -> None:
        curr = self.buckets[key % len(self.buckets)]
        while curr.next:
            if curr.next.key == key: 
                # "Remove" = point to the next key 
                curr.next = curr.next.next
                return 
            curr = curr.next

    def contains(self, key: int) -> bool:
        curr = self.buckets[key % len(self.buckets)] 
        while curr.next: 
            if curr.next.key == key: 
                return True
            curr = curr.next 
        return False



# The BST approach: time and space complexity are O(log n) on average, O(n) in the worst case (unbalanced tree)
# Each BST is init an empty tree, but then each added node is a TreeNode
class TreeNode: 
    def __init__(self, key): 
        self.key = key
        self.left = None
        self.right = None

class BST: 
    def __init__(self): 
        self.root = None

    def insert(self, root, key): 
        if not root: 
            # Explanation: If the current root is None, we have found the correct spot to insert the new key.
            return TreeNode(key) 
        if key < root.key: 
            root.left = self.insert(root.left, key)
        elif key > root.key:
            root.right = self.insert(root.right, key)
        return root 
    # Why return root in the end? To be inserted by the add function to the tree. 

    def delete(self, root, key): 
        if not root: 
            return None  # explanation: If the current root is None, we have reached a leaf node without finding the key 
        if key < root.key: 
            # Walk down the tree
            root.left = self.delete(root.left, key) 
        elif key > root.key: 
            root.right = self.delete(root.right, key)
        else: 
            if not root.left: 
                return root.right 
            if not root.right: 
                return root.left
            # Two children case: find the inorder successor (smallest in the right subtree)
            temp = root.right
            while temp.left: 
                temp = temp.left 
            # Replace the key of the current root with the inorder successor's key
            root.key = temp.key
            # Delete the inorder successor
            root.right = self.delete(root.right, temp.key)
        return root

    def search(self, root, key): 
        if not root:
            return False
        if key == root.key:
            return True
        elif key < root.key:
            return self.search(root.left, key)
        else:
            return self.search(root.right, key)

    # Why do we need an extra add function when we have insert? To maintain the root reference, 
    # or else we lose the reference to the root. Treat insert as a helper function, and add as 
    # the main function that users will call - that ASSIGNS it back to the bst.root 
    def add(self, key):
        self.root = self.insert(self.root, key) 
    
    def remove(self, key): 
        self.root = self.delete(self.root, key) 

    def contains(self, key): 
        return self.search(self.root, key)

class MyHashSet: 
    def __init__(self):
        self.size = 10000 
        self.buckets = [BST() for _ in range(self.size)]
    
    def _hash(self, key): 
        return key % self.size

    def add(self, key: int) -> None:
        index = self._hash(key)
        self.buckets[index].add(key)
    
    def delete(self, key: int) -> None:
        index = self._hash(key) 
        self.buckets[index].remove(key) 
    
    def contains(self, key: int) -> bool:
        index = self._hash(key) 
        return self.buckets[index].contains(key)

"""
Example: 
5
 \
  7
   \
    9

bst.remove(7) 
self.root = self.delete(self.root, 7) 

Calling self.delete(self.root, 7) 
delete(root=5, key=7): 
    root.right = self.delete(root.right, 7) 
    Reaches our target:
    if not root.left: return root.right (9) 
    So, root.right = node9 

self.root = root (which is still node5), but internally the right pointer is at node9.
Then we have: 
5
 \
  9
"""

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
