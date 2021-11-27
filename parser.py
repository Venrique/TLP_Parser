from re import A
from s_lexer import *
from tablasGramaticas import *

stack = ['eof', SWhile]

def customParser(f):
    global tok
    global x
    #f = open('fuente.c','r')
    #lexer.input(f.read())
    lexer.input(f+'$')
    tok=lexer.token()
    x=stack[-1] #primer elemento de der a izq
    parserGen(tablaWhile)

def parserGen(tablaParsing):
    global tok
    global x
    while True:
        print("TOKEN: ",tok.type)
        print("X: ",x)
        if x == tok.type and x == 'eof':
            print("Cadena reconocida exitosamente")
            return #aceptar
        else:
            if x == tok.type and x != 'eof':
                print('*Eliminando token: ',x)
                stack.pop()
                x=stack[-1]
                tok=lexer.token()
                if x == SOpe:
                    parserGen(tablaOperaciones)
                elif x == SIfElse:
                    parserGen(tablaIfElse)
                elif x == SWhile:
                    parserGen(tablaWhile)    
            if x in tokens and x != tok.type:
                print("Error: Se esperaba ", x)
                print('en la posicion: ', tok.lexpos+1);
                return 0;
            print(tok.type)
            print('CHECKPOINT STACK: ',stack)    
            if x not in tokens: #es no terminal
                
                celda=buscar_en_tabla(x,tok.type,tablaParsing)                            
                if  celda is None:
                    print("Error: No se esperaba", tok.type)
                    print('en la posicion: ', tok.lexpos+1);
                    return 0;
                else:
                    stack.pop()
                    agregar_pila(celda)
                    x=stack[-1]
        print(stack)
        print('------------------------------------------------------------------')

def buscar_en_tabla(no_terminal,terminal,tabla):
    for i in range(len(tabla)):
        if( tabla[i][0] == no_terminal and tabla[i][1] == terminal):
            return tabla[i][2] #retorno la celda

def agregar_pila(produccion):
    for elemento in reversed(produccion):
        if elemento != 'vacia': #la vacía no la inserta
            stack.append(elemento)

f = open('./source/ExampleC.c','r')
customParser(f.read())
f.close()