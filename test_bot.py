import discord
from discord.ext import commands
import requests
import uuid

TOKEN = 'MTE4Njc0MDM2MjU5NzkwNDQ3NA.G00NDW.w6MX6mwAzLu-0WhN9w8SB3HeTqvRVe7Uj9DT9E'
SERVER_URL = 'http://localhost:5000/store_token'
intents = discord.Intents.default()
intents.messages = True
intents.guilds=True
intents.message_content=True

bot = commands.Bot(command_prefix='!',intents=intents)
 
@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')
        

@bot.event
async def on_guild_join(guild):
    print(f"Joined a new guild.. {guild.name}")
    server_auth_token = str(uuid.uuid4())
    requests.post(SERVER_URL, data={'server_id': guild.id, 'token': server_auth_token})
    for channel in guild.text_channels:
        guild_name=guild.name
        await channel.send(f"Hello World! {guild_name}")

   
@bot.command(name='hello')
async def hello_world(ctx):
    guild_name=ctx.guild.name
    await ctx.send(f'Hello World,{guild_name}')

bot.run(TOKEN)