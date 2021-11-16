#Copyright Fortior Blockchain, LLLP 2021
#Type python Choice_SDK.py in a directory with all the runsteps to run this file
#Be sure to enter your mnemonic and address in lines 9-10 beforehand. 
from tinyman.v1.client import TinymanMainnetClient
from algosdk.v2client import algod
from algosdk import account, encoding, mnemonic,transaction

print("Welcome to the custom Choice-TinyMan Terminal Wrapper!.")
user_mnemonic = ""
address = ""
private_key = mnemonic.to_private_key(user_mnemonic)
client = TinymanMainnetClient(user_address = address)

def choice_for_algo():
    Choice = client.fetch_asset(297995609)
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

choice_for_algo()

def choice_for_usdc():
        Choice = client.fetch_asset(297995609)
        USDC = client.fetch_asset(31566704)
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
        Choice = client.fetch_asset(297995609)
        YLDY = client.fetch_asset(226701642)
        pool = client.fetch_pool(Choice, YLDY)

        quote = pool.fetch_fixed_input_swap_quote(YLDY(1_000_000), slippage=0.01)
        print(quote)
        print(f'Choice per YLDY: {quote.price * 10000}')
        print(f'Choice per YLDY (worst case): {quote.price_with_slippage * 10000}')
        print("Do you still want to go through this transaction? Type Y for 'Yes' and N for 'No'")
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

def choice_for_comand():
    Choice = client.fetch_asset(297995609)
    comand = client.fetch_asset(330109984)
    pool = client.fetch_pool(Choice, comand)

    quote = pool.fetch_fixed_input_swap_quote(comand(1_000_000), slippage=0.01)
    print(quote)
    print(f'Choice per comand: {quote.price * 10000}')
    print(f'Choice per comand (worst case): {quote.price_with_slippage * 10000}')
    print("Do you still want to go through this transaction? Type Y for 'Yes' and N for 'No'")
    binary = input()
    if binary == "Y":
        new = int(input("How much comand do you want to spend? ")) * 1000000
        quote = pool.fetch_fixed_input_swap_quote(comand(new), slippage=0.01)
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
 
def choice_for_ACORN():
    Choice = client.fetch_asset(297995609)
    ACORN = client.fetch_asset(226265212)
    pool = client.fetch_pool(Choice, ACORN)

    quote = pool.fetch_fixed_input_swap_quote(ACORN(1_000_000), slippage=0.01)
    print(quote)
    print(f'Choice per ACORN: {quote.price * 10000}')
    print(f'Choice per ACORN (worst case): {quote.price_with_slippage * 10000}')
    print("Do you still want to go through this transaction? Type Y for 'Yes' and N for 'No'")
    binary = input()
    if binary == "Y":
        new = int(input("How much comand do you want to spend? ")) * 1000000
        quote = pool.fetch_fixed_input_swap_quote(ACORN(new), slippage=0.01)
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
