from test.Puntuacion.py import calcular_puntuacion
 
def test_puntuacion_coresponde():
   """"
   Definimos la funcion de prueba para verificar la puntuacion

   """"
   puntos : int=  102   # Damos los puntos
   bonus : bool = True   # Damos los bonus
   expect: str  = "oro" # Damos Establecemos el tio de medalla 
   result : str = calcular_puntuacion(puntos , bonus) # Llamamos a la funcion y guardamos el resultdo
   assert expect == result  # Comprobamos que el resulta sea el esperado

   puntos: int=  88
   bonus : bool = ()  
   expect: str  = "Plata"
   result : str = calcular_puntuacion(puntos , bonus)
   assert expect == result 
   
   puntos: int=  20
   bonus : bool = ()  
   expect: str  = "Bronce"
   result : str = calcular_puntuacion(puntos , bonus)
   assert expect == result 


   puntos: int=  117
   bonus : bool = ()  
   expect: str  = "Oro"
   result : str = calcular_puntuacion(puntos , bonus)
   assert expect == result 


   puntos: int=  40
   bonus : bool = ()  
   expect: str  = "Plata"
   result : str = calcular_puntuacion(puntos , bonus)
   assert expect == result 

