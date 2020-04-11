#
# @lc app=leetcode.cn id=1002 lang=python3
#
# [1002] 查找常用字符
#
# https://leetcode-cn.com/problems/find-common-characters/description/
#
# algorithms
# Easy (65.27%)
# Likes:    59
# Dislikes: 0
# Total Accepted:    10.8K
# Total Submissions: 16.1K
# Testcase Example:  '["bella","label","roller"]'
#
# 给定仅有小写字母组成的字符串数组 A，返回列表中的每个字符串中都显示的全部字符（包括重复字符）组成的列表。例如，如果一个字符在每个字符串中出现 3
# 次，但不是 4 次，则需要在最终答案中包含该字符 3 次。
#
# 你可以按任意顺序返回答案。
#
#
#
# 示例 1：
#
# 输入：["bella","label","roller"]
# 输出：["e","l","l"]
#
#
# 示例 2：
#
# 输入：["cool","lock","cook"]
# 输出：["c","o"]
#
#
#
#
# 提示：
#
#
# 1 <= A.length <= 100
# 1 <= A[i].length <= 100
# A[i][j] 是小写字母
#
#
#

from typing import List


# @lc code=start
class Solution:

    def commonChars(self, A: List[str]) -> List[str]:
        from collections import Counter
        counts = [Counter(s) for s in A]
        res = []
        for char in counts[0]:
            if all([char in count for count in counts[1:]]):
                cnt = min([count[char] for count in counts])
                for _ in range(cnt):
                    res.append(char)
        return res


# @lc code=end

A = ["cool", "lock", "cook"]
print(Solution().commonChars(A))