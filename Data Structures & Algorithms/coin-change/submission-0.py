class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Suproblems: The minimum number of coins to make up an amount i (which is smaller than n)
        # OPT(i) = min( OPT(i-1), i) -> meaning the optimal way to make i-1th coins, or take i because a coin can fulfill it
        
        # Each cache value represents increasing amounts, starting from 0.
        cache = [20000] * (amount+1)
        cache[0] = 0

        for i in range(1,amount+1):
            for coin in coins:
                if i - coin >= 0:
                    cache[i] = min(cache[i], 1 + cache[i - coin])
        
        return cache[amount] if (cache[amount] != 20000) else -1


        