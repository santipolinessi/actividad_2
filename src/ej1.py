def ej_1():

##EJERCICIO 1

    text = """Beautiful is better than ugly.
    Explicit is better than implicit.
    Simple is better than complex.
    Complex is better than complicated.
    Flat is better than nested.
    Sparse is better than dense.
    Readability counts.
    Special cases aren't special enough to break the rules.
    Although practicality beats purity.
    Errors should never pass silently.
    Unless explicitly silenced.
    In the face of ambiguity, refuse the temptation to guess.
    There should be one-- and preferably only one --obvious way to do it.
    Although that way may not be obvious at first unless you're Dutch.
    Now is better than never.
    Although never is often better than *right* now.
    If the implementation is hard to explain, it's a bad idea.
    If the implementation is easy to explain, it may be a good idea.
    Namespaces are one honking great idea -- let's do more of those!"""
    lista_lineas = text.splitlines()

    lineas = len(lista_lineas)
    print('Total de lineas: ',lineas)

    palabras = len(text.split())
    print(f'Total de palabras: {palabras}')

    prom = palabras/lineas
    print(f'Promedio palabras por linea: {prom:.2f}')

    print('Lineas por encima del promedio: ')
    for linea in lista_lineas:
        if len(linea.split()) > prom:
            print(f' - "{linea}" ({len(linea.split())} palabras)')


