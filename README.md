# Stock Price Analyzer

This Python program allows users to analyze a list of stock prices. Users can input a new list of prices, print the current prices, find the latest price, calculate the average price, find the minimum price and its day, find the maximum single-day change and its day, test a threshold to see if any prices exceed it, and plan their investment strategy by finding the best days to buy and sell.

## How to Use

1. Run the program.
2. Select an option from the menu:
   - (0) Input a new list of prices
   - (1) Print the current prices
   - (2) Find the latest price
   - (3) Find the average price
   - (4) Find the min price and its day
   - (5) Find the max single-day change and its day
   - (6) Test a threshold
   - (7) Your investment plan
   - (8) Quit

## Functions

- `display_menu()`: Prints the menu of options.
- `get_new_prices()`: Gets a new list of prices from the user.
- `print_prices(prices)`: Prints the current list of prices.
- `latest_price(prices)`: Returns the latest price in the list.
- `avg_price(prices)`: Computes and returns the average price.
- `min_day(prices)`: Computes and returns the day of the minimum price.
- `max_change_day(prices)`: Computes and returns the day of the maximum single-day change in price.
- `any_above(prices, threshold)`: Determines if there are any prices above a given threshold.
- `find_tts(prices)`: Finds the best days to buy and sell the stock for maximum profit.
