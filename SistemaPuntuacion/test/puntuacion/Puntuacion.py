from SistemaPuntuacion.src.puntuacion.Puntuacion import calcular_puntuacion
 
 
def test_puntuacion_igual_o_mayor_a_100_mas_bonus():
   """"
   Definimos la funcion para verificar si obtiene  Oro 

   """
   puntos : int=  102       # Damos los puntos
   bonus : bool = True      # Damos los bonus
   expect: str  = "Oro"     # Resultado esperado 
   result : str = calcular_puntuacion(puntos , bonus) # Llamamos a la funcion y guardamos el resultdo
   assert expect == result  # Comprobamos que el resulta sea el esperado

s
def test_puntuacion_igual_o_mayor_a_50_sin_bonus():
   """"
   Definimos la funcion para verificar si obtiene  Plata 

   """
   puntos : int=  63       # Damos los puntos
   bonus : bool = False     # Damos los bonus
   expect: str  = "Plata"     # Resultado esperado 
   result : str = calcular_puntuacion(puntos , bonus) # Llamamos a la funcion y guardamos el resultdo
   assert expect == result  # Comprobamos que el resulta sea el esperado
  


def test_puntuacion_menor_a_50_o_sin_bonus():
   """"
   Definimos la funcion para verificar si obtiene Broce 

   """
   puntos : int=  46       # Damos los puntos
   bonus : bool = False    # Damos los bonus
   expect: str  = "Bronce"     # Resultado esperado 
   result : str = calcular_puntuacion(puntos , bonus) # Llamamos a la funcion y guardamos el resultdo
   assert expect == result  # Comprobamos que el resulta sea el esperado



def test_puntuacion_igual_a_100_sin_bonus():
   """"
   Definimos la funcion para verificar si obtiene el Plata 

   """
   puntos : int=  100       # Damos los puntos
   bonus : bool = False     # Damos los bonus
   expect: str  = "Plata"     # Resultado esperado 
   result : str = calcular_puntuacion(puntos , bonus) # Llamamos a la funcion y guardamos el resultdo
   assert expect == result  # Comprobamos que el resulta sea el esperado



def test_puntuacion_entre_50_y_99_con_bonus():
   """"
   Definimos la funcion para verificar si obtiene el Bronce 

   """
   puntos : int=  76       # Damos los puntos
   bonus : bool = False      # Damos los bonus
   expect: str  = "Bronce"     # Resultado esperado 
   result : str = calcular_puntuacion(puntos , bonus) # Llamamos a la funcion y guardamos el resultdo
   assert expect == result  # Comprobamos que el resulta sea el esperado


def test_puntuacion_menor_a_50_com_bonus():
   """"
   Definimos la funcion para verificar si obtiene el Plata 

   """
   puntos : int=  23      # Damos los puntos
   bonus : bool = True      # Damos los bonus
   expect: str  = "Plata"     # Resultado esperado 
   result : str = calcular_puntuacion(puntos , bonus) # Llamamos a la funcion y guardamos el resultdo
   assert expect == result  # Comprobamos que el resulta sea el esperado



def test_deberia_tener_puntos_sin_bonus():
   """"
   Definimos la funcion para verificar si obtiene  Bronce 

   """
   puntos : int=  0       # Damos los puntos
   bonus : bool = False      # Damos los bonus
   expect: str  = "Bronce"     # Resultado esperado 
   result : str = calcular_puntuacion(puntos , bonus) # Llamamos a la funcion y guardamos el resultdo
   assert expect == result  # Comprobamos que el resulta sea el esperado

