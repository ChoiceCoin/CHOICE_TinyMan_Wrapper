#Copyright Fortior Blockchain, LLLP 2021
#Type python Choice_SDK.py in a directory with all the runsteps to run this file
#Be sure to enter your mnemonic and address in lines 9-10 beforehand. 


#Overview
#This tutorial is a guide to using the terminal wrapper for Choice Coin and TinyMan. 
#The CHOICE_TinyMan_Wrapper is meant to allow individuals in the Choice Coin Ecosystem to obtain the asset directly through their terminal.

# Requirements
##################################
# All requirements for this Tutorial can be found in the [requirements.txt](https://github.com/ChoiceCoin/CHOICE_TinyMan_Wrapper/blob/main/requirements.txt) file on the Choice Coin GitHub. 
# To install the requirements run: 

pip install requirements.txt

# Steps
##################################
# 1. Import the TinyMan Client for MainNet, and the Algod Client for connecting to Algorand
from tinyman.v1.client import TinymanMainnetClient
from algosdk.v2client import algod
from algosdk import account, encoding, mnemonic,transaction

print("Welcome to the custom Choice-TinyMan Terminal Wrapper!.")

# 2. Copy your address and mnemonic here, which can be found in your Algorand Wallet
address = ""
user_mnemonic = ""
private_key = mnemonic.to_private_key(user_mnemonic)
client = TinymanMainnetClient(user_address = address)
if(not client.is_opted_in()):
    print('Account not opted into TinyMan app, opting in now..')
    transaction_group = client.prepare_app_optin_transactions()
    transaction_group.sign_with_private_key(address, account['private_key'])
    result = client.submit(transaction_group, wait=True)
# 3. Each of the functions below enable the user to swap for Choice Coin on TinyMan using another digital asset. Currently, this wrapper supports ALGO, USDC, YLDY, GEMS, TACOS, and more.
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


def choice_for_OPUL():
        Choice = client.fetch_asset(297995609)
        OPUL = client.fetch_asset(287867876)
        pool = client.fetch_pool(Choice, OPUL)

        quote = pool.fetch_fixed_input_swap_quote(OPUL(1_000_000), slippage=0.01)
        print(quote)
        print(f'Choice per OPUL: {quote.price * 10000}')
        print(f'Choice per OPUL (worst case): {quote.price_with_slippage * 10000}')
        print("Do you still want to go through this transaction? Type Y for 'Yes' and N for 'No'")
        binary = input()
        if binary == "Y":
            new = int(input("How much OPUL do you want to spend? ")) * 1000000
            quote = pool.fetch_fixed_input_swap_quote(OPUL(new), slippage=0.01)
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

def choice_for_TACO():
        Choice = client.fetch_asset(297995609)
        TACO = client.fetch_asset(329110405)
        pool = client.fetch_pool(Choice, TACO)

        quote = pool.fetch_fixed_input_swap_quote(TACO(1_000_000), slippage=0.01)
        print(quote)
        print(f'Choice per TACO: {quote.price * 10000}')
        print(f'Choice per TACO (worst case): {quote.price_with_slippage * 10000}')
        print("Do you still want to go through this transaction? Type Y for 'Yes' and N for 'No'")
        binary = input()
        if binary == "Y":
            new = int(input("How much TACO do you want to spend? ")) * 1000000
            quote = pool.fetch_fixed_input_swap_quote(TACO(new), slippage=0.01)
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

def choice_for_GEMS():
        Choice = client.fetch_asset(297995609)
        GEMS = client.fetch_asset(230946361)
        pool = client.fetch_pool(Choice, GEMS)

        quote = pool.fetch_fixed_input_swap_quote(GEMS(1_000_000), slippage=0.01)
        print(quote)
        print(f'Choice per GEMS: {quote.price * 10000}')
        print(f'Choice per GEMS (worst case): {quote.price_with_slippage * 10000}')
        print("Do you still want to go through this transaction? Type Y for 'Yes' and N for 'No'")
        binary = input()
        if binary == "Y":
            new = int(input("How much GEMS do you want to spend? ")) * 1000000
            quote = pool.fetch_fixed_input_swap_quote(GEMS(new), slippage=0.01)
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
   
def choice_for_AKITA():
    Choice = client.fetch_asset(297995609)
    AKITA = client.fetch_asset(384303832)
    pool = client.fetch_pool(Choice, AKITA)

    quote = pool.fetch_fixed_input_swap_quote(AKITA(1_000_000), slippage=0.01)
    print(quote)
    print(f'Choice per AKITA: {quote.price * 10000}')
    print(f'Choice per AKITA (worst case): {quote.price_with_slippage * 10000}')
    print("Do you still want to go through this transaction? Type Y for 'Yes' and N for 'No'")
    binary = input()
    if binary == "Y":
        new = int(input("How much AKITA do you want to spend? ")) * 1000000
        quote = pool.fetch_fixed_input_swap_quote(AKITA(new), slippage=0.01)
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

def choice_for_HDL():
    Choice = client.fetch_asset(297995609)
    HDL = client.fetch_asset(137594422)
    pool = client.fetch_pool(Choice, HDL)

    quote = pool.fetch_fixed_input_swap_quote(HDL(1_000_000), slippage=0.01)
    print(quote)
    print(f'Choice per HDL: {quote.price * 10000}')
    print(f'Choice per HDL (worst case): {quote.price_with_slippage * 10000}')
    print("Do you still want to go through this transaction? Type Y for 'Yes' and N for 'No'")
    binary = input()
    if binary == "Y":
        new = int(input("How much HDL do you want to spend? ")) * 1000000
        quote = pool.fetch_fixed_input_swap_quote(HDL(new), slippage=0.01)
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
# 4. Run the following command to start the program, once you are in the proper directory with the virtual environment active.
python CHOICE_TinyMan_Wrapper.py
#Follow the instructions below to pick a specific asset, once the program has started. The program will allow you to make swaps as long as it is active. 
user_input = "Go"
while user_input == "Go":
    # If you add extra ASAs, make sure to add the function below. 
    print("What swaps do you want to make with Choice? \n 1. Type 'ALGO' to trade for Choice with Algo. \n 2. Type 'USDC' to trade for Choice with USDC. \n 3. Type 'YLDY' to trade for Choice with Yieldy. \n 4. Type 'OPUL' to trade for Choice with Opulous \n 5. Type 'TACO' to trade for Choice with TACO \n 6. Type 'HDL' to trade for Choice with HDL \n 7. Type 'comand' to trade Choice with command \n 8. Type 'Stop' to stop the program.)
    user = input()
    if user == "Stop":
        user_input = 'Stop'
    elif user == 'ALGO':
        choice_for_algo()
    elif user == 'USDC':
        choice_for_usdc()
    elif user == 'YLDY':
        choice_for_YLDY()
    elif user == 'OPUL':
        choice_for_OPUL()
    elif user == 'TACO':
        choice_for_TACO()
    elif user == 'AKITA':
        choice_for_AKITA()
    elif user == 'HDL':
        choice_for_HDL()
    elif user == 'comand':
        choice_for_comand()
          
          
# 5. Improve this wrapper to earn development badges. Improvements include: adding a frontend, adding wallet integration so that users don't have to manually enter their information, etc. 
# Successful submissions will be eligible to earn the Silver and Gold Badges.          
