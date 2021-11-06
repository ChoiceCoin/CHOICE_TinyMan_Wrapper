# Copyright Fortior Blockchain, LLLP 2021

#VOID TEST ADRESSS
receiver_address = "66PWZ4YF7MT6SRAFESWZ44KA262BLNSH6PTE7CUULPIHMNWYX4ZGPMZJMQ"
receiver_passphrase = "excite profit arch either banner movie open tool model must step zone wisdom deal innocent truck test rocket angle glare between dismiss spell able local"

# Pooling
###############
from tinyman.v1.client import TinymanTestnetClient

account = {
    'address': '66PWZ4YF7MT6SRAFESWZ44KA262BLNSH6PTE7CUULPIHMNWYX4ZGPMZJMQ',
    'private_key': 'excite profit arch either banner movie open tool model must step zone wisdom deal innocent truck test rocket angle glare between dismiss spell able local', 
    # Use algosdk.mnemonic.to_private_key(mnemonic) if necessary
}

client = TinymanTestnetClient(user_address=account['address'])
Choice = client.fetch_asset(17263578)
ALGO = client.fetch_asset(0)
pool = client.fetch_pool(Choice, ALGO)
info = pool.fetch_pool_position()
share = info['share'] * 100

print(f'Pool Tokens: {info[pool.liquidity_asset]}')
print(f'Assets: {info[Choice]}, {info[ALGO]}')
print(f'Share of pool: {share:.3f}%')

# Add Liquidity
###############
from tinyman.v1.client import TinymanTestnetClient

account = {
    'address': '66PWZ4YF7MT6SRAFESWZ44KA262BLNSH6PTE7CUULPIHMNWYX4ZGPMZJMQ',
    'private_key': 'excite profit arch either banner movie open tool model must step zone wisdom deal innocent truck test rocket angle glare between dismiss spell able local', 
    # Use algosdk.mnemonic.to_private_key(mnemonic) if necessary
}

client = TinymanTestnetClient(user_address=account['address'])
Choice = client.fetch_asset(17263578)
ALGO = client.fetch_asset(0)
pool = client.fetch_pool(Choice, ALGO)
# Get a quote for supplying 1000.0 Choice
quote = pool.fetch_mint_quote(Choice(1000_000_000), slippage=0.01)
print(quote)

# Check if we are happy with the quote..
if quote.amounts_in[ALGO] < 5_000_000:
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
print(f'Assets: {info[Choice]}, {info[ALGO]}')
print(f'Share of pool: {share:.3f}%')
