import discord
import os
from discord.ext import commands
from Dado import lanzar_dado
from imagenesApi import get_duck_image_url

# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
bot = commands.Bot(command_prefix='?', intents=intents)
@bot.event
async def on_ready():
    print(f'Hemos iniciado sesión como {bot.user}')

@bot.command()
async def dado(ctx):
    resultado = lanzar_dado()  # Llamamos la función para lanzar el dado
    await ctx.send(f"🎲 El resultado del dado fue: {resultado}")    

@bot.command()
async def mem(ctx):
    with open('image/mm1.jpeg', 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
        print(os.listdir('image'))
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)
@bot.command('duck')
async def duck(ctx):
    '''Una vez que llamamos al comando duck, 
    el programa llama a la función get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)
bot.run(".")

