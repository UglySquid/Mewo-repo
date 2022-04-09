import discord
import praw
from discord.ext import commands
import oauth2

client = discord.Client(command_prefix="mewo.", case_insensitive=True)
Token = "OTYyNDA4ODg4MTMxNTI2NzA3.YlHHHw.S75PU7QCNDYtaV-IzmaHAcCT-Go"
auth = oauth2.Oauth.discord_login_url

# Functionality


@client.event
async def on_ready():
    channel = client.get_channel(851169143767302154)
    await channel.send("Meow has landed!")


@client.event
async def on_disconnect():
    channel = client.get_channel(851169143767302154)
    await channel.send("Au revoir!")


@client.command(name="hi" or "hello")
async def hi(ctx):
    await ctx.message.channel.send("Hello, Assolotls!")

help_embed = discord.Embed(title="Mewo?", description="At your service!", color=0x3c6e71)
help_embed.add_field(name="Name: ", value="Mewo")
help_embed.add_field(name="Age: ", value="Cat")
help_embed.add_field(name="Occupation: ", value="Unemployed but still richer than you", inline=False)
help_embed.add_field(name="Hobbies: ", value="Sending cat pictures", inline=False)
help_embed.set_footer(text="℗ Copyright Mewo Corp 2022")


@client.command(name="helpme")
async def helpme_func(ctx):
    await ctx.message.channel.send(embed=help_embed)

# Run the bot
client.run(Token)
