#programa calcular el interes de una coac
def calcular_interes(monto,encaje,tiempo,interes=19):
    calculo = monto * tiempo 
    calculo = encaje
    subvalor = (calculo* interes)/100
    valor_interes= calculo + subvalor
    return valor_interes

def interes_de_prestamista(otromonto):
   monto = (otromonto * 21)/100
   return monto  
    
    
while True:
    print("----Bienvenidos a la COAC ESTATAL-----")
    print("----Simulador de Creditos ----")
    print("1.- COAC ESTATAL")
    print("2.- prestamista")
    opcion = int(input("Ingrese una opcion:"))
    if opcion == 3:
        print("Gracias por su cooperacion")

