#
# @lc app=leetcode.cn id=500 lang=python3
#
# [500] 键盘行
#
# https://leetcode-cn.com/problems/keyboard-row/description/
#
# algorithms
# Easy (67.82%)
# Likes:    84
# Dislikes: 0
# Total Accepted:    15.3K
# Total Submissions: 22.3K
# Testcase Example:  '["Hello","Alaska","Dad","Peace"]'
#
# 给定一个单词列表，只返回可以使用在键盘同一行的字母打印出来的单词。键盘如下图所示。
# 
# 
# 
# 
# 
# 
# 
# 示例：
# 
# 输入: ["Hello", "Alaska", "Dad", "Peace"]
# 输出: ["Alaska", "Dad"]
# 
# 
# 
# 
# 注意：
# 
# 
# 你可以重复使用键盘上同一字符。
# 你可以假设输入的字符串将只包含字母。
# 
#

from typing import List

# @lc code=start
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        a = set('qwertyuiop')
        b = set('asdfghjkll')
        c = set('zxcvbnm')

        res = []
        for word in words:
            for chars in [a, b, c]:
                if all([c.lower() in chars for c in word]):
                    res.append(word)
                    break
        return res
        
# @lc code=end

