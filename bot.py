import discord
from discord.ext import commands, tasks
import pytz
from datetime import datetime


intents = discord.Intents.default()
intents.typing = False
intents.presences = False

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')
    update_timezones.start()

@tasks.loop(minutes=5)
async def update_timezones():
    guild_id = 1234567890
    guild = bot.get_guild(YOUR_SERVER_ID) # Replace with your Server ID
    category_name = 'Current Time'

    # Check if the category already exists, create it if it doesn't
    category = discord.utils.get(guild.categories, name=category_name)
    if category is None:
        category = await guild.create_category(category_name)

    # Delete old voice channels within the category
    for channel in category.voice_channels:
        await channel.delete()

    # Create voice channels for each time zone and edit the Timezones according to you, You can even add more to it
    timezones = [
        ('USA', 'America/New_York'),
        ('Nigeria', 'Africa/Lagos'),
        ('India', 'Asia/Kolkata')
    ]
    for tz_name, tz_id in timezones:
        timezone = pytz.timezone(tz_id)
        current_time = datetime.now(timezone).strftime('%I:%M %p')  # 12-hour format with AM/PM
        channel_name = f'{tz_name} Time: {current_time}'
        await category.create_voice_channel(channel_name)

@bot.command()
async def timezone(ctx):
    await update_timezones()
    await ctx.send('Time zone channels have been updated.')

bot.run('YOUR_BOT_TOKEN') # Replace with your Bot Token
