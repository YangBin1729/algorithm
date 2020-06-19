/*
 * @lc app=leetcode.cn id=15 lang=cpp
 *
 * [15] 三数之和
 *
 * https://leetcode-cn.com/problems/3sum/description/
 *
 * algorithms
 * Medium (24.65%)
 * Likes:    1585
 * Dislikes: 0
 * Total Accepted:    127.2K
 * Total Submissions: 516.2K
 * Testcase Example:  '[-1,0,1,2,-1,-4]'
 *
 * 给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c
 * ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。
 *
 * 注意：答案中不可以包含重复的三元组。
 *
 * 例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，
 *
 * 满足要求的三元组集合为：
 * [
 * ⁠ [-1, 0, 1],
 * ⁠ [-1, -1, 2]
 * ]
 *
 *
 */

// @lc code=start
class Solution {
  public:
    vector<vector<int>> threeSum(vector<int> &nums) {
        vector<vector<int>> results;
        sort(nums.begin(), nums.end());

        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] > 0)
                break;
            if (i > 0 && nums[i] == nums[i - 1])
                continue;
            int j = i + 1, k = nums.size() - 1;
            while (j < k) {
                int r = nums[i] + nums[j] + nums[k];
                if (r < 0) {
                    j++;
                } else if (r == 0) {
                    vector<int> temp(3, 0);
                    temp[0] = nums[i];
                    temp[1] = nums[j];
                    temp[2] = nums[k];
                    results.push_back(temp);
                    while (j + 1 < k && nums[j + 1] == temp[1])
                        j++;
                    while (j < k - 1 && nums[k - 1] == temp[2])
                        k--;
                    j++;
                    k--;
                } else {
                    k--;
                }
            }
        }
        return results;
    }
};
// @lc code=end
