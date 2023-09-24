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

timezones = [
    ('USA', 'America/New_York'),
    ('Nigeria', 'Africa/Lagos'),
    ('India', 'Asia/Kolkata')
]

channel_data = {}  # To store channel information

@tasks.loop(minutes=5)
async def update_timezones():
    guild_id = "YOUR_SERVER_ID"  # Replace with your Server ID
    guild = bot.get_guild(guild_id)
    category_name = 'Current Time'

    # Check if the category already exists, create it if it doesn't
    category = discord.utils.get(guild.categories, name=category_name)
    if category is None:
        category = await guild.create_category(category_name)

    for tz_name, tz_id in timezones:
        timezone = pytz.timezone(tz_id)
        current_time = datetime.now(timezone).strftime('%I:%M %p')  # 12-hour format with AM/PM
        channel_name = f'{tz_name} Time: {current_time}'

        # Check if a channel already exists for this timezone
        if tz_name in channel_data:
            channel = channel_data[tz_name]
            await channel.edit(name=channel_name)
        else:
            # Create a new voice channel if it doesn't exist
            channel = await category.create_voice_channel(channel_name)
            channel_data[tz_name] = channel

@bot.command()
async def timezone(ctx):
    await update_timezones()
    await ctx.send('Time zone channels have been updated.')

bot.run('YOUR_BOT_TOKEN')  # Replace with your Bot Token
