# Función para recomendar una canción (puedes personalizar según tus necesidades)
def recomendar_cancion(preferencias_usuario):
    # Lógica de recomendación simple (puedes personalizar esta lógica según tus necesidades)
    if "rock" in [token.text.lower() for token in preferencias_usuario]:
        return "Playlist: https://open.spotify.com/playlist/5eYZGmjBvg3kpIUVpRCUhE?si=33cfd11e53544b0e"
    elif "pop" in [token.text.lower() for token in preferencias_usuario]:
        return "https://open.spotify.com/playlist/72FdsweCiOlp4BXdRrUq58?si=424c4bf6195f4a69"
    elif "hip hop" in [token.text.lower() for token in preferencias_usuario]:
        return "https://open.spotify.com/playlist/1WX7qmOf6iczCVogeUC5Sj?si=18edce5576254e8b"
    elif "electrónica" in [token.text.lower() for token in preferencias_usuario]:
        return "https://open.spotify.com/playlist/574gu0rKWEABHngdcdYSbJ?si=b14649ff17be47e5"
    elif "banda" in [token.text.lower() for token in preferencias_usuario]:
        return "https://open.spotify.com/playlist/3IyNJEsknaSFoUIn8qf1Lr?si=fc0d2c0e8cc94b30"
    elif "reggeton" in [token.text.lower() for token in preferencias_usuario]:
        return "https://open.spotify.com/playlist/04SW1JbUtS1VIIv1a9YBrW?si=e872cdb8c7374b8e"
    else:
        return "No tengo una recomendación específica para tus preferencias, ¡pero disfruta de la música que te gusta!"

# Resto del código...