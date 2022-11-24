from random import choice   # importarmos la funcion CHOICE del modulo RANDOM

def Welcome():
    print("############## GENERADOR DE PASSWORDS ##############\n") # Bienvenida
    run()
def run():
    try:
        longitud = int(input("\tDigame la longitud de su Password deseado: "))    # creamos la longitud del password.
        if longitud < 200:  # le damos un limite de caracteres.
            valores = "1234567890avbcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+{\}|:/.,?>\<"

            p = "" # creamos una variable vacia para que la vaya rellenando
            p = p.join([choice(valores) for i in range(longitud)]) 

            ''' -metodo .join = para unir en una sola variable las variables i.
                    -choice = eligira a eleccion los valores.
                        -bucle for = para repetirlo las veces que el usuario lo diga
                            -todo se guardara = en la variable p
                '''

            printLong = str(longitud) # pasamos el int(longitud) a str para concatenarlo al print de abajo
            print("\n \tTu password de " + printLong + " caracteres es --> " + p + " <-- Thank You!") # imprimimos el password al usuario
        else:
            print("\n\t ESTAS COLOCANDO UN NUMERO DEMASIADO ALTO!!") # Le avisamos el limite de caracteres
            run()
    except:
        print("\n\tPOR FAVOR COLOCA SOLO NUMEROS ENTEROS!!") # Excepcion: solo numeros enteros
        run()


if __name__ == "__main__":  
    Welcome()   # ses ejecuta como primera funcion