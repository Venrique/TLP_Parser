class Node:
    def __init__(self,type,contents):
         self.type = type
         self.contents = contents

def p_programA(p):
    'program : SVar program'
    p[0] = Node("programa", [ [p[1]] , [p[2]] ])

def p_programB(p):
    'program : SStruct SInst'
    p[0] = Node("programa", [ [p[1]] , [p[2]] ])

def p_programC(p):
    'program : empty'
    p[0] = Node("programa", ['ε'])

def p_Inst_S(p):
    '''SInst : SVar SInst
    | SIfElse SInst
    | SWhile SInst
    | SDoWhile SInst
    | SFor SInst
    | SRet SInst
    | SArr SInst
    | SBreak SInst
    '''
    p[0] = Node("instruccion", [ [p[1]] , [p[2]] ])

def p_InstEmpty_S(p):
    'SInst : empty'
    p[0] = Node("instrucccion", ['ε'])

def p_ope_S(p):
    'SOpe : AOpe ZOpe'
    p[0] = Node("operacion", [ [p[1]] , [p[2]] ])

def p_ope_Z(p):
    '''ZOpe : SUMAR AOpe ZOpe
    | RESTAR AOpe ZOpe
    | COMPARAR_IGUAL AOpe ZOpe
    | MAYOR_QUE AOpe ZOpe
    | MENOR_QUE AOpe ZOpe
    '''
    p[0] = Node("operacion", [ p[1] , [p[2]] , [p[3]] ])
    
def p_opeEmpty_Z(p):
    'ZOpe : empty'
    p[0] = Node("operacion", [ 'ε' ])

def p_ope_A(p):
    'AOpe : COpe BOpe'
    p[0] = Node("operacion", [ [p[1]] , [p[2]] ])


def p_ope_B(p):
    '''BOpe : MULTIPLICAR COpe BOpe
    | DIVIDIR COpe BOpe
    | MODULO COpe BOpe
    | AND_LOGICO_CONDICIONAL COpe BOpe
    | OR_LOGICO_CONDICIONAL COpe BOpe
    '''
    p[0] = Node("operacion", [ p[1] , [p[2]] , [p[3]] ])

def p_opeEmpty_B(p):
    'BOpe : empty'
    p[0] = Node("operacion", [ 'ε' ])
    
def p_ope_D(p):
    'DOpe : CORCHETE_IZQ NUMERO_ENTERO CORCHETE_DER'
    p[0] = Node("operacion", [ p[1] , p[2] , p[3] ])

def p_opeEmpty_D(p):
    'DOpe : empty'
    p[0] = Node("operacion", [ 'ε' ])

def p_ope_C(p): 
    'COpe : PAREN_IZQ SOpe PAREN_DER'
    p[0] = Node("operacion", [ p[1] , [p[2]] , p[3] ])

def p_ope_C2(p): 
    'COpe : EOpe'
    p[0] = Node("operacion", [ [p[1]] ]) 

def p_ope_C3(p): 
    '''COpe : NUMERO_DECIMAL
    | NUMERO_ENTERO
    '''
    p[0] = Node("operacion", [ p[1] ])

def p_ope_E(p): 
    'EOpe : IDENTIFICADOR FOpe'
    p[0] = Node("operacion", [ p[1], [p[2]] ]) 

def p_ope_F(p): 
    'FOpe : DOpe'
    p[0] = Node("operacion", [ [p[1]] ])

def p_ope_F2(p): 
    '''FOpe : IDENTIFICADOR FOpe
    | PUNTO FOpe
    '''
    p[0] = Node("operacion", [ p[1] , [p[2]] ])

def p_var_S(p):
    'SVar : STipos IDENTIFICADOR FVar'
    p[0] = Node("var-func", [ [p[1]] , p[2] , [p[3]] ])

def p_var_S2(p):
    'SVar : IDENTIFICADOR DVar'
    p[0] = Node("var-func", [ p[1] , [p[2]] ])

def p_var_A(p):
    'AVar : ASIGNAR BVar'
    p[0] = Node("var-func", [ p[1] , [p[2]] ])

def p_var_A2(p):
    'AVar : COMA IDENTIFICADOR AVar'
    p[0] = Node("var-func", [ p[1] , p[2] , [p[3]] ])

def p_var_A3(p):
    'AVar : PUNTO_COMA'
    p[0] = Node("var-func", [ p[1] ])

def p_var_B(p):
    'BVar : SOpe CVar'
    p[0] = Node("var-func", [ [p[1]] , [p[2]] ])
    
def p_var_B2(p):
    'BVar : CARACTER CVar'
    p[0] = Node("var-func", [ p[1] , [p[2]] ])
    
def p_var_B3(p):
    'BVar : IDENTIFICADOR SFunc AVar'
    p[0] = Node("var-func", [ p[1] , [p[2]] , [p[3]] ])

def p_var_C(p):
    'CVar : PUNTO_COMA'
    p[0] = Node("var-func", [ p[1] ])
    
def p_var_C2(p):
    'CVar : COMA BVar'
    p[0] = Node("var-func", [ p[1] , [p[2] ] ])

def p_var_D(p):
    'DVar : ASIGNAR EVar'
    p[0] = Node("var-func", [ p[1] , [p[2]] ])

def p_var_D2(p):
    'DVar : PUNTO_COMA'
    p[0] = Node("var-func", [ p[1] ])

def p_var_E(p):
    'EVar : SOpe PUNTO_COMA'
    p[0] = Node("var-func", [ [p[1]] , p[2] ])

def p_var_E2(p):
    'EVar : CARACTER PUNTO_COMA'
    p[0] = Node("var-func", [ p[1] , p[2] ])

def p_var_E3(p):
    'EVar : IDENTIFICADOR SFunc DVar'
    p[0] = Node("var-func", [ p[1] , [p[2]] , [p[3]] ])

def p_var_F(p):
    'FVar : AVar'
    p[0] = Node("var-func", [ [p[1]] ])

def p_var_F2(p):
    'FVar : PAREN_IZQ GVar'
    p[0] = Node("var-func", [ p[1] , [p[2]] ])

def p_var_G(p):
    'GVar : STipos  HVar'
    p[0] = Node("var-func", [ [p[1]] , [p[2]] ])

def p_var_G2(p):
    'GVar : PAREN_DER JVar'
    p[0] = Node("var-func", [ p[1] , [p[2]] ])
    
def p_var_H(p):
    'HVar : IDENTIFICADOR IVar'
    p[0] = Node("var-func", [ p[1] , [p[2]] ])

def p_var_H2(p):
    'HVar : IVar'
    p[0] = Node("var-func", [ [p[1]] ])

def p_var_I(p):
    '''IVar : COMA GVar
    | PAREN_DER JVar
    '''
    p[0] = Node("var-func", [ p[1] , [p[2]] ])

def p_var_J(p):
    'JVar : PUNTO_COMA'
    p[0] = Node("var-func", [ p[1] ])

def p_var_J2(p):
    'JVar : LLAVE_IZQ SInst LLAVE_DER'
    p[0] = Node("var-func", [ p[1] , [p[2]] , p[3] ])

def p_tipos_S(p):
    '''STipos : TIPO_ENTERO
    | TIPO_CADENA
    | TIPO_LARGO
    | TIPO_VACIO
    | TIPO_CARACTER
    | TIPO_FLOTANTE
    | TIPO_DOUBLE
    '''
    p[0] = Node("var-func", [ p[1] ])

def p_func_S(p):
    'SFunc : PAREN_IZQ AFunc'
    p[0] = Node("var-func", [ p[1] , [p[2]] ])

def p_funcEmpty_S(p):
    'SFunc : empty'
    p[0] = Node("var-func", [ 'ε' ])

def p_func_A(p):
    'AFunc : PAREN_DER'
    p[0] = Node("var-func", [ p[1] ])

def p_func_A2(p):
    'AFunc : IDENTIFICADOR BFunc'
    p[0] = Node("var-func", [ p[1] , [p[2]] ])

def p_func_B(p):
    'BFunc : COMA IDENTIFICADOR BFunc'
    p[0] = Node("var-func", [ p[1] , p[2] , [p[3]] ])

def p_func_B2(p):
    'BFunc : PAREN_DER'
    p[0] = Node("var-func", [ p[1] ])

def p_if_S(p):
    'SIfElse : CONDICIONAL PAREN_IZQ SOpe PAREN_DER LLAVE_IZQ AIfElse'
    p[0] = Node("if-else", [ p[1] , p[2] , [p[3]] , p[4] , p[5] , [p[6]] ])

def p_if_A(p):
    'AIfElse : SInst LLAVE_DER BIfElse'
    p[0] = Node("if-else", [ [p[1]] , p[2] , [p[3]] ])

def p_if_B(p):
    'BIfElse : CASO_CONTRARIO CIfElse'
    p[0] = Node("if-else", [ p[1] , [p[2]] ])

def p_ifEmpty_B(p):
    'BIfElse : empty'
    p[0] = Node("if-else", [ 'ε' ])

def p_if_C(p):
    'CIfElse : LLAVE_IZQ AIfElse'
    p[0] = Node("if-else", [ p[1] , [p[2]] ])

def p_if_C2(p):
    'CIfElse : SIfElse'
    p[0] = Node("if-else", [ [p[1]] ])

def p_ret_S(p):
    'SRet : RETORNAR ARet'
    p[0] = Node("return", [ p[1] , [p[2]] ])

def p_ret_A(p):
    'ARet : SOpe PUNTO_COMA'
    p[0] = Node("return", [ [p[1]] , p[2] ])

def p_ret_A2(p):
    'ARet : CARACTER PUNTO_COMA'
    p[0] = Node("return", [ p[1] , p[2] ])

def p_arr_S(p):
    'SArr : IDENTIFICADOR CORCHETE_IZQ NUMERO_ENTERO CORCHETE_DER ASIGNAR SOpe PUNTO_COMA'
    p[0] = Node("arreglo", [ p[1] , p[2] , p[3] , p[4] , p[5] , [p[6]] , p[7] ])

def p_arr_S2(p):
    'SArr : STipos IDENTIFICADOR CORCHETE_IZQ AArr'
    p[0] = Node("arreglo", [ [p[1]] , p[2] , p[3] , [p[4]] ])

def p_arr_A(p):
    'AArr : NUMERO_ENTERO CORCHETE_DER BArr'
    p[0] = Node("arreglo", [ p[1] , p[2] , [p[3]] ])

def p_arr_A2(p):
    'AArr : CORCHETE_DER CArr'
    p[0] = Node("arreglo", [ p[1] , [p[2]] ])

def p_arr_B(p):
    'BArr : CArr'
    p[0] = Node("arreglo", [ [p[1]] ])

def p_arr_B2(p):
    'BArr : PUNTO_COMA'
    p[0] = Node("arreglo", [ p[1] ])

def p_arr_C(p):
    'CArr : ASIGNAR LLAVE_IZQ DArr'
    p[0] = Node("arreglo", [ p[1] , p[2] , [p[3]] ])
    
def p_arr_D(p):
    'DArr : SOpe EArr'
    p[0] = Node("arreglo", [ [p[1]] , [p[2]] ])

def p_arr_D2(p):
    'DArr : CARACTER EArr'
    p[0] = Node("arreglo", [ p[1] , [p[2]] ])

def p_arr_E(p):
    'EArr : COMA DArr'
    p[0] = Node("arreglo", [ p[1] , [p[2]] ])

def p_arr_E2(p):
    'EArr : LLAVE_DER PUNTO_COMA'
    p[0] = Node("arreglo", [ p[1] , p[2] ])

def p_struct_S(p):
    'SStruct : ESTRUCTURA AStruct'
    p[0] = Node("estructura", [ p[1] , [p[2]] ])
    
def p_struct_A(p):
    'AStruct : IDENTIFICADOR LLAVE_IZQ BStruct LLAVE_DER CStruct'
    p[0] = Node("estructura", [ p[1] , p[2] , [p[3]] , p[4] , [p[5]] ])

def p_struct_A2(p):
    'AStruct : LLAVE_IZQ BStruct LLAVE_DER DStruct'
    p[0] = Node("estructura", [ p[1] , [p[2]] , p[3] , [p[4]] ])

def p_struct_B(p):
    'BStruct : empty'
    p[0] = Node("estructura", [ 'ε' ])

def p_struct_B2(p):
    'BStruct : STipos IDENTIFICADOR FStruct'
    p[0] = Node("estructura", [ [p[1]] , p[2] , [p[3]] ])

def p_struct_C(p):
    'CStruct : PUNTO_COMA'
    p[0] = Node("estructura", [ p[1] ])

def p_struct_C2(p):
    'CStruct : DStruct'
    p[0] = Node("estructura", [ [p[1]] ])

def p_struct_D(p):
    'DStruct : IDENTIFICADOR EStruct'
    p[0] = Node("estructura", [ p[1] , [p[2]] ])

def p_struct_E(p):
    'EStruct : COMA DStruct'
    p[0] = Node("estructura", [ p[1] , [p[2]] ])

def p_struct_E2(p):
    'EStruct : PUNTO_COMA'
    p[0] = Node("estructura", [ p[1] ])
    
def p_struct_F(p):
    'FStruct : PUNTO_COMA BStruct'
    p[0] = Node("estructura", [ p[1] , [p[2]] ])

def p_struct_F2(p):
    'FStruct : CORCHETE_IZQ NUMERO_ENTERO CORCHETE_DER PUNTO_COMA BStruct'
    p[0] = Node("estructura", [ p[1] , p[2] , p[3] , p[4], [p[5]] ])

def p_while_S(p):
    'SWhile : BUCLE_MIENTRAS PAREN_IZQ SOpe PAREN_DER LLAVE_IZQ SInst LLAVE_DER'
    p[0] = Node("while", [ p[1] , p[2] , [p[3]] , p[4] , p[5] , [p[6]] , p[7] ])
    
def p_dowhile_S(p):
    'SDoWhile : HACER LLAVE_IZQ SInst LLAVE_DER BUCLE_MIENTRAS PAREN_IZQ SOpe PAREN_DER PUNTO_COMA'
    p[0] = Node("do-while", [ p[1] , p[2] , [p[3]] , p[4] , p[5] , p[6] , [p[7]] , p[8] , p[9] ])
    
def p_for_S(p):
    'SFor : BUCLE_PARA PAREN_IZQ SDecVarFor PUNTO_COMA SOpe PUNTO_COMA SAsigVarFor PAREN_DER LLAVE_IZQ SInst LLAVE_DER'
    p[0] = Node("for", [ p[1] , p[2] , [p[3]] , p[4] , [p[5]] , p[6] , [p[7]] , p[8] , p[9] , [p[10]] , p[11] ])

def p_asig_var_for_S(p):
    'SAsigVarFor : IDENTIFICADOR ASIGNAR SOpe'
    p[0] = Node("asig-var-for", [ p[1] , p[2] , [p[3]] ])

def p_dec_var_for_S(p):
    'SDecVarFor : STipos IDENTIFICADOR ADecVarFor'
    p[0] = Node("dec-var-for", [ [p[1]] , p[2] , [p[3]] ])

def p_dec_var_for_A(p):
    '''ADecVarFor : ASIGNAR BDecVarFor
    | COMA BDecVarFor
    '''
    p[0] = Node("dec-var-for", [ p[1] , [p[2]] ])

def p_dec_var_for_B(p):
    'BDecVarFor : SOpe CDecVarFor'
    p[0] = Node("dec-var-for", [ [p[1]] , [p[2]] ])

def p_dec_var_for_C(p):
    'CDecVarFor : COMA BDecVarFor'
    p[0] = Node("dec-var-for", [ p[1] , [p[2]] ])

def p_dec_var_forEmpty_C(p):
    'CDecVarFor : empty'
    p[0] = Node("dec-var-for", [ 'ε' ])

def p_break_S(p):
    'SBreak : ROMPER PUNTO_COMA'
    p[0] = Node("break", [ p[1] , p[2] ])