import ply.lex as lex

#Crear los tokens para la siguiente sintaxis

#Diccionario de palabras reservadas
reserved = {
  'while': 'WHILE',
  'if': 'IF',
  'true': 'TRUE',
  'false': 'FALSE',
  'bool': 'BOOL',
  'for': 'FOR',
  'return': 'RETURN',
  'print': 'PRINT',
  'int': 'INTTYPE',
  'var': 'VAR',
  'const': 'CONST',
  'final': 'FINAL',
  'List': 'LIST',
}

 #Sequencia de tokens, puede ser lista o tupla
tokens = (
    'INT',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'LSBRACKET',
    'RSBRACKET',
    'LCURLY_BRACKET',
    'RCURLY_BRACKET',
    'ID',
    'EQUALS',
    'DOTCOMA',
    'COMA',
    'OBJTYPE',
    'STR',
    'DECREMENT_OPERATOR',
    'INCREMENT_OPERATOR',
    'INCREMENT_SELF_ASSIGN_OPERATOR',
    'DECREMENT_SELF_ASSIGN_OPERATOR',
    'METHOD',
    'GREATER_THAN',
    'GREATER_THAN_EQUAL',
    'LESS_THAN',
    'LESS_THAN_EQUAL',
    'EQUAL',
    'NOT_EQUAL',
    'AND',

) + tuple(reserved.values())

 #Exp Regulares para tokens de símbolos
t_DECREMENT_OPERATOR = r'--'
t_INCREMENT_OPERATOR = r'\+\+'
t_INCREMENT_SELF_ASSIGN_OPERATOR = r'\+='
t_DECREMENT_SELF_ASSIGN_OPERATOR = r'\-='
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_LSBRACKET  = r'\['
t_RSBRACKET  = r'\]'
t_LCURLY_BRACKET = r'\{'
t_RCURLY_BRACKET = r'\}'
t_DOTCOMA = r';'
t_COMA = r','
t_EQUALS = r'='
t_INT = r'-?\d+'
t_OBJTYPE = r'<[\w]+>'
t_STR = r'''("[^"]*"|'[^']*')'''
t_METHOD = r'\.[\w]*'
t_GREATER_THAN = r'>'
t_GREATER_THAN_EQUAL = r'<='
t_LESS_THAN = r'<'
t_LESS_THAN_EQUAL = r'<='
t_EQUAL = r'=='
t_NOT_EQUAL = r'!='
t_AND = r'&&'

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

def t_COMMENTS(t):
  r'//.*'
  pass

 #Presentación de errores léxicos
def t_error(t):
  print("Componente léxico no reconocido '%s'" % t.value[0])
  t.lexer.skip(1)

 #Contruir analizador
lexer = lex.lex()

#Testeando
data_List_jairo = '''
  List<int> numeros = [];
  List<String> nombres = List<String>();
  List<double> decimales = List();
  List<String> numeros = ["Hola", "Mundo", "!"];
  List<int> numeros = [1, 2, 3];

  var list = List.filled(3, 0);
  print(list); // [0, 0, 0]
  list[1] = 3;
  print(list); // [0, 3, 0]
'''

data_int_jairo = '''
  --numero;
  ++numero;
  int numero = 1 - 2;
  int numero = 1 + 2;
  const numero = 123;
  var numero = 12;
  var numero -= 1;
  var numero += 2;
'''
data_test_jairo = '''
if (array.isEmpty) {
    return false;
  }

  if (sequence.isEmpty) {
    return true;
  }
  int arrayIndex = 0;
  int sequenceIndex = 0;

  while (sequenceIndex < sequence.length && arrayIndex < array.length) {
    if (sequence[sequenceIndex] == array[arrayIndex]) {
      sequenceIndex += 1;
    }
    arrayIndex += 1;
  }
  return sequenceIndex == sequence.length;
'''

 #Datos de entrada
lexer.input(data_test_jairo)

 # Tokenizador
while True:
  tok = lexer.token()
  if not tok:
    break
  print(tok)

