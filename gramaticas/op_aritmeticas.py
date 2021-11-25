def p_op_aritmetica_S(p):
    'SAritm : AAritm ZAritm'

def p_op_aritmetica_Z(p):
    '''ZAritm : SUMAR AAritm ZAritm
    | RESTAR AAritm ZAritm
    | empty
    '''

def p_op_aritmetica_A(p):
    'AAritm : CAritm BAritm'

def p_op_aritmetica_B(p):
    '''BAritm : MULTIPLICAR CAritm BAritm
    | DIVIDIR CAritm BAritm
    | MODULO CAritm BAritm
    | empty
    '''
    
def p_op_aritmetica_C(p):
    '''CAritm : PAREN_IZQ SAritm PAREN_DER
    | IDENTIFICADOR DAritm
    | NUMERO_ENTERO
    | NUMERO_DECIMAL
    '''

def p_op_aritmetica_D(p):
    '''DAritm : CORCHETE_IZQ NUMERO_ENTERO CORCHETE_DER
    | empty
    '''