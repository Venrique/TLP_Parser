def p_op_logica_S(p):
    'SLog : ALog ZLog'

def p_op_logica_Z(p):
    '''ZLog : COMPARAR_IGUAL ALog ZLog
    | MAYOR_QUE ALog ZLog
    | MENOR_QUE ALog ZLog
    | empty
    '''

def p_op_logica_A(p):
    'ALog : CLog BLog'    

def p_op_logica_B(p):
    '''BLog : AND_LOGICO_CONDICIONAL CLog BLog
    | OR_LOGICO_CONDICIONAL CLog BLog
    | empty
    '''

def p_op_logica_C(p):
    '''CLog : PAREN_IZQ SLog PAREN_DER
    | IDENTIFICADOR DLog
    | NUMERO_DECIMAL
    | NUMERO_ENTERO
    | CADENA
    | SAritm
    '''

def p_op_logica_D(p):
    '''DLog : CORCHETE_IZQ NUMERO_ENTERO CORCHETE_DER
    | empty
    '''