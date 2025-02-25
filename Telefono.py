def verificar_telefono (telefono , formato ) -> bool:
    """"
    Valida si el  telefono tienee el formato correspondiente 

    Retorno
    ---------
        srt: True si el telefono  es valido o False si no es valido 
    """
    if telefono ==  formato :
        return("valido")
    else:
        return("invalido")