import ply.yacc as yacc
from lexico import tokens

def p_emptyList(p):
  '''codeLine : LIST OBJTYPE ID EQUALS LSBRACKET RSBRACKET DOTCOMA
  | LIST OBJTYPE ID EQUALS LIST OBJTYPE LPAREN RPAREN DOTCOMA
  | LIST OBJTYPE ID EQUALS LIST LPAREN RPAREN DOTCOMA
  '''

def p_list(p):
  'codeLine : LIST OBJTYPE ID EQUALS LSBRACKET values RSBRACKET DOTCOMA'

def p_ifStatement(p):
  '''codeLine : IF LPAREN conditionProduction RPAREN LCURLY_BRACKET RCURLY_BRACKET
  | IF LPAREN conditionProduction RPAREN LCURLY_BRACKET
  | RCURLY_BRACKET
  '''

def p_elseStatement(p):
  '''codeLine : ELSE LCURLY_BRACKET RCURLY_BRACKET
  | IF LCURLY_BRACKET
  '''

def p_ifElseStatement(p):
  '''codeLine : ELSE IF LPAREN conditionProduction RPAREN LCURLY_BRACKET RCURLY_BRACKET
  | ELSE IF LPAREN conditionProduction RPAREN LCURLY_BRACKET
  '''

def p_NamedParametersfunction(p):
  '''codeLine : types ID LPAREN LCURLY_BRACKET typesVarProduction RCURLY_BRACKET RPAREN LCURLY_BRACKET RCURLY_BRACKET
  | types ID LPAREN LCURLY_BRACKET typesVarProduction RCURLY_BRACKET RPAREN LCURLY_BRACKET
  '''

def p_condition(p):
  'condition : ID comparator ID'

def p_conditionProduction(p):
  '''conditionProduction : condition
  | condition logicalOperator conditionProduction
  '''

def p_values(p):
  '''values : value
  | value COMA values
  '''

def p_value(p):
  '''value : INT
  | STR
  | DOUBLE
  | TRUE
  | FALSE
  '''

def p_types(p):
  '''types : VAR
  | CONST
  | FINAL
  | VOID
  | STATIC
  | BOOL
  '''

def p_explicit_types(p):
  ''' explicit_types : INTTYPE
      | DOUBLETYPE
      | STRINGTYPE
      | HASHSETTYPE
      | SETTYPE
      | LINKEDHASHSETTYPE
      | SPLAYTREESETTYPE
      | BOOL
      | record_shape
  '''

def p_typesVarProduction(p):
  '''typesVarProduction : types ID
  | types ID COMA typesVarProduction
  '''

def p_logicalOperator(p):
  '''logicalOperator : AND
  | OR
  '''

def p_comparator(p):
  '''comparator : GREATER_THAN
  | GREATER_THAN_EQUAL
  | LESS_THAN
  | LESS_THAN_EQUAL
  | EQUAL
  '''

def p_record_shape(p):
  '''record_shape : LPAREN record_shape_def RPAREN
    | LPAREN LCURLY_BRACKET record_shape_named_def RCURLY_BRACKET RPAREN
  '''

def p_record_shape_def(p):
  ''' record_shape_def : explicit_types
      | explicit_types COMA record_shape_def
  '''
def p_record_shape_named_def(p):
  ''' record_shape_named_def : explicit_types ID
      | explicit_types ID COMA record_shape_named_def
  '''

def p_empty(p):
  'empty :'
  pass

def p_record_variable(p):
  ''' codeLine : VAR ID EQUALS record DOTCOMA
      | CONST ID EQUALS LPAREN record_content RPAREN DOTCOMA
      | FINAL ID EQUALS LPAREN record_content RPAREN DOTCOMA
      | record_shape ID EQUALS record DOTCOMA
  '''
def p_record(p):
  ''' record : LPAREN record_content RPAREN'''

def p_record_content(p):
  ''' record_content : empty
      | value
      | value COMA record_content
      | types COLON value
      | types COLON value COMA record_content
  '''

def p_error(p):
    if p:
         print("Error de sintaxis en token:", p.type)
         #sintactico.errok()
    else:
         print("Syntax error at EOF")

# Build the parser
sintactico = yacc.yacc()

while True:
   try:
       s = input('dart > ')
   except EOFError:
       break
   if not s: continue
   result = sintactico.parse(s)
   if result!=None: print(result)
