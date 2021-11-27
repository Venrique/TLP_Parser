empty = ['vacia']

#Gramática operaciones aritméticas
SAritm=0
ZAritm=1
AAritm=2
BAritm=3
CAritm=4
DAritm=5
#Gramática operaciones lógicas
SLog=6
ZLog=7
ALog=8
BLog=9
CLog=10
DLog=11
#Gramática operaciones lógicas
SDatos=12

#Gramática declaración funciones
SDecFunc = 13
ADecFunc = 14
BDecFunc = 15

#
tablaAritm = [
    #SArtim

    [SAritm, 'PAREN_IZQ', [AAritm,ZAritm]],
   
    [SAritm, 'IDENTIFICADOR', [AAritm,ZAritm]],
    [SAritm, 'NUMERO_DECIMAL', [AAritm,ZAritm]],
    [SAritm, 'NUMERO_ENTERO', [AAritm,ZAritm]],

    #ZAritm
    [ZAritm, 'eof', empty ],
    [ZAritm, 'SUMAR', ['SUMAR',AAritm,ZAritm]],
    [ZAritm, 'RESTAR', ['RESTAR',AAritm,ZAritm] ],

    [ZAritm, 'PAREN_DER', empty ],
 
    #AAritm

    [AAritm, 'PAREN_IZQ', [CAritm,BAritm]],
   
    [AAritm, 'IDENTIFICADOR', [CAritm,BAritm]],
    [AAritm, 'NUMERO_DECIMAL', [CAritm,BAritm]],
    [AAritm, 'NUMERO_ENTERO', [CAritm,BAritm]],
   
    #BAritm
    [BAritm, 'eof', empty ],
    [BAritm, 'SUMAR', empty],
    [BAritm, 'RESTAR', empty ],
    [BAritm, 'MULTIPLICAR', ['MULTIPLICAR',CAritm,BAritm] ],
    [BAritm, 'DIVIDIR', ['DIVIDIR',CAritm,BAritm] ],
    [BAritm, 'MODULO', ['MODULO',CAritm,BAritm] ],
    
    [BAritm, 'PAREN_DER', empty ],

    #CAritm
    [CAritm, 'PAREN_IZQ', ['PAREN_IZQ',SAritm,'PAREN_DER']],
    [CAritm, 'IDENTIFICADOR', ['IDENTIFICADOR',DAritm]],
    [CAritm, 'NUMERO_DECIMAL', ['NUMERO_DECIMAL']],
    [CAritm, 'NUMERO_ENTERO', ['NUMERO_ENTERO']],

    #DAritm
    [DAritm, 'eof', empty ],
    [DAritm, 'SUMAR', empty],
    [DAritm, 'RESTAR', empty ],
    [DAritm, 'MULTIPLICAR', empty ],
    [DAritm, 'DIVIDIR', empty ],
    [DAritm, 'MODULO', empty ], 
    [DAritm, 'PAREN_DER', empty ],
    [DAritm, 'CORCHETE_IZQ', ['CORCHETE_IZQ', 'NUMERO_ENTERO', 'CORCHETE_DER']],
]

tablaLogica = [
    #SLog
    [SLog, 'eof', ],
    [SLog, 'COMPARAR_IGUAL', ],
    [SLog, 'MAYOR_QUE', ],
    [SLog, 'MENOR_QUE', ],
    [SLog, 'AND_LOGICO_CONDICIONAL', ], 
    [SLog, 'OR_LOGICO_CONDICIONAL', ],
    [SLog, 'PAREN_IZQ', ],
    [SLog, 'PAREN_DER', ],
    [SLog, '', ],
    [SLog, '', ]
]

tablaTipos = [
    [SDatos,'TIPO_ENTERO',['TIPO_ENTERO']],
    [SDatos,'TIPO_CADENA',['TIPO_CADENA']],
    [SDatos,'TIPO_LARGO',['TIPO_LARGO']],
    [SDatos,'TIPO_VACIO',['TIPO_VACIO']],
    [SDatos,'TIPO_CARACTER',['TIPO_CARACTER']],
    [SDatos,'TIPO_FLOTANTE',['TIPO_FLOTANTE']],
    [SDatos,'TIPO_DOUBLE',['TIPO_DOUBLE']],
]

tablaDecFunc = [
    #SDecFunc
]
tabla = tablaAritm