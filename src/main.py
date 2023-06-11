import ply.lex as lex

#Crear los tokens para la siguiente sintaxis

#Diccionario de palabras reservadas
reserved = {
}

 #Sequencia de tokens, puede ser lista o tupla
tokens = (
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'ID',

) + tuple(reserved.values())

 #Exp Regulares para tokens de símbolos
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'

 #Para contabilizar nro de líneas
def t_newline(t):
  r'\n+'
  t.lexer.lineno += len(t.value)

def t_ID(t):
  r'[a-zA-Z_]+'
  t.type = reserved.get(t.value,'ID')
  return t

 # Ignorar lo que no sea un token en mi LP
t_ignore  = ' \t'

 #Presentación de errores léxicos
def t_error(t):
  print("Componente léxico no reconocido '%s'" % t.value[0])
  t.lexer.skip(1)

 #Contruir analizador
lexer = lex.lex()

#Testeando
data = '''

    '''

 #Datos de entrada
lexer.input(data)

 # Tokenizador
while True:
  tok = lexer.token()
  if not tok:
    break
  print(tok)

