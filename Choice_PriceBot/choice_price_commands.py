# Imports
import json, time
from datetime import datetime
from algosdk.v2client import algod
from tinyman.v1.client import TinymanClient
import discord
from discord.ext import commands

# Get bot tokens
f = open('./keys.json',)
keys = json.load(f)
f.close()

# Create a discord client
discord_commander = commands.Bot(command_prefix="!")

# Get Algo Client / Using purestake; supplement your own API key for the algod_token
algod_address = 'https://mainnet-algorand.api.purestake.io/ps2'
algod_token = keys['algod_token']
headers = {'X-API-Key': algod_token}
algod_client = algod.AlgodClient(algod_token, algod_address, headers)

# Get TMan Client / 350338509 is the app ID for all TinymanClient implementations
# Get Assets and Pools - ALGO, CHOICE, USDC
tinyman = TinymanClient(algod_client, 350338509)
ALGO = tinyman.fetch_asset(0)
CHOICE = tinyman.fetch_asset(297995609)
LION = tinyman.fetch_asset(372666897)
USDC = tinyman.fetch_asset(31566704)
ALGO_USDC = tinyman.fetch_pool(ALGO, USDC)
CHOICE_ALGO = tinyman.fetch_pool(CHOICE, ALGO)
LION_USDC = tinyman.fetch_pool(LION, USDC)

# Retrieve price of choice
def get_prices():
    quote_ALGO_USDC = ALGO_USDC.fetch_fixed_input_swap_quote(ALGO(1_000_000), slippage=0)
    algo_price = float(quote_ALGO_USDC.amount_out_with_slippage.amount) / float(10**quote_ALGO_USDC.amount_out_with_slippage.asset.decimals)
    algo_price = round(algo_price, 4)
    quote_CHOICE_ALGO = CHOICE_ALGO.fetch_fixed_input_swap_quote(CHOICE(100), slippage=0)
    choice_out = float(quote_CHOICE_ALGO.amount_out_with_slippage.amount) / float(10**quote_CHOICE_ALGO.amount_out_with_slippage.asset.decimals)
    choice_price = round(algo_price * choice_out, 4)
    quote_LION_USDC = LION_USDC.fetch_fixed_input_swap_quote(LION(10_000), slippage=0)
    lion_price = float(quote_LION_USDC.amount_out_with_slippage.amount) / float(10**quote_LION_USDC.amount_out_with_slippage.asset.decimals)
    lion_price = round(lion_price, 4)
    return algo_price, choice_price, lion_price

# Command to show the price immediately
@discord_commander.command()
async def algo_price(ctx):
    sender = str(ctx.author).split("#")[0]
    algo_price, choice_price, lion_price = get_prices()
    await ctx.send(
        f'Hello There, {sender}\n' +
        f'The current price of Algo is **${algo_price}** :rocket:'
    )

@discord_commander.command()
async def choice_price(ctx):
    sender = str(ctx.author).split("#")[0]
    algo_price, choice_price, lion_price = get_prices()
    await ctx.send(
        f'Hello There, {sender}\n' +
        f'The current price of Choice Coin is **${choice_price}** :rocket:'
    )

@discord_commander.command()
async def lion_price(ctx):
    sender = str(ctx.author).split("#")[0]
    algo_price, choice_price, lion_price = get_prices()
    await ctx.send(
        f'Hello There, {sender}\n' +
        f'The current price of Lion Coin is **${lion_price}** :rocket:'
    )

@discord_commander.command()
async def tell_sawamy_he_sucks(ctx):
    await ctx.send(
        f'SAWAMY, you suck! :rocket:'
    )

# Run the client and commander
discord_commander.run(keys['bot_token'])
