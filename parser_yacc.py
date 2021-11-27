import ply.yacc as yacc
from s_lexer import *
from gramaticas.init import *

VERBOSE = 1

def p_empty(p):
    'empty :'
    pass

def p_error( p ):
    if VERBOSE:
        if p is not None:
            print ("Error en Sintaxis linea:" + str(p.lexer.lineno)+"  Error de Contexto " + str(p.value))
        else:
            print ("Error en Lexico linea: " + str(lexer.lineno))
    else:
        raise Exception('Syntax', 'error')

parser = yacc.yacc()

f = open('./source/ExampleCYacc.c','r')
res = parser.parse(f.read()) # the input
print(res)
f.close()