saldo = 1000
def retirar (valor_retirar):
    if valor_retirar <= 0:
        print ("No se pueden retirar valores negativos. Intente nuevamente")
        valor_retirar = saldo
    elif valor_retirar > saldo:
        print("\nEl valor a retirar no puede ser mayor a tu saldo. \n tu saldo actual es de: ",saldo)
        valor_retirar = saldo    
    else: 
        valor_retirar = saldo - valor_retirar
    return valor_retirar


def depositar (valor_depositar):
    if valor_depositar <= 0:
        print ("No se pueden depositar valores negativos y mayores que 0. Intente nuevamente.")
        valor_depositar = saldo
    else:
        valor_depositar = valor_depositar + saldo
    return valor_depositar



def consultar_saldo ():
    print ("\n\n Su saldo actua es de: ", saldo)




def ingresar_dinero ():
    valord = int(input("Ingrese el valor a depositar: $"))
    return depositar(valord)


def sacar_dinero():
    valorr = int(input("Ingrese el valor a retirar: $"))
    return retirar(valorr)

def menu():
    print("""
*** CAJERO AUTOMATICO BANCO CAMPUS ***

1. Consultar saldo
2. Depositar dinero
3. Retirar dinero 
4. Salir

Si presionas 0 tambien saldras del sistema.

""")

def elegir_opcion():
    opcion = int(input(" Ingresa la accion que quieres realizar: "))
    while opcion < 0 or opcion > 4:
        print("Tienes que elegir una opcion entre 0 y 4")
        opcion = int(input(" Ingresa nuevamente la accion que quieres realizar: "))

    return opcion

while True:
    menu()
    opcion = elegir_opcion()
    
    match opcion:

        case 0: 
            print("Gracias por utilizat nuestros servicios")
            break 
        
        case 1:

            consultar_saldo()

        case 2:

            saldo = ingresar_dinero()

        case 3:

            saldo = sacar_dinero()

        case 4:
            print("Gracias por utilizat nuestros servicios")
            break



