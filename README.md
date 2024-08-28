# Discord Timezone Bot ⌚

## Description

The Discord Timezone Bot is a Python-based bot that allows users to view the current time in three different time zones: USA 🇺🇸, Nigeria 🇳🇬, and India 🇮🇳. The bot creates a category called "Current Time ⌚" and three voice channels within it, each displaying the time for a specific time zone. The displayed time updates automatically every 5 minutes ⏲️.

## Features

- Command to run the Bot: `!timezone` ⏰
- Creates a category: "Current Time ⌚"
- Creates 3 voice channels: "USA Time 🇺🇸", "Nigeria Time 🇳🇬", "India Time 🇮🇳" `You can edit it according to any timezone`
- Displays the current time for each time zone
- Updates the displayed time every 5 minutes ⏲️

## Prerequisites

Before running the bot, make sure you have the following installed:

- Python 3.x
- discord.py library

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/CyberWarrior743/Discord-Time-Bot.git
   ```

2. Navigate to the project directory:

   ```bash
   cd Discord-Time-Bot
   ```

3. Update the `bot.py` file with your Server ID & Discord bot token:

   ```python
   guild = bot.get_guild(YOUR_SERVER_ID) # Replace with your Server ID
   bot.run('YOUR_BOT_TOKEN') # Replace with your Bot Token
   ```

## Usage

1. Run the bot:

   ```bash
   python bot.py
   ```

2. Invite the bot to your Discord server using the discord developer portal link:

3. Once the bot is in your server, you can use the `!timezone` command to create the "Current Time ⌚" category and the three voice channels with the displayed time for each time zone.

## Acknowledgements

- [discord.py](https://discordpy.readthedocs.io/) - Python library for creating Discord bots.
- [python-dateutil](https://dateutil.readthedocs.io/) - Python library for parsing and manipulating dates and times.
- [pytz](https://pypi.org/project/pytz/) - World timezone definitions for Python.

## Contact

For any inquiries or support, please contact [Bhavya Pandya](mailto:bhavya@crito.design).
