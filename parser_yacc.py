import ply.yacc as yacc
from s_lexer import *
from gramaticas.init import *
import logging
logging.basicConfig(
    level = logging.INFO,
    filename = "parselog.txt",
    filemode = "w",
    format = "%(filename)10s:%(lineno)4d:%(message)s"
)
log = logging.getLogger()

error = 0

def p_empty(p):
    'empty :'
    pass

def p_error( p ):
    global error
    error=1
    if p is not None:
        print ("Error en Sintaxis en la línea: " + str(p.lexer.lineno)+" | No se esperaba '" + str(p.value)+"'")
        print ("\tProbando reparar con el siguiente token...\n")
        parser.errok()
    else:
        print ("Error en Léxico hasta EOF, no ha sido posible recuperarse.")

parser = yacc.yacc()
f = open('./source/'+input("Ingrese solo el nombre del archivo .c que desea parsear\n(debe estar contenido en la carpeta 'Source'): ")+'.c','r')
print("\nINICIANDO PARSEO")
print("----------------------------------------------------------\n")
res = parser.parse(f.read())
#print(parser.value) # the input
print("\n----------------------------------------------------------")
if error == 0:
    print('Parseo completado exitosamente')
else:
    print('Parseo completado con errores')

f.close()
