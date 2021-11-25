import ply.yacc as yacc
from s_lexer import *
from gramaticas.init import *
from gramaticas.op_aritmeticas import *
from gramaticas.op_logicas import *

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

# id + ( id * num.decimal )
res = parser.parse("2>1+1") # the input
print(res)