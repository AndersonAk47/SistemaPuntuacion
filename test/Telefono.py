from test.Telefono.py import verificar_telefono
 
def test_formato_telefono():
   """"
   Definimos la funcion de prueba para verificar la el formato del telefono
   
   """   
   formato: str = +20-323-754-9745  # Defiimos formato
   telefono:str = +20-323-754-9745  # Damos un numero telefonico
   expect: bool = True              # Resultado esperado
   resut:str = verificar_telefono (telefono , formato) # Llamamos a la funcion y guardamos el resultdo
   assert expect == resut   # Comprobamos que el resulta sea el esperado

   formato: str = +20-323-754-9745  # Defiimos formato
   telefono:str = +20-3A3-7R4-9745  # Damos un numero telefonico
   expect: bool = False              # Resultado esperado
   resut:str = verificar_telefono (telefono , formato) # Llamamos a la funcion y guardamos el resultdo
   assert expect == resut   # Comprobamos que el resulta sea el esperado


   formato: str = +13-567-234-3433  # Defiimos formato
   telefono:str = +13-567-234-3433  # Damos un numero telefonico
   expect: bool = True              # Resultado esperado
   resut:str = verificar_telefono (telefono , formato) # Llamamos a la funcion y guardamos el resultdo
   assert expect == resut   # Comprobamos que el resulta sea el esperado


   formato: str = +13-567-234-3433  # Defiimos formato
   telefono:str = +1*-567-234-3S33  # Damos un numero telefonico
   expect: bool = False              # Resultado esperado
   resut:str = verificar_telefono (telefono , formato) # Llamamos a la funcion y guardamos el resultdo
   assert expect == resut   # Comprobamos que el resulta sea el esperado


   formato: str = +23-843-342-2847  # Defiimos formato
   telefono:str = +23-843-342-2847  # Damos un numero telefonico
   expect: bool = True              # Resultado esperado
   resut:str = verificar_telefono (telefono , formato) # Llamamos a la funcion y guardamos el resultdo
   assert expect == resut   # Comprobamos que el resulta sea el esperado

   formato: str = +40-333-434-247  # Defiimos formato
   telefono:str = +40-3+3-W34-247  # Damos un numero telefonico
   expect: bool = False              # Resultado esperado
   resut:str = verificar_telefono (telefono , formato) # Llamamos a la funcion y guardamos el resultdo
   assert expect == resut   # Comprobamos que el resulta sea el esperado


   formato: str = +34-334-727-9265  # Defiimos formato
   telefono:str = +34-334-727-9265  # Damos un numero telefonico
   expect: bool = True              # Resultado esperado
   resut:str = verificar_telefono (telefono , formato) # Llamamos a la funcion y guardamos el resultdo
   assert expect == resut   # Comprobamos que el resulta sea el esperado


   formato: str = +21-954-945-4123  # Defiimos formato
   telefono:str = +21-954-945-4123  # Damos un numero telefonico
   expect: bool = True              # Resultado esperado
   resut:str = verificar_telefono (telefono , formato) # Llamamos a la funcion y guardamos el resultdo
   assert expect == resut   # Comprobamos que el resulta sea el esperado


   formato: str = +20-832-234-2402  # Defiimos formato
   telefono:str = ++0-832-234-24O2  # Damos un numero telefonico
   expect: bool = True              # Resultado esperado
   resut:str = verificar_telefono (telefono , formato) # Llamamos a la funcion y guardamos el resultdo
   assert expect == resut   # Comprobamos que el resulta sea el esperado

   formato: str = +20-323-754-9745  # Defiimos formato
   telefono:str = +20-323-754-9745  # Damos un numero telefonico
   expect: bool = True              # Resultado esperado
   resut:str = verificar_telefono (telefono , formato) # Llamamos a la funcion y guardamos el resultdo
   assert expect == resut   # Comprobamos que el resulta sea el esperado

