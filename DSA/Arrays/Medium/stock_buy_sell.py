from typing import List

def max_profit(prices: List[int]) -> int:
    """
    Calculates the maximum profit from buying and selling a stock.
    You can only complete at most one transaction.
    """
    current_min_price = float('inf')
    max_profit = 0
    for price in prices:
        current_min_price = min(current_min_price, price)
        max_profit = max(max_profit, price - current_min_price)
    return max_profit

if __name__ == "__main__":
    prices = [7, 1, 5, 3, 6, 4]
    profit = max_profit(prices)
    print(f"The maximum profit is: {profit}")

    prices = [7, 6, 4, 3, 1]
    profit = max_profit(prices)
    print(f"The maximum profit is: {profit}")