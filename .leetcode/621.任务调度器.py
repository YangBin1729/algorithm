#
# @lc app=leetcode.cn id=621 lang=python3
#
# [621] 任务调度器
#
# https://leetcode-cn.com/problems/task-scheduler/description/
#
# algorithms
# Medium (46.14%)
# Likes:    207
# Dislikes: 0
# Total Accepted:    15.2K
# Total Submissions: 31.7K
# Testcase Example:  '["A","A","A","B","B","B"]\n2'
#
# 给定一个用字符数组表示的 CPU 需要执行的任务列表。其中包含使用大写的 A - Z 字母表示的26
# 种不同种类的任务。任务可以以任意顺序执行，并且每个任务都可以在 1 个单位时间内执行完。CPU 在任何一个单位时间内都可以执行一个任务，或者在待命状态。
#
# 然而，两个相同种类的任务之间必须有长度为 n 的冷却时间，因此至少有连续 n 个单位时间内 CPU 在执行不同的任务，或者在待命状态。
#
# 你需要计算完成所有任务所需要的最短时间。
#
# 示例 1：
#
#
# 输入: tasks = ["A","A","A","B","B","B"], n = 2
# 输出: 8
# 执行顺序: A -> B -> (待命) -> A -> B -> (待命) -> A -> B.
#
#
# 注：
#
#
# 任务的总个数为 [1, 10000]。
# n 的取值范围为 [0, 100]。
#
#
#

from typing import List


# @lc code=start
class Solution:

    def leastInterval(self, tasks: List[str], n: int) -> int:
        # TODO:任务种类数多于间隔时间时？
        from collections import Counter
        m = len(tasks)
        if m <= 1:
            return m

        tasks = Counter(tasks).most_common()
        max_cnt = tasks[0][1]

        res = (max_cnt - 1) * (n + 1)

        for task in tasks:
            if task[1] == max_cnt:
                res += 1
        return res if res >= m else m


# @lc code=end

tasks = ["A", "A", "A", "B", "B", "B", "C", "C", "C", "D", "D"]
n = 2
print(Solution().leastInterval(tasks, n))
