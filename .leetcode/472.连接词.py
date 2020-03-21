#
# @lc app=leetcode.cn id=472 lang=python3
#
# [472] 连接词
#
# https://leetcode-cn.com/problems/concatenated-words/description/
#
# algorithms
# Hard (43.62%)
# Likes:    24
# Dislikes: 0
# Total Accepted:    2K
# Total Submissions: 4.5K
# Testcase Example:  '["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]'
#
# 给定一个不含重复单词的列表，编写一个程序，返回给定单词列表中所有的连接词。
#
# 连接词的定义为：一个字符串完全是由至少两个给定数组中的单词组成的。
#
# 示例:
#
#
# 输入:
# ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
#
# 输出: ["catsdogcats","dogcatsdog","ratcatdogcat"]
#
# 解释: "catsdogcats"由"cats", "dog" 和 "cats"组成;
# ⁠    "dogcatsdog"由"dog", "cats"和"dog"组成;
# ⁠    "ratcatdogcat"由"rat", "cat", "dog"和"cat"组成。
#
#
# 说明:
#
#
# 给定数组的元素总数不超过 10000。
# 给定数组中元素的长度总和不超过 600000。
# 所有输入字符串只包含小写字母。
# 不需要考虑答案输出的顺序。
#
#
#

from typing import List


# @lc code=start
class Solution:

    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        # TODO
        # 错误！！！
        wordSet = set(words)
        res = []
        for word in words:
            dp = [0] * (len(word) + 1)
            dp[0] = 1
            for i in range(1, len(word) + 1):
                for j in range(i):
                    if dp[j] and word[j:i] in wordSet:
                        dp[i] = 1
                        break
            if dp[-1] == 1 and sum(dp) > 2:
                res.append(word)
        return res


# @lc code=end

words = ["cat", "cats", "catsdogcats", "dog", "dogcatsdog", "hippopotamuses", "rat", "ratcatdogcat"]
Solution().findAllConcatenatedWordsInADict(words)