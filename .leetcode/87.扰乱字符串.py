#
# @lc app=leetcode.cn id=87 lang=python3
#
# [87] 扰乱字符串
#
# https://leetcode-cn.com/problems/scramble-string/description/
#
# algorithms
# Hard (44.47%)
# Likes:    83
# Dislikes: 0
# Total Accepted:    6.7K
# Total Submissions: 15K
# Testcase Example:  '"great"\n"rgeat"'
#
# 给定一个字符串 s1，我们可以把它递归地分割成两个非空子字符串，从而将其表示为二叉树。
#
# 下图是字符串 s1 = "great" 的一种可能的表示形式。
#
# ⁠   great
# ⁠  /    \
# ⁠ gr    eat
# ⁠/ \    /  \
# g   r  e   at
# ⁠          / \
# ⁠         a   t
#
#
# 在扰乱这个字符串的过程中，我们可以挑选任何一个非叶节点，然后交换它的两个子节点。
#
# 例如，如果我们挑选非叶节点 "gr" ，交换它的两个子节点，将会产生扰乱字符串 "rgeat" 。
#
# ⁠   rgeat
# ⁠  /    \
# ⁠ rg    eat
# ⁠/ \    /  \
# r   g  e   at
# ⁠          / \
# ⁠         a   t
#
#
# 我们将 "rgeat” 称作 "great" 的一个扰乱字符串。
#
# 同样地，如果我们继续交换节点 "eat" 和 "at" 的子节点，将会产生另一个新的扰乱字符串 "rgtae" 。
#
# ⁠   rgtae
# ⁠  /    \
# ⁠ rg    tae
# ⁠/ \    /  \
# r   g  ta  e
# ⁠      / \
# ⁠     t   a
#
#
# 我们将 "rgtae” 称作 "great" 的一个扰乱字符串。
#
# 给出两个长度相等的字符串 s1 和 s2，判断 s2 是否是 s1 的扰乱字符串。
#
# 示例 1:
#
# 输入: s1 = "great", s2 = "rgeat"
# 输出: true
#
#
# 示例 2:
#
# 输入: s1 = "abcde", s2 = "caebd"
# 输出: false
#
#


# @lc code=start
class Solution:

    def isScramble_1(self, s1: str, s2: str) -> bool:
        """
        递归：
        """
        if s1 == s2:
            return True
        if sorted(s1) != sorted(s2):
            return False

        for i in range(1, len(s1)):
            if self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]):
                return True
            if self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:], s2[:-i]):
                return True
        return False

    def isScramble(self, s1: str, s2: str) -> bool:
        """
        TODO: 动态规划：
        dp[i][j][len] 表示 s1[i:i+len] 与 s2[j:j+len] 是否为扰乱字符串
        """
        n = len(s1)
        dp = [[[0] * (n + 1) for _ in range(n)] for i in range(n)]

        for length in range(1, n + 1):
            for i in range(n - length + 1):
                for j in range(n - length + 1):
                    if length == 1 and s1[i:i + length] == s2[j:j + length]:
                        dp[i][j][length] = 1
                    else:
                        for sub_length in range(1, length):
                            if (dp[i][j][sub_length] and
                                    dp[i + sub_length][j + sub_length][length - sub_length]
                               ) or (dp[i][j + length - sub_length][sub_length] and
                                     dp[i + length - sub_length][j][length - sub_length]):
                                dp[i][j][length] = 1

        return bool(dp[0][0][n])


# @lc code=end

s1 = "abc"
s2 = "cba"
print(Solution().isScramble(s1, s2))