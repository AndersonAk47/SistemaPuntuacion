from TelefonoFormato.src.Telefono.Telefono import verificar_telefono

def test_deberia_tener_4_grupos_numerios():
   """"
   Definimos la funcion de prueba para verificar la el formato del telefono
   
   """   
   formato:str = +20-323-754-9745
   telefo:str = +20-323-754-9745  # Damos un numero telefonico
   expect: bool = True              # Resultado esperado
   resut: bool = verificar_telefono (telefo , formato) # Llamamos a la funcion y guardamos el resultdo
   assert expect == resut   # Comprobamos que el resulta sea el esperado

   

def test_deberia_ser_numericos():
   """"
   Definimos la funcion de prueba para verificar la el formato del telefono
   
   """   
   formato:str = +20-323-754-9745
   telefo:str = +20-323-754-9745  # Damos un numero telefonico
   expect: bool = True              # Resultado esperado
   resut: bool = verificar_telefono (telefo , formato) # Llamamos a la funcion y guardamos el resultdo
   assert expect == resut   # Comprobamos que el resulta sea el esperado

   


def test_deberia_iniciar_con_mas():
   """"
   Definimos la funcion de prueba para verificar que inicie con + telefono
   
   """   
   formato:str = +20-323-754-9745
   telefo:str = +20-323-754-9745  # Damos un numero telefonico
   expect: bool = True              # Resultado esperado
   resut: bool = verificar_telefono (telefo , formato) # Llamamos a la funcion y guardamos el resultdo
   assert expect == resut   # Comprobamos que el resulta sea el esperado
   

def test_el_primer_grupo_de_numero_deberia_ser_de_dos_cifras():
   """"
   Definimos la funcion de prueba para verificar que
   lel primer gruupo de numeros sea de dos cifras
   
   """   
   formato:str = +20-323-754-9745
   telefo:str = +20-323-754-9745  # Damos un numero telefonico
   expect: bool = True              # Resultado esperado
   resut: bool = verificar_telefono (telefo , formato) # Llamamos a la funcion y guardamos el resultdo
   assert expect == resut   # Comprobamos que el resulta sea el esperado
   


def test_deberia_ingresar_12_numero():
   """"
   Definimos la funcion de prueba para verificar que
   ingrese 12 numeros 
   
   """   
   formato:str = +34-732-453-2445
   telefo:str = +34-732-453-2445  # Damos un numero telefonico
   expect: bool = True              # Resultado esperado
   resut: bool = verificar_telefono (telefo , formato) # Llamamos a la funcion y guardamos el resultdo
   assert expect == resut   # Comprobamos que el resulta sea el esperado



def test_el_segundo_y_tercer_grupo_de_numeros_deberia_ser_de_tres_cifras():
   """"
   Definimos la funcion de prueba para verificar que
   el segundo y tercer  gruupo de numeros sea de tres cifras
   
   """   
   formato:str = +12-342-324-3374
   telefo:str = +12-342-324-3374  # Damos un numero telefonico
   expect: bool = True              # Resultado esperado
   resut: bool = verificar_telefono (telefo , formato) # Llamamos a la funcion y guardamos el resultdo
   assert expect == resut   # Comprobamos que el resulta sea el esperado



def test_el_cuarto_grupo_de_numero_deberia_ser_de_tres_cifras():
   """"
   Definimos la funcion de prueba para verificar que
   el cuarto gruupo de numeros sea de tres cifras
   
   """   
   formato:str = +32-569-346-3220
   telefo:str = +32-569-346-3220  # Damos un numero telefonico
   expect: bool = True              # Resultado esperado
   resut: bool = verificar_telefono (telefo , formato) # Llamamos a la funcion y guardamos el resultdo
   assert expect == resut   # Comprobamos que el resulta sea el esperado



def test_no_debe_contener_letras():
   """"
   Definimos la funcion de prueba para verificar que
   no ingrese letras
   
   """   
   formato:str = +32-56E-346-3220
   telefo:str = +32-56E-346-3220  # Damos un numero telefonico
   expect: bool = False             # Resultado esperado
   resut: bool = verificar_telefono (telefo , formato) # Llamamos a la funcion y guardamos el resultdo
   assert expect == resut   # Comprobamos que el resulta sea el esperado



def test_no_debe_contener_espacios():
   """"
   Definimos la funcion de prueba para verificar que
   no ingrese espacios
   
   """   
   formato:str = +32-56 -346-3220
   telefo:str = +32-56 -346-3220  # Damos un numero telefonico
   expect: bool = False             # Resultado esperado
   resut: bool = verificar_telefono (telefo , formato) # Llamamos a la funcion y guardamos el resultdo
   assert expect == resut   # Comprobamos que el resulta sea el esperado


def test_los_grupos_deben_ser_separados_por_un_guion_medio():
   """"
   Definimos la funcion de prueba para verificar que
   los grupos esten separados por un guion medio 
   
   """   
   formato:str = +32-563-346-3220
   telefo:str = +32-563-346-3220  # Damos un numero telefonico
   expect: bool = False             # Resultado esperado
   resut: bool = verificar_telefono (telefo , formato) # Llamamos a la funcion y guardamos el resultdo
   assert expect == resut   # Comprobamos que el resulta sea el esperado
