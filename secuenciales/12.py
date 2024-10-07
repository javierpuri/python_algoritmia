import os 
os.system("cls")

numero = int ( input( "Número :") )

días =["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
if numero >= 1 and numero <= 7: print( días[numero - 1] )
else : print("error")

#if ( numero == 1 ) : print("lunes")
#elif ( numero == 2 ) : print("martes")
#elif ( numero == 3 ) : print("miércoles")
#elif ( numero == 4 ) : print("jueves")
#elif ( numero == 5 ) : print("lunes")
#elif ( numero == 6 ) : print("sábado")
#elif ( numero == 7 ) : print("domingo")
#else : print ("errror")