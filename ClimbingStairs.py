#######  FileName = ClimbingStairs.py

'''You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the
top'''

''' the for the n steps, you can climb (n-1)steps and then climb 1 steps, or you can climb
to n-2 steps then 2 steps. so f(n) = f(n-1)+f(n-2)'''

class Solution:
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
        f = [1 for i in range(n+1)]
        for n in range(2,n+1):
            f[n] = f[n-1] + f[n-2]
        return f[n]
