#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#
# https://leetcode-cn.com/problems/longest-common-prefix/description/
#
# algorithms
# Easy (35.45%)
# Likes:    848
# Dislikes: 0
# Total Accepted:    175.4K
# Total Submissions: 489.3K
# Testcase Example:  '["flower","flow","flight"]'
#
# 编写一个函数来查找字符串数组中的最长公共前缀。
#
# 如果不存在公共前缀，返回空字符串 ""。
#
# 示例 1:
#
# 输入: ["flower","flow","flight"]
# 输出: "fl"
#
#
# 示例 2:
#
# 输入: ["dog","racecar","car"]
# 输出: ""
# 解释: 输入不存在公共前缀。
#
#
# 说明:
#
# 所有输入只包含小写字母 a-z 。
#
#
from typing import List


# @lc code=start
class Solution:

    def longestCommonPrefix_1(self, strs: List[str]) -> str:
        if not strs:
            return ""
        ans = strs[0]
        for i in range(1, len(strs)):
            j = 0
            while j < len(ans) and j < len(strs[i]):
                if ans[j] == strs[i][j]:
                    j += 1
                else:
                    break
            ans = ans[:j]
        return ans

# @lc code=end
