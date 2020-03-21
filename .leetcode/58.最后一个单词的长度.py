#
# @lc app=leetcode.cn id=58 lang=python3
#
# [58] 最后一个单词的长度
#
# https://leetcode-cn.com/problems/length-of-last-word/description/
#
# algorithms
# Easy (31.65%)
# Likes:    168
# Dislikes: 0
# Total Accepted:    64K
# Total Submissions: 198.8K
# Testcase Example:  '"Hello World"'
#
# 给定一个仅包含大小写字母和空格 ' ' 的字符串 s，返回其最后一个单词的长度。
# 
# 如果字符串从左向右滚动显示，那么最后一个单词就是最后出现的单词。
# 
# 如果不存在最后一个单词，请返回 0 。
# 
# 说明：一个单词是指仅由字母组成、不包含任何空格的 最大子字符串。
# 
# 
# 
# 示例:
# 
# 输入: "Hello World"
# 输出: 5
# 
# 
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.rstrip().split(' ')[-1])



# @lc code=end

