def calcular_puntuacion ( puntos, bonus ):
    """"
    Verificamos la cantida de puntos y si hay bonus

    Retorno
    ---------
        srt: Tipo de medalla obtenia = Oro , Plata,  Bronce
    """
    if puntos >= 100 and bonus:   # Se veifica si los puntos son  100 o mas      
        return ("Has obtenido la medalla de:  Oro") 
    
    elif puntos >= 50 and puntos < 100 : # Se veifica si los puntos estan entre 50 y 100 
        return("Has obtenido la medalla de: Plata")
    elif puntos < 50 and bonus:
        return ("Has obtenido la medalla de: Bronce") # Se veifica si los son menores de 50
