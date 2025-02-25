from test.Telefono.py import verificar_telefono
 
def test_formato_telefono():
   
   formato: str = +20-323-754-9745
   telefono:str = +20-323-754-9745
   expect: bool = True
   resut:str = verificar_telefono (telefono , formato)
   assert expect == resut