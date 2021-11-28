# Parser y Lexer de C

# _Un analizador sintáctico_

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)



[![python](https://img.shields.io/badge/python-3.10-green)](https://www.python.org/downloads/) [![GitHub](https://badgen.net/badge/icon/github?icon=github&label)](https://github.com)



Este proyecto esta desarrollado con el fin de visualizar el comportamiento de un analizador sintáctico.



## Instalación

Este proyecto requiere de [Python 3.10](https://www.python.org/downloads/) o mayor para correr.



## Pasos para utilizar el proyecto



Una vez tenga el proyecto en el directorio deseado y python instalado, se pueden correr 2 de los archivos dentro de la carpeta.



Para correr el analizador sintáctico utilizando la librería de yacc:

```Console
> python parser_yacc.py
```

Este comando pedirá al usuario que ingrese el nombre del archivo a analizar:

```Console

Ingrese solo el nombre del archivo .c que desea parsear

(debe estar contenido en la carpeta 'Source'):

```

 Y una vez ingresado el archivo, el programa se encargará de analizar el archivo de ejemplo, con lo que el output esperado es el siguiente:

```Console

Iniciando análisis sintáctico
----------------------------------------------------------
ERRORES:
Ninguno
----------------------------------------------------------

Análisis sintáctico completado exitosamente

Árbol sintáctico generado en "./resultados/Árbol sintáctico - ExampleCError.txt"

```



Para correr el analizador sintáctico diseñado por el equipo se debe ejecutar el comando:

```Console

> python parser.py

```



El output esperado para dicho analizador sintáctico es el siguiente:

```Console

TOKEN:  BUCLE_MIENTRAS

X:  25

BUCLE_MIENTRAS

CHECKPOINT STACK:  ['eof', 25]

['eof', 'LLAVE_DER', 6, 'LLAVE_IZQ', 'PAREN_DER', 0, 'PAREN_IZQ', 'BUCLE_MIENTRAS']

------------------------------------------------------------------

TOKEN:  BUCLE_MIENTRAS

X:  BUCLE_MIENTRAS

*Eliminando token:  BUCLE_MIENTRAS

PAREN_IZQ

CHECKPOINT STACK:  ['eof', 'LLAVE_DER', 6, 'LLAVE_IZQ', 'PAREN_DER', 0, 'PAREN_IZQ']

['eof', 'LLAVE_DER', 6, 'LLAVE_IZQ', 'PAREN_DER', 0, 'PAREN_IZQ']

------------------------------------------------------------------

```



Este output muestra paso por paso del analizador hasta llegar al final.



## Casos de error para los analizadores

Para el analizador sintáctico diseñado por el equipo se muestra el siguiente error al momento de no encontrar forma de analizar el token actual:
```Console
Iniciando análisis sintáctico
----------------------------------------------------------
ERRORES:
Error en Sintaxis en la línea: 2 | No se esperaba '5'
        Probando reparar con el siguiente token...

----------------------------------------------------------

Análisis sintáctico completado con errores
```


En el caso del analizador sintáctico diseñado por el equipo, al momento de encontrar algo que no puede analizar se muestra el siguiente output:
```Console
TOKEN:  TIPO_ENTERO
X:  25
TIPO_ENTERO
CHECKPOINT STACK:  ['eof', 25]
Error: No se esperaba TIPO_ENTERO
en la posicion:  1
```


## Ejemplos de código C a analizar
En este proyecto se utilizá un código de ejemplo en el lenguaje de alto nivel C:
```c
while (count < 10){
    if(5){
        
    }else if (5>variable && 1+2+3 < 6){


    }else if (test){


    }else{
        
    }
}
```


y también: 
```c
if(5){
        
}else if (5>variable && 1+2+3 < 6){


}else{
    
}
```
## Consideraciones


Este proyecto consta de 2 analizadores sintácticos:
1. Analizador sintáctico manual (diseñado por el equipo).
2. Analizador sintáctico por medio de una librería (YACC).


El analizador sintáctico creado por el equipo tiene la capacidad de:
* Analizar los condicionales.
* Analizar las operaciones dentro de los condicionales.
* Analizar los bucles: 
  * For
  * While
  * Do-While


Sin embargo, este analizador NO puede:
* Analizar el contenido del bloque condicional.
* Analizar el contenido del de los bucles.

---
# Gramáticas utilizadas

## Gramática inicial
~~~ 
program ::= SVar program  
program ::= SStruc SInst  
program ::= " 
~~~

## Gramática de instrucciones
~~~
SInst ::= SVar SInst  
SInst ::= SIfElse SInst
SInst ::= SWhile SInst  
SInst ::= DoWhile SInst
SInst ::= SFor SInst  
SInst ::= SRet SInst 
SInst ::= SArr SInst  
SInst ::= SBreak SInst 
SInst ::= "  
~~~

## Operaciones aritméticas y lógicas
~~~
SOpe ::= AOpe ZOpe  
ZOpe ::= SUMAR AOpe ZOpe  
ZOpe ::= RESTAR AOpe ZOpe  
ZOpe ::= COMPARAR_IGUAL AOpe ZOpe  
ZOpe ::= MAYOR_QUE AOpe ZOpe  
ZOpe ::= MENOR_QUE AOpe ZOpe  
ZOpe ::= ''  
AOpe ::= COpe BOpe  
BOpe ::= MULTIPLICAR COpe BOpe  
BOpe ::= DIVIDIR COpe BOpe  
BOpe ::= MODULO COpe BOpe  
BOpe ::= AND_LOGICO_CONDICIONAL COpe BOpe  
BOpe ::= OR_LOGICO_CONDICIONAL COpe BOpe  
BOpe ::= ''  
COpe ::= PAREN_IZQ SOpe PAREN_DER  
COpe ::= EOpe  
COpe ::= NUMERO_DECIMAL  
COpe ::= NUMERO_ENTERO  
DOpe ::= CORCHETE_IZQ NUMERO_ENTERO CORCHETE_DER  
DOpe ::= ''  
EOpe ::= IDENTIFICADOR FOpe  
FOpe ::= DOpe  
FOpe ::= IDENTIFICADOR FOpe  
FOpe ::= PUNTO FOpe  
~~~

## Gramatica de variable y funciones
~~~
SVar::= STipos IDENTIFICADOR FVar  
SVar::= IDENTIFICADOR DVaR  
AVar::= ASIGNAR BVar  
AVar::= COMA IDENTIFICADOR AVar  
AVar::= PUNTO_COMA  
BVar::= SOpe CVar  
BVar::= CARACTER CVar  
BVar::= IDENTIFICADOR SFunc AVar  
CVar::= PUNTO_COMA    
CVar::= COMA BVar  
DVar::= ASIGNAR EVar  
DVar::= PUNTO_COMA  
EVar::= SOpe PUNTO_COMA  
EVar::= CARACTER PUNTO_COMA  
EVar::= IDENTIFICADOR SFunc DVar  
FVar::= AVar  
FVar::= PAREN_IZQ GVar  
GVar::= STipos  HVar  
GVar::= PAREN_DER JVar  
HVar::= IDENTIFICADOR IVar  
HVar::=  IVar  
IVar::= COMA GVar   
IVar::= PAREN_DER JVar   
JVar::= PUNTO_COMA  
JVar::= LLAVE_IZQ SInst LLAVE_DER  
STipos::= TIPO_ENTERO  
STipos::= TIPO_CADENA  
STipos::= TIPO_LARGO  
STipos::= TIPO_VACIO  
STipos::= TIPO_CARACTER  
STipos::= TIPO_FLOTANTE  
STipos::= TIPO_DOUBLE  
SFunc::= PAREN_IZQ AFunc  
SFunc::= "
AFunc::= PAREN_DER  
AFunc::= IDENTIFICADOR BFunc  
BFunc::= COMA IDENTIFICADOR BFunc  
BFunc::= PAREN_DER
~~~

## Gramatica de If-Else
~~~
SIfElse::= CONDICIONAL PAREN_IZQ SOpe PAREN_DER LLAVE_IZQ AIfElse  
AIfElse::= SInst LLAVE_DER BIfElse  
BIfElse::= "  
BIfElse::= CASO_CONTRARIO CIfElse   
CIfElse::= LLAVE_IZQ AIfElse  
CIfElse::= SIfElse  
~~~

## Gramatica de retorno
~~~
SRet::= RETORNAR ARet
ARet::= SOpe PUNTO_COMA
ARet::= CARACTER PUNTO_COMA
~~~
## Gramatica de array
~~~
SArr::= IDENTIFICADOR CORCHETE_IZQ NUMERO_ENTERO CORCHETE_DER ASIGNAR SOpe PUNTO_COMA
SArr::= STipos IDENTIFICADOR CORCHETE_IZQ AArr

AArr::= NUMERO_ENTERO CORCHETE_DER BArr
AArr::= CORCHETE_DER CArr
BArr::= CArr 
BArr::= PUNTO_COMA
CArr::=  ASIGNAR LLAVE_IZQ DArr
DArr::= SOpe EArr
DArr::= CARACTER EArr
EArr::= COMA DArr
EArr::= LLAVE_DER PUNTO_COMA
~~~
## Gramatica de estructura
~~~
SStruct::= ESTRUCTURA AStruct
AStruct::= IDENTIFICADOR LLAVE_IZQ BStruct LLAVE_DER CStruct
AStruct::= LLAVE_IZQ BStruct LLAVE_DER DStruct
BStruct::= "
BStruct::= IDENTIFICADOR FStruct  
CStruct::= PUNTO_COMA  
CStruct::= DStruct
DStruct::= IDENTIFICADOR EStruct
EStruct::= COMA DStruct
EStruct::= PUNTO_COMA
FStruct::= PUNTO_COMA BStruct
FStruct::= CORCHETE_IZQ NUMERO_ENTERO CORCHETE_DER PUNTO_COMA BStruct
~~~



## Gramatica de While, Do-While, For
~~~
SWhile::= BUCLE_MIENTRAS PAREN_IZQ SOpe PAREN_DER LLAVE_IZQ SInst LLAVE_DER  
SDoWhile::= HACER LLAVE_IZQ SInst LLAVE_DER BUCLE_MIENTRAS PAREN_IZQ SOpe PAREN_DER PUNTO_COMA  
SFor::= BUCLE_PARA PAREN_IZQ SDecVarFor PUNTO_COMA SOpe PUNTO_COMA SAsigVarFor PAREN_DER LLAVE_IZQ SInst LLAVE_DER
~~~

## Gramatica de asignar y declarar variable
~~~
SAsigVarFor::= IDENTIFICADOR ASIGNAR SOpe  
SDecVarFor::= STipos IDENTIFICADOR ADecVarFor  
ADecVarFor::= ASIGNAR BDecVarFor
ADecVarFor::= COMA BDecVarFor
BDecVarFor::= SOpe CDecVarFor
CDecVarFor::= COMA BDecVarFor
CDecVarFor::= "
~~~

## Gramática de break
~~~
SBreak::= ROMPER PUNTO_COMA
~~~

