import discord
from discord.ext import tasks

from dotenv import dotenv_values

# Les trois lignes suivantes permettent une connexion direct à Discord
intents = discord.Intents.default()
intents.message_content = True

bot = discord.Client(intents=intents)

# Récupération des variables d'environnement pour utilisation
env_variable = dotenv_values(".env")

@bot.event
async def on_ready():
    print("Logged in as")
    print(bot.user.name)
    print("------")
    msg1.start()


@tasks.loop(minutes=1)
async def msg1():
    message_channel = bot.get_channel(1048956032237441074)
    await message_channel.send("@everyone -> call du jeudi !")

bot.run(env_variable['TOKEN'])
