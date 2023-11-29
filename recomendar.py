# Función para recomendar una canción (puedes personalizar según tus necesidades)
def recomendar_cancion(preferencias_usuario):
    # Lógica de recomendación simple (puedes personalizar esta lógica según tus necesidades)
    if "rock" in [token.text.lower() for token in preferencias_usuario]:
        return "Stairway to Heaven - Led Zeppelin"
    elif "pop" in [token.text.lower() for token in preferencias_usuario]:
        return "Shape of You - Ed Sheeran"
    elif "hip hop" in [token.text.lower() for token in preferencias_usuario]:
        return "Sicko Mode - Travis Scott"
    elif "electrónica" in [token.text.lower() for token in preferencias_usuario]:
        return "Clarity - Zedd"
    elif "banda" in [token.text.lower() for token in preferencias_usuario]:
        return "Bésame Mucho - Consuelo Velázquez"
    elif "reggae" in [token.text.lower() for token in preferencias_usuario]:
        return "Three Little Birds - Bob Marley"
    else:
        return "No tengo una recomendación específica para tus preferencias, ¡pero disfruta de la música que te gusta!"

# Resto del código...