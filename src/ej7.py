import random

def amigo_invisble():

    nombres = input('Ingrese los participantes (separados por coma): ')
    amigos = [nombre.strip().lower() for nombre in nombres.split(',')] ##desde aca ya saco espacios
                                                                    ##y dejo todo en lowercase
    if len(amigos) < 3:
        print('deben ser al menos de 3')
        return

    if len(amigos) != len(set(amigos)):  ##set elimina repetidos
        print('hay nombres repetidos')
        return

    sorteo = amigos.copy()

    while True:
        random.shuffle(sorteo)

        valido = True
        for i in range(len(amigos)):
            if amigos[i]==sorteo[i]:
                valido = False
                break

        if valido:
            break

    print('Sorteo de amigo invisible: ')
    for i in range(len(amigos)):
        print(f'{amigos[i].capitalize()} \u2192 {sorteo[i].capitalize()}')
                

