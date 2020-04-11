#
# @lc app=leetcode.cn id=202 lang=python3
#
# [202] 快乐数
#
# https://leetcode-cn.com/problems/happy-number/description/
#
# algorithms
# Easy (56.13%)
# Likes:    240
# Dislikes: 0
# Total Accepted:    46.3K
# Total Submissions: 80.7K
# Testcase Example:  '19'
#
# 编写一个算法来判断一个数是不是“快乐数”。
#
# 一个“快乐数”定义为：对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和，然后重复这个过程直到这个数变为 1，也可能是无限循环但始终变不到
# 1。如果可以变为 1，那么这个数就是快乐数。
#
# 示例:
#
# 输入: 19
# 输出: true
# 解释:
# 1^2 + 9^2 = 82
# 8^2 + 2^2 = 68
# 6^2 + 8^2 = 100
# 1^2 + 0^2 + 0^2 = 1
#
#
#


# @lc code=start
class Solution:

    def isHappy_1(self, n: int) -> bool:
        visited = set()
        while n != 1:
            if n in visited:     # 出现了循环
                return False
            visited.add(n)

            tmp = 0
            while n > 0:
                n, res = divmod(n, 10)
                tmp += res**2
            n = tmp
        return True


    def isHappy(self, n: int) -> bool:
        def bitsum(n):
            ans = 0
            while n>0:
                n, res = divmod(n, 10)
                ans += res**2
            return ans

        slow = bitsum(n)    # 快慢指针判断是否出现了循环
        fast = bitsum(slow)
        while slow != fast:
            slow = bitsum(slow)
            fast = bitsum(fast)
            fast = bitsum(fast)
        return slow==1


# @lc code=end
