import discord

from dotenv import dotenv_values

# Les trois lignes suivantes permettent une connexion direct à Discord
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

# Récupération des variables d'environnement pour utilisation
env_variable = dotenv_values(".env")

# On utilise des decorators pour enregister les évenements que l'on souhaite set up
# pour chaque Decorators, le contenu sera executer sous certaines conditions

@client.event
async def on_ready():
    print('Ready!')

@client.event
async def on_message(message):
    # Le contenu de cette fonction sera exécuter desque le bot sera prêt
    if message.content.startswith('hello'):
        await message.channel.send('Hello!')




# Pour terminer cette commande permet d'éxécuter le bot
client.run(env_variable['TOKEN'])
