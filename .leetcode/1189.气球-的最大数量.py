#
# @lc app=leetcode.cn id=1189 lang=python3
#
# [1189] “气球” 的最大数量
#
# https://leetcode-cn.com/problems/maximum-number-of-balloons/description/
#
# algorithms
# Easy (61.51%)
# Likes:    24
# Dislikes: 0
# Total Accepted:    8.5K
# Total Submissions: 13.5K
# Testcase Example:  '"nlaebolko"'
#
# 给你一个字符串 text，你需要使用 text 中的字母来拼凑尽可能多的单词 "balloon"（气球）。
#
# 字符串 text 中的每个字母最多只能被使用一次。请你返回最多可以拼凑出多少个单词 "balloon"。
#
#
#
# 示例 1：
#
#
#
# 输入：text = "nlaebolko"
# 输出：1
#
#
# 示例 2：
#
#
#
# 输入：text = "loonbalxballpoon"
# 输出：2
#
#
# 示例 3：
#
# 输入：text = "leetcode"
# 输出：0
#
#
#
#
# 提示：
#
#
# 1 <= text.length <= 10^4
# text 全部由小写英文字母组成
#
#
#


# @lc code=start
class Solution:

    def maxNumberOfBalloons(self, text: str) -> int:
        from collections import Counter
        target = Counter("balloon")
        count = Counter(text)
        if all(char in count for char in target):
            return min([count[char] // target[char] for char in target])
        return 0


# @lc code=end

text = "loonbalxballpoon"
print(Solution().maxNumberOfBalloons(text))