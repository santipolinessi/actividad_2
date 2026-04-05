def costo_envio():
    
    matriz = [
        [500, 1000, 2000],
        [1000, 2500, 4500],
        [2000, 5000, 8000]
    ]

    peso = float(input('ingrese el peso del paquete (en kg): '))
    zona = input('Ingrese la zona de destino (local/regional/nacional): ')

    zona = zona.lower()

    if zona not in ('local','regional','nacional'):
        print('Zona no válida. Las zonas disponibles son: local, regional, nacional.')
    else:
        if peso < 1:
            fila = 0
        elif 1<= peso <=5:
            fila = 1
        else:
            fila = 2
        
        if zona == 'local':
            col = 0
        elif zona == 'regional':
            col = 1
        else:
            col = 2
            
        print('Costo de envio: $',matriz[fila][col])
            
                