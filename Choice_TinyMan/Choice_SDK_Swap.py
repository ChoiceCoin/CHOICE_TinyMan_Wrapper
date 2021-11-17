# Copyright Fortior Blockchain, LLLP 2021
#Type python Choice_SDK.py in a directory with all the runsteps to run this file
from tinyman.v1.client import TinymanTestnetClient
from algosdk.v2client import algod
from algosdk import account, encoding, mnemonic,transaction

print("Welcome to the custom Choice-TinyMan Terminal Wrapper! Please enter your mnemonic and address to sign transactions manually.")
user_mnemonic = ""
address = ""

private_key = mnemonic.to_private_key(user_mnemonic)
client = TinymanTestnetClient(user_address = address)

if(not client.is_opted_in()):
    print('Account not opted into TinyMan app, opting in now..')
    transaction_group = client.prepare_app_optin_transactions()
    transaction_group.sign_with_private_key(address, account['private_key'])
    result = client.submit(transaction_group, wait=True)

def choice_for_algo():
    Choice = client.fetch_asset(17263578)
    ALGO = client.fetch_asset(0)
    pool = client.fetch_pool(Choice, ALGO)
    quote = pool.fetch_fixed_input_swap_quote(ALGO(1_000_000), slippage=0.01)
    print(quote)
    print(f'Choice per ALGO: {quote.price}')
    print(f'Choice per ALGO (worst case): {quote.price_with_slippage}')
    print("Do you still want to go through this transaction? Type Y for 'Yes' and N for 'No'")
    binary = input()
    if binary == "Y":
        new = int(input("How much ALGO do you want to spend? ")) * 1000000
        quote = pool.fetch_fixed_input_swap_quote(ALGO(new), slippage=0.01)
        print(f'Swapping {quote.amount_in} to {quote.amount_out_with_slippage}')
        transaction_group = pool.prepare_swap_transactions_from_quote(quote)
            # Sign the group with our key
        transaction_group.sign_with_private_key(address, private_key)
            # Submit transactions to the network and wait for confirmation
        result = client.submit(transaction_group, wait=True)

    # Check if any excess remaining after the swap
    excess = pool.fetch_excess_amounts()
    if Choice in excess:
        amount = excess[Choice]
        print(f'Excess: {amount}')
        if amount > 1_000_000:
            transaction_group = pool.prepare_redeem_transactions(amount)
            transaction_group.sign_with_private_key(address, private_key)
            result = client.submit(transaction_group, wait=True)
    else:
        print('Returning to wrapper home')

def choice_for_usdc():
        Choice = client.fetch_asset(17263578)
        USDC = client.fetch_asset(21582668)
        pool = client.fetch_pool(Choice, USDC)

        quote = pool.fetch_fixed_input_swap_quote(USDC(1_000_000), slippage=0.01)
        print(quote)
        print(f'Choice per USDC: {quote.price * 10000}')
        print(f'Choice per USDC (worst case): {quote.price_with_slippage * 10000}')
        print("Do you still want to go through this transaction? Type Y for 'Yes' and N for 'No'")
        binary = input()
        if binary == "Y":
            new = int(input("How much USDC do you want to spend? ")) * 1000000
            quote = pool.fetch_fixed_input_swap_quote(USDC(new), slippage=0.01)
            print(f'Swapping {quote.amount_in} to {quote.amount_out_with_slippage}')
            transaction_group = pool.prepare_swap_transactions_from_quote(quote)
                # Sign the group with our key
            transaction_group.sign_with_private_key(address, private_key)
                # Submit transactions to the network and wait for confirmation
            result = client.submit(transaction_group, wait=True)

        # Check if any excess remaining after the swap
        excess = pool.fetch_excess_amounts()
        if Choice in excess:
            amount = excess[Choice]
            print(f'Excess: {amount}')
            if amount > 1_000_000:
                transaction_group = pool.prepare_redeem_transactions(amount)
                transaction_group.sign_with_private_key(address, private_key)
                result = client.submit(transaction_group, wait=True)

def choice_for_YLDY():
        Choice = client.fetch_asset(17263578)
        YLDY = client.fetch_asset(22847688)
        pool = client.fetch_pool(Choice, YLDY)

        quote = pool.fetch_fixed_input_swap_quote(YLDY(1_000_000), slippage=0.01)
        print(quote)
        print(f'Choice per YLDY: {quote.price * 10000}')
        print(f'Choice per YLDY (worst case): {quote.price_with_slippage * 10000}')
        print("Do you still want to go through this transaction?")
        print("Type Y for 'Yes' and N for 'No'") 
        binary = input()
        if binary == "Y":
            new = int(input("How much YLDY do you want to spend? ")) * 1000000
            quote = pool.fetch_fixed_input_swap_quote(YLDY(new), slippage=0.01)
            print(f'Swapping {quote.amount_in} to {quote.amount_out_with_slippage}')
            transaction_group = pool.prepare_swap_transactions_from_quote(quote)
            # Sign the group with our key
            transaction_group.sign_with_private_key(address, private_key)
            # Submit transactions to the network and wait for confirmation
            result = client.submit(transaction_group, wait=True)

        # Check if any excess remaining after the swap
        excess = pool.fetch_excess_amounts()
        if Choice in excess:
            amount = excess[Choice]
            print(f'Excess: {amount}')
            if amount > 1_000_000:
                transaction_group = pool.prepare_redeem_transactions(amount)
                transaction_group.sign_with_private_key(address, private_key)
                result = client.submit(transaction_group, wait=True)

user_input = "Go"
while user_input == "Go":
    print("What swaps do you want to make with Choice? ")
    print("Type 'ALGO' to trade Choice for Algo. ")  
    print("Type 'USDC' to trade Choice for USDC. ")
    print("Type 'YLDY' to trade Choice for YLDY. ")
    print("Type 'Stop' to stop the program. ")
    user = input()
    if user == "Stop":
        user_input = 'Stop'
    elif user == 'ALGO':
        choice_for_algo()
    elif user == 'USDC':
        choice_for_usdc()
    elif user == 'YlDY':
        choice_for_YLDY()
