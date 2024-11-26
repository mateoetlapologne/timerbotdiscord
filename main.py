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
        # Parse la date et l'heure cible
        target_time = datetime.strptime(f"{date} {time}", "%Y-%m-%d %H:%M")
        now = datetime.now()
        if target_time <= now:
            await interaction.response.send_message("La date et l'heure doivent être dans le futur.", ephemeral=True)
            return

        # Création de l'embed
        embed = discord.Embed(
            title="C'est quand qu'on y va",
            description="Calcul du temps restant...",
            color=discord.Color.blue()
        )
        embed.add_field(name="Temps restant", value="Calcul en cours...")
        embed.set_image(url="https://i.ibb.co/kmsBmcC/squidgame.gif")
        await interaction.response.send_message(embed=embed)
        message = await interaction.original_response()

        # Boucle de mise à jour
        while True:
            now = datetime.now()
            if now >= target_time:
                embed.description = "On y est ! 🎉"
                embed.clear_fields()
                await message.edit(embed=embed)
                break

            # Calcul du temps restant
            remaining_time = target_time - now
            days, seconds = divmod(remaining_time.total_seconds(), 86400)
            hours, seconds = divmod(seconds, 3600)
            minutes, seconds = divmod(seconds, 60)
            if minutes > 30:
                hours += 1
            if minutes < 30:
                hours -= 1
            if len(embed.fields) > 0:
                embed.set_field_at(
                    0,
                    name="Temps restant",
                    value=f"{int(days)}j {int(hours)}h",
                    inline=False
                )
            else:
                embed.add_field(
                    name="Temps restant",
                    value=f"{int(days)}j {int(hours)}h",
                    inline=False
                )

            await message.edit(embed=embed)
            await asyncio.sleep(3600)  # wait for 1 hour

    except ValueError:
        await interaction.response.send_message(
            "Format invalide. Utilisez : `/countdown date:YYYY-MM-DD time:HH:MM`", ephemeral=True
        )

bot.run("bot token")
