from test.Puntuacion.py import calcular_puntuacion
 
def test_puntuacion_coresponde():
   """"
   Definimos la funcion de prueba para verificar la puntuacion

   """"
   puntos : int=  102       # Damos los puntos
   bonus : bool = True      # Damos los bonus
   expect: str  = "oro"     # Resultado esperado 
   result : str = calcular_puntuacion(puntos , bonus) # Llamamos a la funcion y guardamos el resultdo
   assert expect == result  # Comprobamos que el resulta sea el esperado

   puntos: int=  88        # Damos los puntos
   bonus : bool = ()       # Damos los bonus
   expect: str  = "Plata"  # Resultado esperado
   result : str = calcular_puntuacion(puntos , bonus) # Llamamos a la funcion y guardamos el resultdo
   assert expect == result # Comprobamos que el resulta sea el esperado
   
   puntos: int=  20        # Damos los puntos
   bonus : bool = ()       # Damos los bonus
   expect: str  = "Bronce" # Resultado esperado
   result : str = calcular_puntuacion(puntos , bonus)  # Llamamos a la funcion y guardamos el resultdo
   assert expect == result   # Comprobamos que el resulta sea el esperado


   puntos: int=  117       # Damos los puntos
   bonus : bool = ()       # Damos los bonua
   expect: str  = "Oro"    # Resultado esperado
   result : str = calcular_puntuacion(puntos , bonus)  # Llamamos a la funcion y guardamos el resultdo
   assert expect == result   # Comprobamos que el resulta sea el esperado


   puntos: int=  40         # Damos los puntos
   bonus : bool = ()        # Damos los bonus
   expect: str  = "Bronce"  # Resultado
   result : str = calcular_puntuacion(puntos , bonus)  # Llamamos a la funcion y guardamos el resultdo
   assert expect == result   # Comprobamos que el resulta sea el esperado


   puntos : int=  154       # Damos los puntos
   bonus : bool = True      # Damos los bonus
   expect: str  = "oro"     # Resultado esperado 
   result : str = calcular_puntuacion(puntos , bonus) # Llamamos a la funcion y guardamos el resultdo
   assert expect == result  # Comprobamos que el resulta sea el esperado


   puntos: int=  36         # Damos los puntos
   bonus : bool = ()        # Damos los bonus
   expect: str  = "Bronce"  # Resultado
   result : str = calcular_puntuacion(puntos , bonus)  # Llamamos a la funcion y guardamos el resultdo
   assert expect == result   # Comprobamos que el resulta sea el esperado



   puntos: int=  58        # Damos los puntos
   bonus : bool = ()       # Damos los bonus
   expect: str  = "Plata"  # Resultado esperado
   result : str = calcular_puntuacion(puntos , bonus) # Llamamos a la funcion y guardamos el resultdo
   assert expect == result # Comprobamos que el resulta sea el esperado


   puntos : int=  172      # Damos los puntos
   bonus : bool = True      # Damos los bonus
   expect: str  = "oro"     # Resultado esperado 
   result : str = calcular_puntuacion(puntos , bonus) # Llamamos a la funcion y guardamos el resultdo
   assert expect == result  # Comprobamos que el resulta sea el esperado


   puntos: int=  43       # Damos los puntos
   bonus : bool = ()       # Damos los bonus
   expect: str  = "Bronce" # Resultado esperado
   result : str = calcular_puntuacion(puntos , bonus)  # Llamamos a la funcion y guardamos el resultdo
   assert expect == result   # Comprobamos que el resulta sea el esperado