#Jossian Abimelec García Quijano
#Calcula el rendimiento a partir de los kilometros que recorrio y la cantidad de gasolina que utilizo asi como litros necesarios para recorrer cierta distancia



def calcularRendimiento(kilometros, gasolina):
    rendimiento=kilometros/gasolina
    return rendimiento


def calcularConversion(rendimiento):
    conversion=(rendimiento*3.785)/1.6093
    return conversion

def calcularLitros(kilometrosrecorrer, gasolina,kilometros):
    litrosrecorrer=(kilometrosrecorrer*gasolina)/kilometros
    return litrosrecorrer

def main():
    kilometros = int(input("Teclea el número de kilometros recorridos: "))
    gasolina = int(input("Teclea el número de litros de gasolina usados: "))
    rendimiento = calcularRendimiento(kilometros, gasolina)
    conversion = calcularConversion(rendimiento)
    print("Si recorres %.0f"%kilometros,"kms con %.0f"%gasolina," litros de gasolina, el rendimiento es: \n%.2f"%rendimiento,"km/l \n%.2f"%conversion,"mi/gal")
    kilometrosrecorrer = int(input("¿Cuántos kilometros vas a recorrer?"))
    litros = calcularLitros(kilometrosrecorrer,gasolina, kilometros)
    print("Para recorrer %.0f"%kilometrosrecorrer,"km. necesitas %.2f"%litros,"litros de gasolina")

main()