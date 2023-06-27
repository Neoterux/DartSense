import ply.yacc as yacc
from lexico import tokens

def p_forBucle(p):
  ''' codeLine : FOR LPAREN typesVarAsignation conditionProduction DOTCOMA operation RPAREN LCURLY_BRACKET codeLine RCURLY_BRACKET
  '''

def p_operation(p):
  ''' operation : ID DECREMENT_OPERATOR
  | DECREMENT_OPERATOR ID
  | INCREMENT_OPERATOR ID
  | ID INCREMENT_OPERATOR
  | ID operator ID
  | ID operator numericValue
  | numericValue operator ID
  '''
  
def p_operator(p):
  ''' operator : PLUS
  | MINUS
  | TIMES
  | DIVIDE
  '''

def p_emptySet(p):
  '''codeLine : VAR ID EQUALS LESS_THAN OBJTYPE GREATER_THAN LCURLY_BRACKET RCURLY_BRACKET DOTCOMA
  | setTypes LESS_THAN OBJTYPE GREATER_THAN ID EQUALS LCURLY_BRACKET RCURLY_BRACKET DOTCOMA
  '''

def p_set(p):
  '''codeLine : VAR ID EQUALS LESS_THAN OBJTYPE GREATER_THAN LCURLY_BRACKET values RCURLY_BRACKET DOTCOMA
  | setTypes LESS_THAN OBJTYPE GREATER_THAN ID EQUALS LCURLY_BRACKET values RCURLY_BRACKET DOTCOMA
  '''

def p_setTypes(p):
  '''setTypes : SETTYPE
  | HASHSETTYPE
  | LINKEDHASHSETTYPE
  | SPLAYTREESETTYPE
  '''

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
  '''value : numericValue
  | STR
  | TRUE
  | FALSE
  '''

def p_numericValue(p):
  '''numericValue : INT
  | DOUBLE
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
  '''typesVarProduction : requiredTypes
  | requiredTypes COMA typesVarProduction
  '''
def p_requiredTypes(p):
  ''' requiredTypes : REQUIRED types ID
  | types ID
  | types CLOSEQUESTIONMARK ID
  | types LSBRACKET CLOSEQUESTIONMARK ID RSBRACKET
  '''
  
  #LSBRACKET
  
def p_typesVarAsignation(p):
  '''typesVarAsignation : types ID EQUALS value DOTCOMA
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
       s = input('''dart > ''')
   except EOFError:
       break
   if not s: continue
   result = sintactico.parse(s)
   if result!=None: print(result)
