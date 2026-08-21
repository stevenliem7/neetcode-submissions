class Solution {
    /**
     * @param {number[]} prices
     * @return {number}
     */
    maxProfit(prices) {
        let buyPrice = prices[0];
        let sellPrice = 0;
        let maxProfit = 0;
        let l, r = 0;

        while (r < prices.length) {
            if (buyPrice > prices[r] ) {
                buyPrice = prices[r];
                l = r;
                r+=1;
                sellPrice = buyPrice;
            }
            else if (sellPrice < prices[r]) {
                sellPrice = prices[r];
                r+=1;
            }
            else { r+=1; }
            maxProfit = Math.max(sellPrice - buyPrice, maxProfit);
            console.log(buyPrice, sellPrice);
        }
        return maxProfit;
    }
}
