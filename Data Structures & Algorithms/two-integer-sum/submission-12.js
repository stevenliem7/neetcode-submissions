class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        // 3: 0, 4: 1, 5: 2
        let mapp = new Map();
        for (let i = 0; i < nums.length; i++) {
            let diff  = target - nums[i];
            if (mapp.has(diff)) { return [mapp.get(diff), i]; }
            mapp.set(nums[i], i);
            }
        }

    }
