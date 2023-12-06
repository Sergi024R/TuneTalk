import asyncio
from distutils import config
import discord
from discord.ext import commands
import requests
from database import check_database_connection, create_generos_table, insert_user_into_database, obtener_opciones_generos, obtener_playlist_genero, update_user_in_database
import spacy
import credentials  # Importa tus credenciales


from recomendar import recomendar_cancion

nlp = spacy.load("es_core_news_sm")

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

# Llama al la funcion Actualizar usuario

@bot.command(name='actualizar')
async def actualizar_usuario(ctx, nombre, edad):
    # Obtener el ID del usuario que ejecutó el comando
    id_usuario = ctx.author.id
    
    # Llamar a la función para actualizar el usuario en la base de datos
    if update_user_in_database(id_usuario, nombre, edad):
        await ctx.send(f'Información de usuario actualizada correctamente: {nombre}, {edad} años.')
    else:
        await ctx.send('Error al actualizar la información del usuario. Por favor, inténtalo de nuevo.')

# Resto del código...
# create_generos_table()

# Resto del código...

@bot.command(name='play')
async def reproducir_playlist(ctx):
    # Obtener opciones de géneros desde la base de datos
    generos_options = obtener_opciones_generos()

    # Mostrar opciones al usuario
    mensaje_opciones = "Selecciona un género para reproducir la playlist:\n"
    for i, genero in enumerate(generos_options, start=1):
        mensaje_opciones += f"{i}. {genero}\n"

    await ctx.send(mensaje_opciones)

    # Esperar la respuesta del usuario
    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

    try:
        respuesta = await bot.wait_for('message', check=check, timeout=30)
        opcion_elegida = int(respuesta.content)

        # Obtener el nombre del género seleccionado
        nombre_genero_seleccionado = generos_options[opcion_elegida - 1]

        # Obtener la playlist del género desde la base de datos
        playlist = obtener_playlist_genero(nombre_genero_seleccionado)

        await ctx.send(f"Reproduciendo la playlist de {nombre_genero_seleccionado}: {playlist}")

    except asyncio.TimeoutError:
        await ctx.send("Se agotó el tiempo para seleccionar un género. Vuelve a intentarlo.")



# Cargar el modelo de spaCy para el idioma español
# nlp = spacy.load("es_core_news_sm")

@bot.command(name='preferencias')
async def obtener_preferencias(ctx):
    await ctx.send("Hola, ¿cuáles son tus preferencias musicales? Puedes mencionar géneros, artistas o cualquier detalle que te gustaría tener en cuenta.")

    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

    try:
        respuesta = await bot.wait_for('message', check=check, timeout=30)
        preferencias_usuario = respuesta.content

        # Procesar preferencias del usuario con spaCy
        doc = nlp(preferencias_usuario)

        # Realizar recomendación basada en preferencias
        recomendacion = recomendar_cancion(doc)


        await ctx.send(f"¡Gracias por compartir tus preferencias! Te recomiendo escuchar: {recomendacion}")

    except asyncio.TimeoutError:
        await ctx.send("Se agotó el tiempo para ingresar tus preferencias. Vuelve a intentarlo.")

@bot.command(name='recomendar_cancion_lastfm') 
async def recomendar_cancion_lastfm(ctx, genero):
    try:
        # Realizar una llamada a la API de Last.fm para obtener una recomendación de canción por género
        url = f'http://ws.audioscrobbler.com/2.0/?method=tag.gettoptracks&tag={genero}&api_key={credentials.LASTFM_API_KEY}&format=json'
        response = requests.get(url)
        data = response.json()

        # Extraer información de la primera canción
        cancion = data['tracks']['track'][0]['name']
        artista = data['tracks']['track'][0]['artist']['name']

        await ctx.send(f"¡Aquí tienes una recomendación de {genero}!: {cancion} - {artista}")

    except Exception as e:
        print(f"Error al recomendar canción desde Last.fm: {e}")
        await ctx.send("Ocurrió un error al intentar recomendar una canción.")

# Resto del código...



bot.run('MTE3MzgyNzc5NTc0NzYxMDY0NA.GOIvNA.eWFhk6oHHxzCnHDzh-g7rafrELJMHfLJc3G2_c')