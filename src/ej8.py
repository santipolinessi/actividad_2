def cifrado():
  
    mensaje = input('ingrese un mensaje: ')
    desp = int(input('ingrese un desplazamiento: '))

    resultado = ''
    descifrado = ''

    #CIFRADO
    
    for char in mensaje:
        if char.isalpha(): #solo letras
            base = ord('a') if char.islower() else ord('A') #ord convierte letra en nro

            nueva = (ord(char) - base + desp) % 26 + base 
            resultado += chr(nueva) #mantiene espacios y simbolos
        else:
            resultado += char

    #DESCIFRADO

    for char in resultado:
        if char.isalpha(): 
            base = ord('a') if char.islower() else ord('A') 

            nueva = (ord(char) - base - desp) % 26 + base
            descifrado += chr(nueva)
        else:
            descifrado += char

    print('mensaje cifrado: ',resultado)
    print('mensaje descifrado: ',descifrado)
    