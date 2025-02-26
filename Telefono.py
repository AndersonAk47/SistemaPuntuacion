def verificar_telefono (telefono: str , formato: str ) -> bool:
    """"
    Valida si el  telefono tiene el formato correspondiente 

    Retorno
    ---------
        srt: True si el telefono  es valido o False si no es valido 
    """

    if formato ==  telefono :
        return(" El formato es valido")
    else:
        return(" El formati es invalido")