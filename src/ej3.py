## ACTIVIDAD 3
def ej_3():
    review = """La película sigue a un grupo de astronautas que 
    viajan a Marte en una misión de rescate. El capitán Torres lidera al equipo 
    a través de tormentas solares y fallos en el sistema de navegación. Al 
    llegar a Marte descubren que la base está abandonada y los 
    suministros destruidos. Torres decide sacrificar la nave nodriza para 
    salvar al equipo y logran volver a la Tierra en una cápsula de emergencia.
    El final revela que Torres sobrevivió gracias a un pasaje secreto."""
    
    palabras = review.split()
    resultado = []
    
    spoilers = input('ingrese las palabras consideradas spoilers separadas por comas: ')
    lista_spoilers = spoilers.split(',')
    lista_spoilers = [palabra.strip() for palabra in lista_spoilers]
    
    print(lista_spoilers)
    
    for palabra in palabras:
        limpia = palabra.lower().strip('.,;:')
    
        if limpia in lista_spoilers:
            resultado.append('*'*len(limpia))
        else:
            resultado.append(palabra)
    
    texto_final = ' '.join(resultado)
    
    print('\nTexto censurado\n')
    print(texto_final)