# Imports
import discord
import discord.ext
import asyncio
import requests

# VLONE
client = discord.Client()

# Requests
b = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
bprice = b.json()['bpi']['USD']['rate_float']
bprice = round(int(bprice))

# ESKEETIT

@client.event
async def on_message(message):
	if message.content.startswith('$DESC'):
		await client.send_message(message.channel, "VLONE Bot created by Aqtive")

@client.event
async def on_message(message):
	if message.content.startswith('$BPRICE'):
		await client.send_message(message.channel, "Current Bitcoin Price: %s" % (bprice))

# Run

client.run("NDU0ODE5NDgxMjczNzYxODAy.Df1SFw.3WlZoAs18W65CnFA1IRvGOWsy-U")
