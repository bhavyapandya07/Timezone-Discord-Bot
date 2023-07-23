import discord
from discord.ext import commands, tasks
import pytz
from datetime import datetime

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

bot = commands.Bot(command_prefix='!', intents=intents)

Unicode flag emojis
FLAG_EMOJIS = {
    'USA': '\U0001F1FA\U0001F1F8',
    'Nigeria': '\U0001F1F3\U0001F1EC',
    'India': '\U0001F1EE\U0001F1F3'
}

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')
    update_timezones.start()


@tasks.loop(minutes=5)
async def update_timezones():
    guild_id = 1234567890  # Replace with your guild ID
    guild = bot.get_guild(YOUR_SERVER_ID)
    category_name = 'Current Time'

    # Check if the category already exists, create it if it doesn't
    category = discord.utils.get(guild.categories, name=category_name)
    if category is None:
        category = await guild.create_category(category_name)

    # Get the existing voice channels within the category
    voice_channels = [channel for channel in category.voice_channels]

    # Update the names of existing voice channels for each time zone
    timezones = [
        ('USA', 'America/Los_Angeles'),
        ('Nigeria', 'Africa/Lagos'),
        ('India', 'Asia/Kolkata')
    ]

    for channel, (tz_name, tz_id) in zip(voice_channels, timezones):
        timezone = pytz.timezone(tz_id)
        current_time = datetime.now(timezone).strftime('%d %b %Y %I:%M %p')  # Include day and year
        flag_emoji = FLAG_EMOJIS.get(tz_name, '')
        channel_name = f'{flag_emoji} {current_time}'
        await channel.edit(name=channel_name)


@bot.command()
async def timezone(ctx):
    await update_timezones()
    await ctx.send('Time zone channels have been updated.')


bot.run('YOUR_BOT_TOKEN')