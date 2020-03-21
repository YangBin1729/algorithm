/*
 * @lc app=leetcode.cn id=70 lang=javascript
 *
 * [70] 爬楼梯
 *
 * https://leetcode-cn.com/problems/climbing-stairs/description/
 *
 * algorithms
 * Easy (47.34%)
 * Likes:    736
 * Dislikes: 0
 * Total Accepted:    109K
 * Total Submissions: 230.3K
 * Testcase Example:  '2'
 *
 * 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
 * 
 * 每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
 * 
 * 注意：给定 n 是一个正整数。
 * 
 * 示例 1：
 * 
 * 输入： 2
 * 输出： 2
 * 解释： 有两种方法可以爬到楼顶。
 * 1.  1 阶 + 1 阶
 * 2.  2 阶
 * 
 * 示例 2：
 * 
 * 输入： 3
 * 输出： 3
 * 解释： 有三种方法可以爬到楼顶。
 * 1.  1 阶 + 1 阶 + 1 阶
 * 2.  1 阶 + 2 阶
 * 3.  2 阶 + 1 阶
 * 
 * 
 */

// @lc code=start
/**
 * @param {number} n
 * @return {number}
 */
var climbStairs = function (n) {
    // let f1 = 1,
    //     f2 = 1,
    //     f3 = 1;
    // for (let i = 1; i < n; i++) {
    //     f3 = f1 + f2;
    //     f1 = f2;
    //     f2 = f3;
    // }
    // return f3;
    var sqrt5 = Math.sqrt(5);
    var pow =  Math.pow((1+sqrt5)/2,n+1) - Math.pow((1-sqrt5)/2,n+1);
    return Math.round( pow/sqrt5 );
};
// @lc code=end

