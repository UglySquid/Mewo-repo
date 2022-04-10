import discord
import random
import praw
from discord.ext import commands
import Information

client = commands.Bot(command_prefix="mewo.", case_insensitive=True)
Token = Information.TOKEN
reddit = praw.Reddit(client_id=Information.REDDIT_APP_ID,
                     client_secret=Information.REDDIT_APP_SECRET,
                     user_agent='<console:Mewo:0.0.1 (by /u/Ruo_Childe)>',
                     username='Ruo_Childe',
                     password=Information.Reddit_pass,
                     check_for_async=False)

# subreddits = ['Cats', 'IllegallySmolCats', 'Kitty', 'GrumpyCats','fatcats','AdorableCats','CatLoaf','Purrito',
# 'Catbaguette','noodlebones','CatMemes']

subreddits = ['catpictures']


@client.event
async def on_ready():
    channel = client.get_channel(962409619353895016)
    await channel.send("Meow has landed!")


@client.event
async def on_disconnect():
    channel = client.get_channel(851169143767302154)
    await channel.send("Au revoir!")


@client.command(name="hi" or "hello")
async def hi(ctx):
    await ctx.message.channel.send("AYO!")

help_embed = discord.Embed(title="Mewo?", description="At your service!", color=0xECD7D5)
help_embed.add_field(name="Name: ", value="Mewo")
help_embed.add_field(name="Age: ", value="Cat")
help_embed.add_field(name="Occupation: ", value="Unemployed but still richer than you", inline=False)
help_embed.add_field(name="Hobbies: ", value="Sending cat pictures", inline=False)
help_embed.set_footer(text="℗ Copyright Mewo Corp 2022")


@client.command(name="helpme")
async def helpme_func(ctx):
    await ctx.message.channel.send(embed=help_embed)


@client.command(name="meow")
async def meow_func(ctx):
    global subreddits

    for submission in reddit.subreddit('catpictures').top(limit=None):
        url = submission.url
        if url.endswith(('.jpg', '.png', '.gif', '.jpeg')):
            meow_pic = url
        redditor = submission.author
        post_title = submission.title
        post_url = str(submission.permalink)

    # create embed with cat picture
    meow_embed = discord.Embed(title=f"Meow:", description=f"[{post_title}](https://reddit.com{post_url})", color=0xECD7D5)
    meow_embed.add_field(name="Redditor:", value=str(redditor), inline=False)
    meow_embed.set_image(url=meow_pic)
    await ctx.message.channel.send(embed=meow_embed)


# Run the bot
client.run(Token)
