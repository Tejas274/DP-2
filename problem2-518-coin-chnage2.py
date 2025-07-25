#time - o(n*amount)
#space -- o(n*amount) # n is num of coins

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        if coins == None or len(coins) == 0:
            return 0
        n = len(coins)
        dp = [[0] * (amount + 1)] * (n + 1)

        for i in range(len(coins) + 1):
            dp[i][0] = 1

        for i in range(1, n + 1):
            for j in range(1, amount + 1):
                # jya sudho coin sudhi na poche uper
                if j < coins[i - 1]:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - coins[i - 1]]

        return dp[n][amount]