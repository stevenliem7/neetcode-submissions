class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    maxSubArray(nums) {

        if (nums.length === 1) {
            return nums[0];
        }

        let best = -10000;
        let curr = 0;
        for (let n of nums) {
            // If max goes under 0, restart
            // otherwise, continue the sum
            curr += n;

            if (curr > best) {
                best = curr;
            }
            if (curr < 0) {
                curr = 0;
            }

            console.log(best);
        }
    return best;
    }
}
