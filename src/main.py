# Main loop runs here
from pricing import pricing
from mock_data import generate_mock_price

from leds import display_price_category


def main():
    current_price = generate_mock_price()
    price_category = pricing(current_price)
    display_price_category(price_category)
    
    print(f"Electricity price: {current_price}c/kWh")
    print(f"Price category: {price_category}")
    
if __name__ == "__main__":
    main()