def p_program(p):
    '''program : SVar program
    | SStruct SInst
    | empty
    '''

def p_Inst_S(p):
    '''SInst : SVar SInst
    | SIfElse SInst
    | SWhile SInst
    | SDoWhile SInst
    | SFor SInst
    | SRet SInst
    | SArr SInst
    | SBreak SInst
    | empty
    '''

def p_ope_S(p):
    'SOpe : AOpe ZOpe'

def p_ope_Z(p):
    '''ZOpe : SUMAR AOpe ZOpe
    | RESTAR AOpe ZOpe
    | COMPARAR_IGUAL AOpe ZOpe
    | MAYOR_QUE AOpe ZOpe
    | MENOR_QUE AOpe ZOpe
    | empty
    '''

def p_ope_A(p):
    'AOpe : COpe BOpe'


def p_ope_B(p):
    '''BOpe : MULTIPLICAR COpe BOpe
    | DIVIDIR COpe BOpe
    | MODULO COpe BOpe
    | AND_LOGICO_CONDICIONAL COpe BOpe
    | OR_LOGICO_CONDICIONAL COpe BOpe
    | empty
    '''
    
def p_ope_D(p):
    '''DOpe : CORCHETE_IZQ NUMERO_ENTERO CORCHETE_DER
    | empty
    '''

def p_ope_C(p): 
    '''COpe : PAREN_IZQ SOpe PAREN_DER
    | EOpe
    | NUMERO_DECIMAL
    | NUMERO_ENTERO
    '''

def p_ope_E(p): 
    'EOpe : IDENTIFICADOR FOpe'

def p_ope_F(p): 
    '''FOpe : DOpe
    | IDENTIFICADOR FOpe
    | PUNTO FOpe
    '''

def p_var_S(p):
    '''SVar : STipos IDENTIFICADOR FVar
    | IDENTIFICADOR DVar
    '''

def p_var_A(p):
    '''AVar : ASIGNAR BVar
    | COMA IDENTIFICADOR AVar
    | PUNTO_COMA
    '''

def p_var_B(p):
    '''BVar : SOpe CVar
    | CARACTER CVar
    | IDENTIFICADOR SFunc AVar
    '''

def p_var_C(p):
    '''CVar : PUNTO_COMA
    | COMA BVar
    '''

def p_var_D(p):
    ''' DVar : ASIGNAR EVar
    | PUNTO_COMA
    '''

def p_var_E(p):
    '''EVar : SOpe PUNTO_COMA
    | CARACTER PUNTO_COMA
    | IDENTIFICADOR SFunc DVar
    '''

def p_var_F(p):
    '''FVar : AVar
    | PAREN_IZQ GVar
    '''

def p_var_G(p):
    '''GVar : STipos  HVar
    | PAREN_DER JVar
    '''
    
def p_var_H(p):
    '''HVar : IDENTIFICADOR IVar
    | IVar
    '''

def p_var_I(p):
    '''IVar : COMA GVar
    | PAREN_DER JVar
    '''

def p_var_J(p): #Agregar Instrucciones
    '''JVar : PUNTO_COMA
    | LLAVE_IZQ SInst LLAVE_DER
    '''

def p_tipos_S(p):
    '''STipos : TIPO_ENTERO
    | TIPO_CADENA
    | TIPO_LARGO
    | TIPO_VACIO
    | TIPO_CARACTER
    | TIPO_FLOTANTE
    | TIPO_DOUBLE
    '''

def p_func_S(p):
    '''SFunc : PAREN_IZQ AFunc
    | empty
    '''

def p_func_A(p):
    '''AFunc : PAREN_DER
    | IDENTIFICADOR BFunc
    '''

def p_func_B(p):
    '''BFunc : COMA IDENTIFICADOR BFunc
    | PAREN_DER
    '''

def p_if_S(p):
    'SIfElse : CONDICIONAL PAREN_IZQ SOpe PAREN_DER LLAVE_IZQ AIfElse'

def p_if_A(p):
    'AIfElse : SInst LLAVE_DER BIfElse'

def p_if_B(p):
    '''BIfElse : empty
    | CASO_CONTRARIO CIfElse
    '''

def p_if_C(p):
    '''CIfElse : LLAVE_IZQ AIfElse
    | SIfElse
    '''

def p_ret_S(p):
    'SRet : RETORNAR ARet'

def p_ret_A(p):
    '''ARet : SOpe PUNTO_COMA
    | CARACTER PUNTO_COMA
    '''

def p_arr_S(p):
    '''SArr : IDENTIFICADOR CORCHETE_IZQ NUMERO_ENTERO CORCHETE_DER ASIGNAR SOpe PUNTO_COMA
    | STipos IDENTIFICADOR CORCHETE_IZQ AArr
    '''
def p_arr_A(p):
    '''AArr : NUMERO_ENTERO CORCHETE_DER BArr
    | CORCHETE_DER CArr
    '''
def p_arr_B(p):
    '''BArr : CArr 
    | PUNTO_COMA
    '''
def p_arr_C(p):
    'CArr : ASIGNAR LLAVE_IZQ DArr'
    
def p_arr_D(p):
    '''DArr : SOpe EArr
    | CARACTER EArr
    '''
def p_arr_E(p):
    '''EArr : COMA DArr
    | LLAVE_DER PUNTO_COMA
    '''
def p_struct_S(p):
    'SStruct : ESTRUCTURA AStruct'
    
def p_struct_A(p):
    '''AStruct : IDENTIFICADOR LLAVE_IZQ BStruct LLAVE_DER CStruct
    | LLAVE_IZQ BStruct LLAVE_DER DStruct
    '''
def p_struct_B(p):
    '''BStruct : empty
    | STipos IDENTIFICADOR FStruct
    '''
def p_struct_C(p):
    '''CStruct : PUNTO_COMA
    | DStruct
    '''
def p_struct_D(p):
    'DStruct : IDENTIFICADOR EStruct'

def p_struct_E(p):
    '''EStruct : COMA DStruct
    | PUNTO_COMA
    '''
def p_struct_F(p):
    '''FStruct : PUNTO_COMA BStruct
    | CORCHETE_IZQ NUMERO_ENTERO CORCHETE_DER PUNTO_COMA BStruct
    '''
def p_while_S(p):
    'SWhile : BUCLE_MIENTRAS PAREN_IZQ SOpe PAREN_DER LLAVE_IZQ SInst LLAVE_DER'
    
def p_dowhile_S(p):
    'SDoWhile : HACER LLAVE_IZQ SInst LLAVE_DER BUCLE_MIENTRAS PAREN_IZQ SOpe PAREN_DER PUNTO_COMA'
    
def p_for_S(p):
    'SFor : BUCLE_PARA PAREN_IZQ SDecVarFor PUNTO_COMA SOpe PUNTO_COMA SAsigVarFor PAREN_DER LLAVE_IZQ SInst LLAVE_DER'

def p_asig_var_for_S(p):
    'SAsigVarFor : IDENTIFICADOR ASIGNAR SOpe'


def p_dec_var_for_S(p):
    'SDecVarFor : STipos IDENTIFICADOR ADecVarFor'

def p_dec_var_for_A(p):
    '''ADecVarFor : ASIGNAR BDecVarFor
    | COMA BDecVarFor
    '''

def p_dec_var_for_B(p):
    'BDecVarFor : SOpe CDecVarFor'

def p_dec_var_for_C(p):
    '''CDecVarFor : COMA BDecVarFor
    | empty
    '''

def p_break_S(p):
    'SBreak : ROMPER PUNTO_COMA'