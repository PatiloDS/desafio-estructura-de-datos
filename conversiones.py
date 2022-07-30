#Patricio Carrasco



#tasa de conversion
#sol peruano: 0.0046
#peso argentino: 0.093
#dolar americano: 0.00013

import sys

sol_peruano = float(sys.argv[1])
peso_argentino = float(sys.argv[2])
dolar_americano = float(sys.argv[3])
pesos_chilenos = int(sys.argv[4])

print(f"los $ {pesos_chilenos} pesos es igual a :")
print(f"{sol_peruano} Soles")
print(f"{peso_argentino} Pesos argentinos")
print(f"{dolar_americano} Dolares")