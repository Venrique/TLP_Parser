from re import A
from s_lexer import *

SAritm=0
ZAritm=1
AAritm=2
BAritm=3
CAritm=4
DAritm=5

empty = ['vacia']

tablaAritm = [
        #SArtim
        [SAritm, 'eof', None ],
        [SAritm, 'SUMAR', None ],
        [SAritm, 'RESTAR', None ],
        [SAritm, 'MULTIPLICAR', None ],
        [SAritm, 'DIVIDIR', None ],
        [SAritm, 'MODULO', None ],
        [SAritm, 'PAREN_IZQ', [AAritm,ZAritm]],
        [SAritm, 'PAREN_DER', None ],
        [SAritm, 'IDENTIFICADOR', [AAritm,ZAritm]],
        [SAritm, 'NUMERO_DECIMAL', [AAritm,ZAritm]],
        [SAritm, 'NUMERO_ENTERO', [AAritm,ZAritm]],
        [SAritm, 'CORCHETE_IZQ', None],
        [SAritm, 'CORCHETE_DER', None],
        #ZAritm
        [ZAritm, 'eof', empty ],
        [ZAritm, 'SUMAR', ['SUMAR',AAritm,ZAritm]],
        [ZAritm, 'RESTAR', ['RESTAR',AAritm,ZAritm] ],
        [ZAritm, 'MULTIPLICAR', None ],
        [ZAritm, 'DIVIDIR', None ],
        [ZAritm, 'MODULO', None ],
        [ZAritm, 'PAREN_IZQ', None],
        [ZAritm, 'PAREN_DER', empty ],
        [ZAritm, 'IDENTIFICADOR', None],
        [ZAritm, 'NUMERO_DECIMAL', None],
        [ZAritm, 'NUMERO_ENTERO', None],
        [ZAritm, 'CORCHETE_IZQ', None],
        [ZAritm, 'CORCHETE_DER', None],
        #AAritm
        [AAritm, 'eof', None ],
        [AAritm, 'SUMAR', None],
        [AAritm, 'RESTAR', None ],
        [AAritm, 'MULTIPLICAR', None ],
        [AAritm, 'DIVIDIR', None ],
        [AAritm, 'MODULO', None ],
        [AAritm, 'PAREN_IZQ', [CAritm,BAritm]],
        [AAritm, 'PAREN_DER', None ],
        [AAritm, 'IDENTIFICADOR', [CAritm,BAritm]],
        [AAritm, 'NUMERO_DECIMAL', [CAritm,BAritm]],
        [AAritm, 'NUMERO_ENTERO', [CAritm,BAritm]],
        [AAritm, 'CORCHETE_IZQ', None],
        [AAritm, 'CORCHETE_DER', None],
        #BAritm
        [BAritm, 'eof', empty ],
        [BAritm, 'SUMAR', empty],
        [BAritm, 'RESTAR', empty ],
        [BAritm, 'MULTIPLICAR', ['MULTIPLICAR',CAritm,BAritm] ],
        [BAritm, 'DIVIDIR', ['DIVIDIR',CAritm,BAritm] ],
        [BAritm, 'MODULO', ['MODULO',CAritm,BAritm] ],
        [BAritm, 'PAREN_IZQ', None],
        [BAritm, 'PAREN_DER', empty ],
        [BAritm, 'IDENTIFICADOR', None],
        [BAritm, 'NUMERO_DECIMAL', None],
        [BAritm, 'NUMERO_ENTERO', None],
        [BAritm, 'CORCHETE_IZQ', None],
        [BAritm, 'CORCHETE_DER', None],
        #CAritm
        [CAritm, 'eof', None ],
        [CAritm, 'SUMAR', None],
        [CAritm, 'RESTAR', None ],
        [CAritm, 'MULTIPLICAR', None ],
        [CAritm, 'DIVIDIR', None ],
        [CAritm, 'MODULO', None ],
        [CAritm, 'PAREN_IZQ', ['PAREN_IZQ',SAritm,'PAREN_DER']],
        [CAritm, 'PAREN_DER', None ],
        [CAritm, 'IDENTIFICADOR', ['IDENTIFICADOR',DAritm]],
        [CAritm, 'NUMERO_DECIMAL', ['NUMERO_DECIMAL']],
        [CAritm, 'NUMERO_ENTERO', ['NUMERO_ENTERO']],
        [CAritm, 'CORCHETE_IZQ', None],
        [CAritm, 'CORCHETE_DER', None],
        #DAritm
        [DAritm, 'eof', empty ],
        [DAritm, 'SUMAR', empty],
        [DAritm, 'RESTAR', empty ],
        [DAritm, 'MULTIPLICAR', empty ],
        [DAritm, 'DIVIDIR', empty ],
        [DAritm, 'MODULO', empty ],
        [DAritm, 'PAREN_IZQ', None],
        [DAritm, 'PAREN_DER', empty ],
        [DAritm, 'IDENTIFICADOR', None],
        [DAritm, 'NUMERO_DECIMAL', None],
        [DAritm, 'NUMERO_ENTERO', None],
        [DAritm, 'CORCHETE_IZQ', ['CORCHETE_IZQ', 'NUMERO_ENTERO', 'CORCHETE_DER']],
        [DAritm, 'CORCHETE_DER', None]
    ]

tabla = tablaAritm

stack = ['eof', 0]

def customParser(f):
    #f = open('fuente.c','r')
    #lexer.input(f.read())
    lexer.input('2+2$')
    
    tok=lexer.token()
    x=stack[-1] #primer elemento de der a izq
    while True:    
        if x == tok.type and x == 'eof':
            print("Cadena reconocida exitosamente")
            return #aceptar
        else:
            if x == tok.type and x != 'eof':
                stack.pop()
                x=stack[-1]
                tok=lexer.token()                
            if x in tokens and x != tok.type:
                print("Error: se esperaba ", tok.type)
                return 0;
            if x not in tokens: #es no terminal
                print("van entrar a la tabla:")
                print(x)
                print(tok.type)
                celda=buscar_en_tabla(x,tok.type)                            
                if  celda is None:
                    print("Error: NO se esperaba", tok.type)
                    print("En posición:", tok.lexpos)
                    return 0;
                else:
                    stack.pop()
                    agregar_pila(celda)
                    print(stack)
                    print("------------")
                    x=stack[-1]            

            
        #if not tok:
            #break
        #print(tok)
        #print(tok.type, tok.value, tok.lineno, tok.lexpos)

def buscar_en_tabla(no_terminal, terminal):
    for i in range(len(tabla)):
        if( tabla[i][0] == no_terminal and tabla[i][1] == terminal):
            return tabla[i][2] #retorno la celda

def agregar_pila(produccion):
    for elemento in reversed(produccion):
        if elemento != 'vacia': #la vacía no la inserta
            stack.append(elemento)

f = open('./source/ExampleC.c','r')
customParser(f)
f.close()