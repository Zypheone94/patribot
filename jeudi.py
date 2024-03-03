import discord
import time
import schedule

from dotenv import dotenv_values

# Les trois lignes suivantes permettent une connexion direct à Discord
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

# Récupération des variables d'environnement pour utilisation
env_variable = dotenv_values(".env")


def call_du_jeudi():
    print('test')
    client.run(env_variable['TOKEN'])


schedule.every(1).minute.do(call_du_jeudi)


@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")
    print('test du call')
    channel = client.get_channel(1048956032237441074)
    await channel.send('@everyone test !')

while True:
    schedule.run_pending()
    time.sleep(1)
