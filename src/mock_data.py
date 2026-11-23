# This file handles mock data randomization
from random import uniform

def generate_mock_price():
    random_mock_price = round(uniform(-5, 25), 2)
    return random_mock_price


if __name__ == "__main__":
    print(generate_mock_price())