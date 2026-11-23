# This file handles pricing logic
from config import CHEAP_THRESHOLD, EXPENSIVE_THRESHOLD
from mock_data import generate_mock_price

# Function for pricing
def pricing(price):
    if price < CHEAP_THRESHOLD: # Price lower than 5c/kWh
        category = "cheap"
    elif price >= EXPENSIVE_THRESHOLD: # Price equal to or over 15c/kWh 
        category = "expensive"
    else:
        category = "moderate" # Price between 5c/kWh & 15c/kWh
    return category

if __name__ == "__main__":
    print(pricing(generate_mock_price()))