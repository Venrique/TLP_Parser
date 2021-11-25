#----------------------------------
#   Lexer C
#----------------------------------
import re
 
#Expresiones regulares
identificadores = {
    'IDENTIFICADOR': r'[_a-zA-Z][_a-zA-Z0-9]*'
}
claves_identificador = identificadores.keys()

cadenas = {
    'CADENA': r'"(.*?)"'
}

commentarios = {
    'COMENTARIO_LINEA': r'\/\/[\s\S]*?\n',
    'COMENTARIO_MULTILINEA': r'\/\*[\s\S]*?\*\/'
}

operadores = {
    '=': 'ASIGNAR',
    '+': 'SUMAR',
    '-': 'RESTAR',  
    '/': 'DIVIDIR',
    '*': 'MULTIPLICAR',
    '%': 'MODULO',
    '>': 'MAYOR_QUE', 
    '<': 'MENOR_QUE',
    '!': 'NEGACION',
    '&': 'AND_LOGICO',
    '|': 'OR_LOGICO'
}
claves_operadores = operadores.keys()

operadores_comp = {
    '>=': 'MAYOR_IGUAL', 
    '<=': 'MENOR_IGUAL ',
    '++': 'INCREMENTO',
    '--': 'DECREMENTO',
    '==': 'COMPARAR_IGUAL',
    '!=': 'COMPARAR_DIF',
    '&&': 'AND_LOGICO_CONDICIONAL',
    '||': 'OR_LOGICO_CONDICIONAL',
    '+=': 'ASIGNAR_SUMA',
    '-=': 'ASIGNAR_RESTA',
    '*=': 'ASIGNAR_MULT',
    '/=': 'ASIGNAR_DIV',
    '//': 'DIVISION_ENTERA'
}
claves_operadores_comp = operadores_comp.keys()

palabras_reservadas = {
    'static': 'ESTATICO',
    'if': 'CONDICIONAL',
    'for': 'BUCLE_PARA',
    'while': 'BUCLE_MIENTRAS',
    'do': 'HACER',
    'return': 'RETORNAR',
    'else': 'CASO_CONTRARIO',
    'struct': 'ESTRUCTURA'
}
claves_palabras_res = palabras_reservadas.keys()

directivas = {
    '#include': "DIR_INCLUIR",
    '#define': "DIR_DEFINIR",
    '#undef': "DIR_UNDEFINIR"
}
claves_directivas = directivas.keys()

tipos_de_datos = {
    'int': 'TIPO_ENTERO',
    'string': 'TIPO_CADENA',
    'long': 'TIPO_LARGO',
    'void': 'TIPO_VACIO',
    'char': 'TIPO_CARACTER',
    'float': 'TIPO_FLOTANTE',
    'double': 'TIPO_DOUBLE'
}
claves_tipos_de_datos = tipos_de_datos.keys()

puntuacion = {
    '.': 'PUNTO',
    ';': 'PUNTO_COMA',
    '\'': 'COMILLA_SIMPLE',
    ',': 'COMA',
    '(': 'PAREN_IZQ',
    ')': 'PARENT_DER',
    '[': 'CORCHETE_IZQ',
    ']': 'CORCHETE_DER',
    '"': 'COMILLA_DOBLE',
    '{': 'LLAVE_IZQ',
    '}': 'LLAVE_DER'
}
claves_puntuacion = puntuacion.keys()
claves = list(claves_operadores)+list(claves_operadores_comp)+list(claves_palabras_res)+list(claves_puntuacion)+list(claves_tipos_de_datos)

def getTokens(linea):
    #Primer filtro: Separar por espacios
    tokens = linea.split()
    #Segundo filtro: Encontrar tokens sin espacios
    i = 0
    stop = len(tokens)
    while i < stop:
        token = tokens[i]
        if not(token in claves):
            tokenBuffer = ""
            for j in range(0,len(token)):
                char = token[j]
                if char in claves:
                    extra = 0
                    if j < len(token)-1:
                        if token[j+1] == '+' or token[j+1] == '-' or token[j+1] == '/' or token[j+1] == '*' or token[j+1] == '=' or token[j+1] == '|' or token[j+1] == '&':
                            extra = 1
                    if(len(tokenBuffer)>0):
                        tokensMiddle = [tokenBuffer, token[j:]]
                    else:
                        tokensMiddle = [token[0:j+1+extra], token[j+1+extra:]]
                    tokensPrev = tokens[0:i]
                    tokensPost = tokens[i+1:]
                    tokens = tokensPrev+tokensMiddle+tokensPost
                    break
                else:
                    tokenBuffer += char
                    if tokenBuffer in claves :
                        if not(tokenBuffer+token[j+1] in claves) and token[j+1]==' ':
                            limit = j
                            if token[j+1] == '+' or token[j+1] == '-' or token[j+1] == '/' or token[j+1] == '*' or token[j+1] == '=' or token[j+1] == '|' or token[j+1] == '&':
                                limit = j+1
                            tokensMiddle = [token[0:limit+1], token[limit+1:]]
                            tokensPrev = tokens[0:i]
                            tokensPost = tokens[i+1:]
                            tokens = tokensPrev+tokensMiddle+tokensPost
                            break
        i+=1
        stop = len(tokens)

    for i,t in enumerate(tokens):
        if t == '==' and tokens[i+1] == '=':
            tokens[i] = '==='
            del tokens[i+1]
    return tokens

def lex(archivo):
    f = open(archivo, 'r')
    #finalRes = open('./source/Hash Table.txt', 'w')
    #print ("Hash Table de la tokenizacion:\n", file=finalRes)
    #finalRes.close()
    #finalRes = open('./source/Hash Table.txt', 'a')
    lectura = f.read()

    #Se eliminan los comentarios
    lectura = re.sub(commentarios['COMENTARIO_MULTILINEA'], '', lectura)
    lectura = re.sub(commentarios['COMENTARIO_LINEA'], '\n', lectura)

    #Se separa el codigo en lineas
    codigo =  lectura.split('\n')
    lineaIndex = 1

    hashTable = []

    for linea in codigo:
        preTokens = getTokens(linea)

        #Deteccion de cadenas
        stringToken = ""
        stringFlag = False
        tokens = []

        for t in preTokens:
            if t=='"' and not(stringFlag):
                stringFlag = True
                stringToken += "\""
                continue

            if t=='"' and stringFlag:
                stringFlag = False
                stringToken = stringToken[:-1]
                stringToken += "\""
                tokens.append(stringToken)
                stringToken = ""
                continue

            if stringFlag:
                stringToken += t+" "

            if not(stringFlag):
                tokens.append(t)

        tokensText = tokens.copy()

        #Si la linea tiene contenido se utiliza
        if len(tokens) > 0:
            for idx, token in enumerate(tokens):
                flag = False

                if re.match(identificadores['IDENTIFICADOR'], token):
                    tokensText[idx] = {'tipo': 'IDENTIFICADOR', 'token': token}
                    flag = True
                
                if token in claves_operadores:
                    tokensText[idx] = {'tipo': "OPERADOR", 'token': operadores[token]}
                    flag = True

                if token in claves_operadores_comp:
                    tokensText[idx] = {'tipo': "OPERADOR",'token': operadores_comp[token]}
                    flag = True

                if token in claves_palabras_res:
                    tokensText[idx] = {'tipo': "PALABRA_RESERVADA", 'token': palabras_reservadas[token]}
                    flag = True
                
                if token in claves_directivas:
                    tokensText[idx] ={ 'tipo':"DIRECTIVA", 'token': directivas[token]}
                    flag = True

                if token in claves_puntuacion:
                    tokensText[idx] = {'tipo': "PUNTUACION", 'token': puntuacion[token]}
                    flag = True

                if token in claves_tipos_de_datos:
                    tokensText[idx] = {'tipo': "TIPO_DE_DATO", 'token': tipos_de_datos[token]}
                    flag = True
                
                if re.match(cadenas['CADENA'], token):
                    tokensText[idx] ={'tipo': "CADENA",'token': token.replace("\"", "")}
                    flag = True
                
                if token.isnumeric():
                    tokensText[idx] = {'tipo': "NUMERO", 'token': token}
                    flag = True

                if not(flag):
                    tokensText[idx] = {'tipo': "ERROR", 'token': token}
                
            lineaIndex += 1
            hashTable.extend(tokensText)

    #print("[", file=finalRes)
    #for i,row in enumerate(hashTable):
    #    end = ""
    #    if i < len(hashTable)-1:
    #        end = ","
    #    print("\t"+str(hashTable[i])+end, file=finalRes)
    #print("]", file=finalRes)
    #finalRes.close()
    return hashTable
