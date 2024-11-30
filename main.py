import discord
from discord import app_commands
from discord.ext import commands
from datetime import datetime

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="/", intents=intents)


@bot.tree.command(name="cquand", description="Compte à rebours jusqu'au 23 décembre 2024 à 09:55.")
async def cquand(interaction: discord.Interaction):
    # Date et heure cibles
    target_time = datetime.strptime("2024-12-23 09:55", "%Y-%m-%d %H:%M")

    # Vérification du temps actuel
    now = datetime.now()

    if target_time <= now:
        # Si la date est déjà passée
        await interaction.response.send_message(
            "La date est déjà passée ! 🎉", ephemeral=True
        )
        return

    # Calcul du temps restant
    remaining_time = target_time - now
    days, seconds = divmod(remaining_time.total_seconds(), 86400)
    hours, seconds = divmod(seconds, 3600)
    minutes, seconds = divmod(seconds, 60)

    # Création de l'embed avec le temps restant
    embed = discord.Embed(
        title="C'est quand qu'on y va ?",
        description=f"Il reste :",
        color=discord.Color.blue()
    )
    embed.add_field(
        name="Temps restant",
        value=f"{int(days)} jours, {int(hours)} heures, {int(minutes)} minutes.",
        inline=False
    )
    embed.set_image(url="https://i.ibb.co/kmsBmcC/squidgame.gif")

    # Envoi du message une seule fois
    await interaction.response.send_message(embed=embed)


# Synchronisation des commandes slash et confirmation
@bot.event
async def on_ready():
    try:
        synced = await bot.tree.sync()
        print(f"Commandes slash synchronisées : {synced}")
    except Exception as e:
        print(f"Erreur lors de la synchronisation des commandes : {e}")
    print(f"Bot connecté en tant que {bot.user}")


# Démarrage du bot avec le toke
        
bot.run("")
