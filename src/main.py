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
