import ply.lex as lex

# Crear los tokens para la siguiente sintaxis

# Diccionario de palabras reservadas
reserved = {
    "while": "WHILE",
    "do": "DO",
    "if": "IF",
    "else": "ELSE",
    "true": "TRUE",
    "false": "FALSE",
    "bool": "BOOL",
    "for": "FOR",
    "return": "RETURN",
    "print": "PRINT",
    "int": "INTTYPE",
    "var": "VAR",
    "const": "CONST",
    "final": "FINAL",
    "late": "LATE",
    "void": "VOID",
    "static": "STATIC",
    "List": "LIST",
    "num": "NUM",
    "double": "DOUBLETYPE",
    "String": "STRINGTYPE",
    'HashSet': "HASHSETTYPE",
    'Set': "SETTYPE",
    'LinkedHashSet': "LINKEDHASHSETTYPE",
    'SplayTreeSet': "SPLAYTREESETTYPE",
    'required': "REQUIRED"
}

# Sequencia de tokens, puede ser lista o tupla
tokens = (
    "LEAP",
    "INT",
    "PLUS",
    "MINUS",
    "TIMES",
    "DIVIDE",
    "LPAREN",
    "RPAREN",
    "LSBRACKET",
    "RSBRACKET",
    "LCURLY_BRACKET",
    "RCURLY_BRACKET",
    "ID",
    "EQUALS",
    "DOTCOMA",
    "DOT",
    "COMA",
    "STR",
    "DECREMENT_OPERATOR",
    "INCREMENT_OPERATOR",
    "INCREMENT_SELF_ASSIGN_OPERATOR",
    "DECREMENT_SELF_ASSIGN_OPERATOR",
    "METHOD",
    "GREATER_THAN",
    "GREATER_THAN_EQUAL",
    "LESS_THAN",
    "LESS_THAN_EQUAL",
    "EQUAL",
    "NOT_EQUAL",
    "AND",
    "OR",
    "COLON",
    "RECORD_ARG",
    "DOUBLE",
    "NEG",
    "CLOSEQUESTIONMARK",
    "COMMENTS"
) + tuple(reserved.values())

# Exp Regulares para tokens de símbolos
t_LEAP = r"\n+"
t_DECREMENT_OPERATOR = r"--"
t_INCREMENT_OPERATOR = r"\+\+"
t_INCREMENT_SELF_ASSIGN_OPERATOR = r"\+="
t_DECREMENT_SELF_ASSIGN_OPERATOR = r"-="
t_PLUS = r"\+"
t_MINUS = r"-"
t_TIMES = r"\*"
t_DIVIDE = r"/"
t_LPAREN = r"\("
t_RPAREN = r"\)"
t_LSBRACKET = r"\["
t_RSBRACKET = r"\]"
t_LCURLY_BRACKET = r"\{"
t_RCURLY_BRACKET = r"\}"
t_DOTCOMA = r"\;"
t_DOT = r"\."
t_COMA = r","
t_EQUALS = r"="
t_INT = r"-?\d+"
t_STR = r"""(\"(?:[^\"\\]|\\.)*\")|(\'(?:[^\'\\]|\\.)*\')"""
t_METHOD = r"\.[a-zA-Z0-9_-][a-zA-Z0-9_-]*"
t_GREATER_THAN = r">"
t_GREATER_THAN_EQUAL = r">="
t_LESS_THAN = r"<"
t_LESS_THAN_EQUAL = r"<="
t_EQUAL = r"=="
t_NOT_EQUAL = r"!="
t_AND = r"&&"
t_OR = r"\|\|"
t_COLON = r":"
t_RECORD_ARG = r"\$\d+"
t_DOUBLE = r'-?((\d*\.\d+)|(\d+(\.))|(\d+(\.)\d+e(\d{3})))'
t_NEG = r'!'
t_CLOSEQUESTIONMARK = r'\?'

# Para contabilizar nro de líneas
def t_newline(t):
    r"\n+"
    t.lexer.lineno += len(t.value)
    t.type = reserved.get(t.value, "LEAP")
    return t


def t_ID(t):
    r"[a-zA-Z_]+"
    t.type = reserved.get(t.value, "ID")
    return t


# Ignorar lo que no sea un token en mi LP
t_ignore = " \t"


def t_COMMENTS(t):
    r'(\/\/.*)|(\/\*.*\*\/)|(\/\*\*.*\*\/)'
    t.type = reserved.get(t.value, "COMMENTS")
    return t


# Presentación de errores léxicos
def t_error(t):
    print("Componente léxico no reconocido '%s'" % t.value[0])
    t.lexer.skip(1)


# Contruir analizador
lexer = lex.lex()

# Testeando
data_List_jairo = """
  List<int> numeros = [];
List<String> nombres = List<String>();
List<double> decimales = List();
List<String> numeros = ["Hola", "Mundo", "!"];
List<int> numeros = [1, 2, 3];

  var list = List.filled(3, 0);
  print(list); // [0, 0, 0]
  list[1] = 3;
  print(list); // [0, 3, 0]
"""

data_int_jairo = """
  --numero;
  ++numero;
  int numero = 1 - 2;
  int numero = 1 + 2;
  const numero = 123;
  var numero = 12;
  var numero -= 1;
  var numero += 2;
"""
data_test_jairo = """
if (numero > numerob) {
    return false;
  }

  if (numero > numerob) {
    return true;
  }
  int arrayIndex = 0;
  int sequenceIndex = 0;

  while (sequenceIndex < sequence && arrayIndex < array) {
    if (sequence[sequenceIndex] == array[arrayIndex]) {
      sequenceIndex += 1;
    }
    arrayIndex += 1;
  }
  return sequenceIndex == sequence.length;
"""

data_record_luis = """
  var record = ('first', a: 2, b: true, 'last')
  var record_alt = ({ a: 1, b: 'hola', c: (1, 2) })
  var first = record.$1
  var named = record.a
  var xd = record.$3244
  print(record) // ('first', a: 2, b: true, 'last')
"""

data_string_luis = """
  var str = 'sfsdfsdf'
  String str = "Hola mundo"
  String complex = "This is 'hello' from your \\"world\\""
"""
data_double_jose = """
  var numero = -2.653;
  for( var i = 5. ; i >= 0.; i-- ) {
      numero += i*.75 ;
   }
"""

data_set_jose = """
  var doubles_set = {-563.3, 230.3, .3, -165165., -166.};
  var doubles_set_empty = <double>{};
  var doubles_set_empty = Set<double>{};
  var doubles_set_empty = HashSet<double>{};
  var doubles_set_empty = LinkedHashSet<double>{};
  var doubles_set_empty = SplayTreeSet<double>{};
  // var names = {}; // Creates a map, not a set.
"""

data_test_jose = """
  var valores = {-563.3, 230.3, .3, 1655., -166.};
  num total = 0;
  for(var i = 0. ; i <= valores.lenght; i++ ) {
      total += i ;
  }
  print(total);
"""
# Datos de entrada
# lexer.input(data_test_jairo)

# lexer.input(data_record_luis)
# lexer.input(data_string_luis)

# lexer.input(data_double_jose)
# lexer.input(data_set_jose)

lexer.input("print(adfa);\nprint(adfa);")
# Tokenizador
while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)
