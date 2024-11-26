import discord
from discord import app_commands
from discord.ext import commands
from datetime import datetime, timedelta
import asyncio

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="/", intents=intents)
@bot.tree.command(name="cquand", description="Pour savoir quand on")
async def countdown(interaction: discord.Interaction):
    date = "2024-12-23"
    time = "09:55"
    try:
        target_time = datetime.strptime(f"{date} {time}", "%Y-%m-%d %H:%M")
        now = datetime.now()
        embed = discord.Embed(
            title="C'est quand qu'on y va",
            description="Calcul du temps restant...",
            color=discord.Color.blue()
        )
        embed.add_field(name="Temps restant", value="Calcul en cours...")
        embed.set_image(url="https://i.ibb.co/kmsBmcC/squidgame.gif")
        await interaction.response.send_message(embed=embed)
        message = await interaction.original_response()
        while True:
            now = datetime.now()
            remaining_time = target_time - now
            days, seconds = divmod(remaining_time.total_seconds(), 86400)
            hours, seconds = divmod(seconds, 3600)
            minutes, seconds = divmod(seconds, 60)
            if len(embed.fields) > 0:
                embed.set_field_at(
                    0,
                    name="Temps restant",
                    value=f"{int(days)}j {int(hours)}h",
                    inline=False
                )
    except ValueError:
        await interaction.response.send_message(
            "Format invalide. Utilisez : `/countdown date:YYYY-MM-DD time:HH:MM`", ephemeral=True
        )

bot.run("")
