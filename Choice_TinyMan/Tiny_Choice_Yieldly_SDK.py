# Copyright Fortior Blockchain, LLLP 2021

#VOID TEST ADRESSS
receiver_address = ""
receiver_passphrase = ""

# Pooling
###############
from tinyman.v1.client import TinymanTestnetClient

account = {
    'address': '',
    'private_key': '', 
    # Use algosdk.mnemonic.to_private_key(mnemonic) if necessary
}

client = TinymanTestnetClient(user_address=account['address'])
Choice = client.fetch_asset(17263578)
YLDY = client.fetch_asset(22847688)
pool = client.fetch_pool(Choice, YLDY)
info = pool.fetch_pool_position()
share = info['share'] * 100

print(f'Pool Tokens: {info[pool.liquidity_asset]}')
print(f'Assets: {info[Choice]}, {info[YLDY]}')
print(f'Share of pool: {share:.3f}%')

# Add Liquidity
###############
from tinyman.v1.client import TinymanTestnetClient

account = {
    'address': '',
    'private_key': '', 
    # Use algosdk.mnemonic.to_private_key(mnemonic) if necessary
}

client = TinymanTestnetClient(user_address=account['address'])
Choice = client.fetch_asset(17263578)
YLDY = client.fetch_asset(22847688)
pool = client.fetch_pool(Choice, YLDY)
# Get a quote for supplying 1000.0 Choice
quote = pool.fetch_mint_quote(Choice(1000_000_000), slippage=0.01)
print(quote)

# Check if we are happy with the quote..
if quote.amounts_in[YLDY] < 5_000_000:
    # Prepare the mint transactions from the quote and sign them
    transaction_group = pool.prepare_mint_transactions_from_quote(quote)
    transaction_group.sign_with_private_key(account['address'], account['private_key'])
    result = client.submit(transaction_group, wait=True)
    # Check if any excess liquidity asset remaining after the mint
    excess = pool.fetch_excess_amounts()
    if pool.liquidity_asset in excess:
        amount = excess[pool.liquidity_asset]
        print(f'Excess: {amount}')
        if amount > 1_000_000:
            transaction_group = pool.prepare_redeem_transactions(amount)
            transaction_group.sign_with_private_key(account['address'], account['private_key'])
            result = client.submit(transaction_group, wait=True)

info = pool.fetch_pool_position()
share = info['share'] * 100
print(f'Pool Tokens: {info[pool.liquidity_asset]}')
print(f'Assets: {info[Choice]}, {info[YLDY]}')
print(f'Share of pool: {share:.3f}%')
