def ej_2():

    ##EJERCICIO 2
    
    playlist = [
        {"title": "Bohemian Rhapsody", "duration": "5:55"},
        {"title": "Hotel California", "duration": "6:30"},
        {"title": "Stairway to Heaven", "duration": "8:02"},
        {"title": "Imagine", "duration": "3:07"},
        {"title": "Smells Like Teen Spirit", "duration": "5:01"},
        {"title": "Billie Jean", "duration": "4:54"},
        {"title": "Hey Jude", "duration": "7:11"},
        {"title": "Like a Rolling Stone", "duration": "6:13"},
    ]
    
    tot_secs = 0
    mas_larga = None
    mas_corta = None
    
    for song in playlist:
        minutos,segundos = map(int,song["duration"].split(":"))
        duration_sec = minutos*60 + segundos
        tot_secs += duration_sec
    
        if mas_larga is None or duration_sec > mas_larga[1]:
            mas_larga=(song["title"],duration_sec)
    
        if mas_corta is None or duration_sec < mas_corta[1]:
            mas_corta = (song["title"], duration_sec)
    
    min_total = tot_secs // 60
    seg_total = tot_secs % 60
    
    # convertir duraciones de canciones
    def formatear(seg):
        return f"{seg//60}:{seg%60:02d}"
    
    print(f"Duración total: {min_total}m {seg_total}s")
    print(f"Cancion mas larga: {mas_larga[0]} ({formatear(mas_larga[1])})")
    print(f"Cancion mas corta: {mas_corta[0]} ({formatear(mas_corta[1])})")