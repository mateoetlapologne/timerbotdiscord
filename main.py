import discord
from discord import app_commands
from discord.ext import commands
from datetime import datetime, timedelta
import asyncio
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="/", intents=intents)
@bot.tree.command(name="countdown", description="Lance un compte à rebours jusqu'à une date et heure.")
async def countdown(interaction: discord.Interaction, date: str, time: str):
    try:
        target_time = datetime.strptime(f"{date} {time}", "%Y-%m-%d %H:%M")
        now = datetime.now()
        if target_time <= now:
            await interaction.response.send_message("La date et l'heure doivent être dans le futur.", ephemeral=True)
            return
        embed = discord.Embed(
            title="C'est quand qu'on y va",
            description="Calcul du temps restant...",
            color=discord.Color.blue()
        )
        embed.add_field(name="Temps restant", value="Calcul en cours...")
        embed.set_image(url="https://i.ibb.co/kmsBmcC/squidgame.gif")  # Set image url if u want, if u dont want just put an # behind this line
        await interaction.response.send_message(embed=embed)
        message = await interaction.original_response()
        while True:
            now = datetime.now()
            if now >= target_time:
                embed.description = "On "
                embed.clear_fields()
                await message.edit(embed=embed)
                break
            remaining_time = target_time - now
            days, seconds = divmod(remaining_time.total_seconds(), 86400)
            hours, seconds = divmod(seconds, 3600)
            minutes, seconds = divmod(seconds, 60)
            if len(embed.fields) > 0:
                embed.set_field_at(
                    0,
                    name="Temps restant",
                    value=f"{int(days)}j {int(hours)}h {int(minutes)}m {int(seconds)}s",
                    inline=False
                )
            else:
                embed.add_field(
                    name="Temps restant",
                    value=f"{int(days)}j {int(hours)}h {int(minutes)}m {int(seconds)}s",
                    inline=False
                )

            await message.edit(embed=embed)
            await asyncio.sleep(1)

    except ValueError:
        await interaction.response.send_message(
            "Format invalide. Utilisez : `/countdown date:YYYY-MM-DD time:HH:MM`", ephemeral=True
        )

bot.run("bot token")
