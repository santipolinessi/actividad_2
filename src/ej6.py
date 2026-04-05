def hashtags():

    posts = [
        "Arrancando el lunes con energía #Motivación #NuevaSemana",
        "Terminé mi primer proyecto en Python #Python #Programación #OrgullosoDeMi",
        "No puedo creer el final de la serie #SinSpoilers #SerieAdicta",
        "Nuevo video en el canal sobre #InteligenciaArtificial y #Python",
        "Entrenamiento de hoy completado #Fitness #Motivación #NoPainNoGain",
        "Leyendo sobre #InteligenciaArtificial y el futuro del trabajo #Tecnología",
        "Arranqué a estudiar #Programación por mi cuenta #Python #Autodidacta",
        "Finde de lluvia, maratón de series #SerieAdicta #Relax",
        "Workshop de #InteligenciaArtificial en la universidad #Tecnología #Programación"
        ]

    sin_hashtag = []

    for post in posts:
        words = post.split()

        for word in words:
            if word.startswith('#'):
                sin_hashtag.append(word)

    conteo = {}
    for palabra in sin_hashtag:
        if palabra in conteo:
            conteo[palabra] += 1
        else:
            conteo[palabra] = 1

    print("Hashtags trending (más de una aparición):")
    for palabra,cantidad in sorted(conteo.items(), key=lambda x: x[1], reverse = True):
        if cantidad > 1:
            print(f' {palabra}: {cantidad}')

    print('Total hashtags unicos: ',len(conteo))


    
    