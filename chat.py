import discord
from discord.ext import commands

from database import check_database_connection, insert_user_into_database

# Crear una instancia de intenciones
intents = discord.Intents.default()
intents.message_content = True  # Habilitar intención de contenido de mensajes

# Crear una instancia del bot con intenciones
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Conectado como {bot.user.name}')

@bot.command(name='saludo')
async def saludar(ctx):
    await ctx.send(f'Hola, {ctx.author.mention}!')


@bot.command(name='registro')
async def registrar_usuario(ctx, nombre, edad):
    # Obtener el ID del usuario que ejecutó el comando
    id_usuario = ctx.author.id
    
    # Llamar a la función para insertar el usuario en la base de datos
    if insert_user_into_database(id_usuario, nombre, edad):
        await ctx.send(f'Usuario registrado correctamente: {nombre}, {edad} años.')
    else:
        await ctx.send('Error al registrar el usuario. Por favor, inténtalo de nuevo.')


bot.run('MTE3MzgyNzc5NTc0NzYxMDY0NA.Gbom9B.xlb0m4XxYfShpw6dRhAeT95nC4nqUYkQZWoV5A')

