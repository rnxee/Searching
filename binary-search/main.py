# binary-search Function
def find_price(prices, target):
    first = 0
    last = len(prices) - 1
    while first <= last: # Loop the search while First <= last
        mid = (first + last) // 2
        if prices[mid] == target: # If mid = target then return mid
            return mid
        elif prices[mid] > target: # If mid > target then we disregard right side
            last = mid - 1
        else:       # But if mid < target then we disregard left side
            first = mid + 1
    return -1


def get_prices(gadgets):
    prices = sorted(int(i) for i in input("Prices: ").split())
    prices = prices[:gadgets] # Remove excess items
    return prices


def main():
    cases = int(input("Enter No. of Test Cases: "))  # Number of Test Cases
    results = [] # Stores the result

    for i in range(cases):  # For every cases run this block of Code
        gadgets = int(input(f"\nCase {i+1}: Enter No. of Gadgets: "))
        prices = get_prices(gadgets) # Gets Gadgets prices
        target = int(input("Enter Target Price: "))

        result = find_price(prices, target) # Identifies if price is available

        if result != -1:
            results.append(f"Available")
        else:
            results.append(f"Not available")

    print("\nResults:")
    for i, r in enumerate(results):
        print(f"Case {i + 1}: {r}")

main()