#!/usr/bin/python3
""" Defines the function makeChange """


def makeChange(coins, total):
    """
        Determines the fewest number of coins needed to meet a given
        amount total from a pile of coins of different values in other
        to make change
    """
    # Initialize an array to store the minimum number of coins needed
    # for each value from 0 to 'total'.
    # Initialize the array with a large value to represent infinity.
    dp = [float('inf')] * (total + 1)

    # The minimum number of coins needed to make change for 0 is 0.
    dp[0] = 0

    # Iterate through each coin denomination.
    for coin in coins:
        # Update the dp array for each possible total value.
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    # If dp[total] is still infinity, it means it's not possible
    # to make change for the given total.
    if dp[total] == float('inf'):
        return -1
    else:
        return dp[total]
