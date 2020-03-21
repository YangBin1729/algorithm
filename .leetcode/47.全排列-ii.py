#
# @lc app=leetcode.cn id=47 lang=python3
#
# [47] 全排列 II
#
# https://leetcode-cn.com/problems/permutations-ii/description/
#
# algorithms
# Medium (55.88%)
# Likes:    188
# Dislikes: 0
# Total Accepted:    31.2K
# Total Submissions: 55.7K
# Testcase Example:  '[1,1,2]'
#
# 给定一个可包含重复数字的序列，返回所有不重复的全排列。
#
# 示例:
#
# 输入: [1,1,2]
# 输出:
# [
# ⁠ [1,1,2],
# ⁠ [1,2,1],
# ⁠ [2,1,1]
# ]
#
#


# @lc code=start
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # 46.全排列的解法中添加判断条件：tmp not in res
        # res = []
        # def backtrack(nums, tmp):
        #     if not nums and tmp not in res:
        #         res.append(tmp)
        #     for i in range(len(nums)):
        #         backtrack(nums[:i] + nums[i + 1:], tmp + [nums[i]])

        # backtrack(nums, [])

        # TODO:
 


# @lc code=end
