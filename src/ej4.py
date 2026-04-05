def ej_4():
    mail = input('ingrese un email: ')

    if (mail.count('@') == 1 and mail.index('@')>0 and '.' in mail[mail.index('@'):] 
        and not(mail.startswith('@') or mail.endswith('@')) and 
        not(mail.startswith('.') or mail.endswith('.')) and
        len(mail.split(".")[-1]) >= 2) :
            print('email valido')
    else:
            print('email no valido')


        