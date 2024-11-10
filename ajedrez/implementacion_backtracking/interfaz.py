### EJERCICIO: Caballo Ajedrez
# TÉCNICA: Backtracking

#PSEUDOCÓDIGO:

# recorridoCaballo(S)
# Posiciones = casillasDisponibles(S)
# 	para cada p ∈ Posiciones 
# 		avanzarPosicion(S,p)
# 		//si Factible
# 		si largo(casillasDisponibles(S))>0 || esSolucion(S)
# 			si esSolucion(S)
# 				return S
# 			sino
# 				recorridoCaballo(S)
# 			fin si
# 		fin si
# 		volverPosicionAnterior(S,p)
# 	fin para
