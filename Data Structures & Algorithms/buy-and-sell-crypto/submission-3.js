class Solution {
    /**
     * @param {number[]} prices
     * @return {number}
     */
    maxProfit(prices) {
        let maxProfit = 0;
        let sellPrice = 0;
        let l = 0, r = 1;

        while (r < prices.length) {
            if (prices[l] > prices[r] ) {
                l = r;
            }
            else if (sellPrice < prices[r]) {
                 maxProfit = Math.max(prices[r] - prices[l], maxProfit);
            }
            r+=1;
        }
        return maxProfit;
    }
}
