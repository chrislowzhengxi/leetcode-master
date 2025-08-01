'''
Hackerrank NA: Old Mission DP
Photos in /Uchicago Miscellaneous/Hackerrank OA/Old Mission DP


🧩 Problem Overview: Count Good Arrays

You're given an array arr of length n, where:
Each element is either 0 (can be changed) or a positive integer (must remain unchanged).
You must count how many ways you can replace the zeros so that every pair of adjacent values differ by at most 1.
Return the count modulo 10^9 + 7.

✅ Example:

    arr = [0, 0, 1]
We must end with something like [a, b, 1] where:
    |a - b| ≤ 1
    |b - 1| ≤ 1
We find that there are 9 valid ways to fill [0, 0, 1] that meet the condition:
    [1, 1, 1]
    [2, 1, 1]
    [2, 2, 1]
    [2, 3, 1]
    [1, 2, 1]
    [0, 1, 1]
    [0, 0, 1]
    [1, 0, 1]
    [1, 2, 1]
(you can verify the differences between neighbors are always ≤ 1)



🧠 Core Logic (No Code)


Anchor point:
Find the first non-zero element (the anchor) — this is fixed and splits the array into a left and right part.

Dynamic programming on both sides (they are independent):
- For each side (left and right), you simulate "walking" toward/away from the anchor using DP.
- Keep track of how many ways you can reach each possible value at each step. Two cases:
    - If the current value is fixed (not 0), you can only stay at that value. (L-1, L, L+1)
    - If the current value is 0, you can branch to three possible values: val-1, val, and val+1. (where
    val is the last value you can reach) -- for all previously possible values.
- Dictionary to store counts of ways to reach each value.
- Multiply the counts from both sides to get the total number of valid arrays. (independent choices). 
'''


'''
What is dynamic programming? DP is a method for solving complex problems by breaking them down into simpler subproblems.
It is applicable when the problem can be divided into overlapping subproblems that can be solved independently. From our 
example, we can see that the problem can be divided into two independent parts: the left side of the anchor and the 
right side of the anchor. We do not recompute the same values multiple times, which is a key feature of DP.
'''

def countGoodArrays(arr):
    MOD = 10**9 + 7
    n = len(arr)
 
    # 1) find the anchor index & its fixed value A
    anchor = next(i for i,v in enumerate(arr) if v != 0)
    A = arr[anchor]
 
    # 2) DP to the left of anchor
    dp = { A: 1 }   # at anchor, exactly one way to be at A
    for i in range(anchor-1, -1, -1):
        new_dp = {}
        if arr[i] != 0:
            L = arr[i]
            ways = (dp.get(L-1,0) + dp.get(L,0) + dp.get(L+1,0)) % MOD
            if ways == 0:
                return 0
            new_dp[L] = ways
        else:
            for y, cnt in dp.items():
                for x in (y-1, y, y+1):
                    new_dp[x] = (new_dp.get(x, 0) + cnt) % MOD
        dp = new_dp
 
    ways_left = sum(dp.values()) % MOD
 
    # 3) DP to the right of anchor
    dp = { A: 1 }
    for i in range(anchor+1, n):
        new_dp = {}
        if arr[i] != 0:
            L = arr[i]
            ways = (dp.get(L-1,0) + dp.get(L,0) + dp.get(L+1,0)) % MOD
            if ways == 0:
                return 0
            new_dp[L] = ways
        else:
            for y, cnt in dp.items():
                for x in (y-1, y, y+1):
                    new_dp[x] = (new_dp.get(x,0) + cnt) % MOD
        dp = new_dp
 
    ways_right = sum(dp.values()) % MOD
 
    # 4) combine independent halves
    return (ways_left * ways_right) % MOD
 