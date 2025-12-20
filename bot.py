import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
load_dotenv()

print("Loading bot...")

class Teams:
    def __init__(self, nom, points):
        self.nom = nom
        self.points = points

    def add_points(self, nombre):
        self.points += nombre




intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!" ,intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f"Bot connecté en tant que {bot.user}")
    try:
        synced = await bot.tree.sync()
        print (f"Commandes slash sunchronisées : {len(synced)}")
    except Exception as e:
        print(e)

@bot.event 
async def on_message(message: discord.message):
    if message.content.lower() == '$help':
        channel = message.channel
        await channel.send("Ta besoin d'aide ?")

@bot.tree.command(name="test", description ="C'est juste pour le test")
async def test(interaction: discord.Interaction):
    await interaction.response.send_message("Voici et ça  montre que le test fonction")


@bot.tree.command(name="classement", description ="classement des meilleurs équipes")
async def test(interaction: discord.Interaction):
    embed_classement = discord.Embed(
        title="Classement des equipes",
        description="Voici le classement des équipes par rapport au point obtenue !",
        color=discord.Color.blue()
    )
    embed_classement.add_field(name="Blue Team", value=f"Nombre de Point = {point} / Position {position} ")
    await interaction.response.send_message(embed=embed_classement)



bot.run(os.getenv('DISCORD_TOKEN'))
