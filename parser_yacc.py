import ply.yacc as yacc
from s_lexer import *
from gramaticas.init import *

def recorrerArbol(nodo, archivoArbol, level=0):
    if nodo is not None:
        print("\t"*level,'<'+nodo.type+'>', file=archivoArbol)
        for i in nodo.contents:
            if type(i) is list:
                recorrerArbol(i[0],archivoArbol,level+1)
            else:
                print("\t"*level, "'"+str(i)+"'", file=archivoArbol)

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
nombreArchivo = input("Ingrese solo el nombre del archivo .c que desea analizar\n(debe estar contenido en la carpeta 'Source'): ")
f = open('./source/'+nombreArchivo+'.c','r')
print("\nIniciando análisis sintáctico")
print("----------------------------------------------------------\nERRORES:")
res = parser.parse(f.read())
if error == 0:
    print("Ninguno")
print("----------------------------------------------------------")
if error == 0:
    print('\nAnálisis sintáctico completado exitosamente')
    salida = open('./resultados/Árbol sintáctico - '+nombreArchivo+'.txt','w', encoding="utf-8")
    print('', file=salida)
    salida.close()
    salida = open('./resultados/Árbol sintáctico - '+nombreArchivo+'.txt','a', encoding="utf-8")
    recorrerArbol(res,salida)
    salida.close()
    print("\nÁrbol sintáctico generado en \"./resultados/Árbol sintáctico - "+nombreArchivo+".txt\"")
else:
    print('\nAnálisis sintáctico completado con errores')

f.close()