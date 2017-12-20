def cifrar():
    msg1 = input("Ingrese un mensaje a cifrar: ")
    lista1 = list(msg1)
    msgc = ""
    abrir()
    for i in lista1:
        a = ord(i)
        b = a + e
        msgc += chr(b)
    print("Mensaje cifrado: "+msgc)

def descifrar():
    msg2 = input("Ingrese un mensaje cifrado: ")
    msgd = ""
    abrir()
    for f in msg2:
        c = ord(f)
        d = c - e
        msgd += chr(d)
    print("Mensaje descifrado: "+msgd)

def abrir():
    arch= open('num.txt','r')
    linea= arch.readline()
    global e
    e= int(float(linea))
    arch.close()

def hacer():
    f=open('num.txt',"w")
    f.write(num)
    f.close()

def banner():
    print('\033[1;94m'"""
    ______  ___    _____                   
    ___   |/  /______  /_____________ _    
    __  /|_/ /_  _ \  __/_  ___/  __ `/    
    _  /  / / /  __/ /_ _  /   / /_/ /     
    /_/  /_/  \___/\__/ /_/    \__,_/ 
    """'\033[1;94m')
    mg= ("HiddenShot")
    long= len(mg) + 8
    print('\033[1;91m'"#"+ long * '-' + "#"'\033[1;91m')
    print("|"+ long*' '+"|")
    print("|"+4*' '+mg+4*' '+"|")
    print("|"+ long * ' ' + "|")
    print("#"+ long * '-' + "#")

banner()

while(True):

    print("""
    Opciones:
    1- Cifrar mensaje
    2- Descifrar mensaje
    3- Configurar
    4- Salir
    """)
    print('\033[1;93m'"***Recuerda configurar tu numero modificador***"'\033[1;93m')

    opc1= input('\033[1;91m'">> "'\033[1;91m')
    if opc1 == '1':

        cifrar()

    elif opc1 == '2':

        descifrar()

    elif opc1 == '3':

        while(True):

            print("""
    Opciones:
    1- Cambiar el numero modificador
    2- Regresar
            """)

            opc2= input('\033[1;91m'">> "'\033[1;91m')

            if opc2 == '1':

                num= input("Ingrese su numero modificador: ")
                hacer()

            elif opc2 == '2':

                break

    elif opc1 == '4':

        break

    else:
        print("Eliga una opcion correcta")
