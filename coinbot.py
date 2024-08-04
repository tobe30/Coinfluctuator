import random
import time
import msvcrt

def update_prices(prices):
    bitcoin_fluctuation = 500
    ethereum_fluctuation = 25
    solana_fluctuation = 0.9

    prev_bitcoin = prices['bitcoin']
    prev_ethereum = prices['ethereum']
    prev_solana = prices['solana']

    bitcoin_change = random.uniform(-bitcoin_fluctuation, bitcoin_fluctuation)
    ethereum_change = random.uniform(-ethereum_fluctuation, ethereum_fluctuation)
    solana_change = random.uniform(-solana_fluctuation, solana_fluctuation)

    prices['bitcoin'] += bitcoin_change
    prices['ethereum'] += ethereum_change
    prices['solana'] += solana_change

    prices['bitcoin'] = max(prices['bitcoin'], 1)
    prices['ethereum'] = max(prices['ethereum'], 1)
    prices['solana'] = max(prices['solana'], 1)

    prices['bitcoin_direction'] = "↑" if prices['bitcoin'] > prev_bitcoin else "↓"
    prices['ethereum_direction'] = "↑" if prices['ethereum'] > prev_ethereum else "↓"
    prices['solana_direction'] = "↑" if prices['solana'] > prev_solana else "↓"

    prev_bitcoin = prices['bitcoin']
    prev_ethereum = prices['ethereum']
    prev_solana = prices['solana']

    # Format the prices with commas and two decimal places
    formatted_bitcoin = f"{prices['bitcoin']:,.2f}"
    formatted_ethereum = f"{prices['ethereum']:,.2f}"
    formatted_solana = f"{prices['solana']:,.2f}"

    # Construct the output string
    output = (f"Bitcoin price: {formatted_bitcoin} {prices['bitcoin_direction']}  "
              f"Ethereum price: {formatted_ethereum} {prices['ethereum_direction']}  "
              f"Solana price: {formatted_solana} {prices['solana_direction']}")

    print(f"\r{output}", end='', flush=True)

def handle_user_input(prices):
    
 
    DATA = [
        {'words': ['what is the price of bitcoin', 'bitcoin price'], 'key': 'bitcoin'},
        {'words': ['what is the price of ethereum', 'ethereum price'], 'key': 'ethereum'},
        {'words': ['solana price', 'what is the price of solana'], 'key': 'solana'}
    ]

    print('\nEnter  : ', end='', flush=True)
    response = input().strip().lower()
    has_response = False

    for data in DATA:
        for accepted_word in data['words']:
            if accepted_word in response:
                has_response = True
                key = data['key']
                formatted_price = f"{prices[key]:,.2f}"
                direction = prices[f'{key}_direction']
                print(f'\nbot: {key.capitalize()} price: {formatted_price} {direction}')
                break
        if has_response:
            break

    if not has_response:
        print("Sorry, I don't understand that I only give you price of 3 coins.")

def main():
    prices = {
        'bitcoin': 60000,
        'ethereum': 3000,
        'solana': 141,
        'bitcoin_direction': '',
        'ethereum_direction': '',
        'solana_direction': ''
    }
    
    print("coinbot- Hey, I'm a coinbot. Want to see the market today (type 'yes' to start): ")
    start = input().strip().lower()
    if start == 'yes':
        while True:
            update_prices(prices)
            time.sleep(1.5)
            
            if msvcrt.kbhit():
                handle_user_input(prices)
    else:
        print('Wrong answer input yes/no')

main()
