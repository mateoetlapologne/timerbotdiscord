import discord
from discord import app_commands
from discord.ext import commands
from datetime import datetime
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="/", intents=intents)
@bot.tree.command(name="when", description="Discord command for know how many day/hours last before the day...")
async def cquand(interaction: discord.Interaction):
    # Date/Hour
    target_time = datetime.strptime("2024-12-23 09:55", "%Y-%m-%d %H:%M")
    now = datetime.now()
    if target_time <= now:
        await interaction.response.send_message(
            "Day is already outpassed", ephemeral=True
        )
        return
    remaining_time = target_time - now
    days, seconds = divmod(remaining_time.total_seconds(), 86400)
    hours, seconds = divmod(seconds, 3600)
    minutes, seconds = divmod(seconds, 60)
    embed = discord.Embed(
        title="Change the title",
        description=f"Time last",
        color=discord.Color.blue()
    )
    embed.add_field(
        name="Time Last",
        value=f"{int(days)} day, {int(hours)} hours, {int(minutes)} minutes.",
        inline=False
    )
    embed.set_image(url="https://i.ibb.co/kmsBmcC/squidgame.gif")
    await interaction.response.send_message(embed=embed)
@bot.event
async def on_ready():
    try:
        synced = await bot.tree.sync()
    except Exception as e:
    print(f"Bot ready{bot.user}")
        
bot.run("") #Put the discord token here
