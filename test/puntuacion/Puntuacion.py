from src.puntuacion.Puntuacion import calcular_puntuacion 
 
def test_puntuacion_igual_o_mayor_a_100_mas_bonus():
   """"
   Definimos la funcion para verificar si obtiene el Oro 

   """
   puntos : int=  102       # Damos los puntos
   bonus : bool = True      # Damos los bonus
   expect: str  = "oro"     # Resultado esperado 
   result : str = calcular_puntuacion(puntos , bonus) # Llamamos a la funcion y guardamos el resultdo
   assert expect == result  # Comprobamos que el resulta sea el esperado


def test_puntuacion_igual_o_mayor_a_50_sin_bonus():
   """"
   Definimos la funcion para verificar si obtiene el Plata 

   """
   puntos : int=  63       # Damos los puntos
   bonus : bool = ""      # Damos los bonus
   expect: str  = "Plata"     # Resultado esperado 
   result : str = calcular_puntuacion(puntos , bonus) # Llamamos a la funcion y guardamos el resultdo
   assert expect == result  # Comprobamos que el resulta sea el esperado
  