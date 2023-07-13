import ply.yacc as yacc
from lexico import tokens

_has_errors = False
_last_error = None
_self_test = False

def p_code(p):
    """code : codeLine LEAP code
    | codeLine
    """

def p_basic(p):
    "codeLine : printfunc DOTCOMA"

def p_operationCode(p):
    "codeLine : operation DOTCOMA"

def p_return(p):
    """codeLine : RETURN ID DOTCOMA
    | RETURN value DOTCOMA
    """

def p_printFunction(p):
    """printfunc : PRINT LPAREN ID RPAREN
    | PRINT LPAREN value RPAREN
    """

def p_forBucle(p):
    "codeLine : FOR LPAREN typesVarAsignation conditionProduction DOTCOMA operation RPAREN LCURLY_BRACKET"


def p_operation(p):
    """operation : ID DECREMENT_OPERATOR
    | DECREMENT_OPERATOR ID
    | INCREMENT_OPERATOR ID
    | ID INCREMENT_OPERATOR
    | ID operator ID
    | ID operator numericValue
    | numericValue operator ID
    """

def p_operator(p):
    """operator : PLUS
    | MINUS
    | TIMES
    | DIVIDE
    """


def p_emptySet(p):
    """codeLine : VAR ID EQUALS LESS_THAN OBJTYPE GREATER_THAN LCURLY_BRACKET RCURLY_BRACKET DOTCOMA
    | setTypes LESS_THAN OBJTYPE GREATER_THAN ID EQUALS LCURLY_BRACKET RCURLY_BRACKET DOTCOMA
    """


def p_set(p):
    """codeLine : VAR ID EQUALS LESS_THAN OBJTYPE GREATER_THAN LCURLY_BRACKET values RCURLY_BRACKET DOTCOMA
    | setTypes LESS_THAN OBJTYPE GREATER_THAN ID EQUALS LCURLY_BRACKET values RCURLY_BRACKET DOTCOMA
    """

def p_setTypes(p):
    """setTypes : SETTYPE
    | HASHSETTYPE
    | LINKEDHASHSETTYPE
    | SPLAYTREESETTYPE
    """


def p_emptyList(p):
    """codeLine : LIST OBJTYPE ID EQUALS LSBRACKET RSBRACKET DOTCOMA
    | LIST OBJTYPE ID EQUALS LIST OBJTYPE LPAREN RPAREN DOTCOMA
    | LIST OBJTYPE ID EQUALS LIST LPAREN RPAREN DOTCOMA
    """


def p_list(p):
    "codeLine : LIST OBJTYPE ID EQUALS LSBRACKET values RSBRACKET DOTCOMA"


def p_listMethods(p):
    """codeLine : ID METHOD LPAREN RPAREN DOTCOMA
    | ID METHOD LPAREN values RPAREN DOTCOMA
    | ID METHOD DOTCOMA
    """


def p_ifStatement(p):
    """codeLine : IF LPAREN conditionProduction RPAREN LCURLY_BRACKET RCURLY_BRACKET
    | IF LPAREN conditionProduction RPAREN LCURLY_BRACKET
    | RCURLY_BRACKET
    """


def p_elseStatement(p):
    """codeLine : ELSE LCURLY_BRACKET RCURLY_BRACKET
    | IF LCURLY_BRACKET
    """


def p_ifElseStatement(p):
    """codeLine : ELSE IF LPAREN conditionProduction RPAREN LCURLY_BRACKET RCURLY_BRACKET
    | ELSE IF LPAREN conditionProduction RPAREN LCURLY_BRACKET
    """


def p_NamedParametersfunction(p):
    """codeLine : types ID LPAREN LCURLY_BRACKET typesVarProduction RCURLY_BRACKET RPAREN LCURLY_BRACKET RCURLY_BRACKET
    | types ID LPAREN LCURLY_BRACKET typesVarProduction RCURLY_BRACKET RPAREN LCURLY_BRACKET
    """


def p_condition(p):
    """condition : ID comparator ID
    | value comparator value
    | ID comparator value
    | value comparator ID
    """


def p_conditionProduction(p):
    """conditionProduction : condition
    | condition logicalOperator conditionProduction
    """


def p_values(p):
    """values : value
    | value COMA values
    """


def p_value(p):
    """value : numericValue
    | STR
    | TRUE
    | FALSE
    | ID
    | ID LSBRACKET value RSBRACKET
    """


def p_numericValue(p):
    """numericValue : INT
    | DOUBLE
    """


def p_types(p):
    """types : VAR
    | CONST
    | FINAL
    | VOID
    | STATIC
    | explicit_types
    """


def p_explicit_types(p):
    """explicit_types : INTTYPE
    | DOUBLETYPE
    | STRINGTYPE
    | HASHSETTYPE
    | SETTYPE
    | LINKEDHASHSETTYPE
    | SPLAYTREESETTYPE
    | BOOL
    | record_shape
    """


def p_typesVarProduction(p):
    """typesVarProduction : requiredTypes
    | requiredTypes COMA typesVarProduction
    """


def p_requiredTypes(p):
    """requiredTypes : REQUIRED types ID
    | types ID
    | types CLOSEQUESTIONMARK ID
    | types LSBRACKET CLOSEQUESTIONMARK ID RSBRACKET
    """

    # LSBRACKET

def p_num_self_operation(p):
    """codeLine : pre_decrement DOTCOMA
    | post_decrement DOTCOMA
    | pre_increment DOTCOMA
    | post_increment DOTCOMA
    """

def p_pre_decrement(p):
    """pre_decrement : DECREMENT_OPERATOR ID
    | DECREMENT_OPERATOR symbol_chain
    """

def p_post_decrement(p):
    """ post_decrement : ID DECREMENT_OPERATOR
    | symbol_chain DECREMENT_OPERATOR
    """

def p_pre_increment(p):
    """pre_increment : INCREMENT_OPERATOR ID
    | INCREMENT_OPERATOR symbol_chain
    """

def p_post_increment(p):
    """post_increment : ID INCREMENT_OPERATOR
    | symbol_chain INCREMENT_OPERATOR
    """


def p_typesVarAsignation(p):
    """typesVarAsignation : types ID EQUALS value DOTCOMA
    | doubleTypeAsignation
    """

def p_doubleTypeAsignation(p):
    """doubleTypeAsignation : var_mods DOUBLETYPE ID EQUALS DOUBLE
    | var_mods NUM ID EQUALS DOUBLE
    """

def p_logicalOperator(p):
    """logicalOperator : AND
    | OR
    | NOT_EQUAL
    """


def p_comparator(p):
    """comparator : GREATER_THAN
    | GREATER_THAN_EQUAL
    | LESS_THAN
    | LESS_THAN_EQUAL
    | EQUAL
    """


#############################
###   Variables/Symbols   ###
#############################
def p_declaration(p):
    """codeLine : types ID EQUALS value DOTCOMA
    | explicit_types ID DOTCOMA
    | explicit_types ID EQUALS value DOTCOMA
    | var_mods explicit_types ID DOTCOMA
    | var_mods explicit_types CLOSEQUESTIONMARK ID DOTCOMA
    | LATE explicit_types nullsafe_mod ID DOTCOMA
    """

def p_int_self_operation(p):
    """codeLine : ID DECREMENT_SELF_ASSIGN_OPERATOR int_value_statement DOTCOMA
    | ID INCREMENT_SELF_ASSIGN_OPERATOR int_value_statement DOTCOMA
    """

def p_int_value_statement(p):
    """int_value_statement : numericValue
    | invoke
    | operation
    """


def p_nullsafe_mod(p):
    """nullsafe_mod : empty
    | CLOSEQUESTIONMARK
    """


def p_var_mods(p):
    """var_mods : empty
    | FINAL
    | CONST
    """


## Record syntax definition
def p_record_shape(p):
    """record_shape : LPAREN record_shape_def RPAREN
    | LPAREN LCURLY_BRACKET record_shape_named_def RCURLY_BRACKET RPAREN
    """


def p_record_shape_def(p):
    """record_shape_def : explicit_types
    | explicit_types COMA record_shape_def
    """


def p_record_shape_named_def(p):
    """record_shape_named_def : explicit_types ID
    | explicit_types ID COMA record_shape_named_def
    """


def p_empty(p):
    "empty :"
    pass


def p_record_variable(p):
    """codeLine : VAR ID EQUALS record DOTCOMA
    | CONST ID EQUALS LPAREN record_content RPAREN DOTCOMA
    | FINAL ID EQUALS LPAREN record_content RPAREN DOTCOMA
    | record_shape ID EQUALS record DOTCOMA
    """


def p_record(p):
    """record : LPAREN record_content RPAREN"""


def p_record_content(p):
    """record_content : empty
    | value
    | value COMA record_content
    | types COLON value
    | types COLON value COMA record_content
    """


################################
###   While/do-while loops   ###
################################
def p_while(p):
    """codeLine : WHILE LPAREN evaluable_condition RPAREN LCURLY_BRACKET RCURLY_BRACKET"""


def p_do_while(p):
    """codeLine : DO LCURLY_BRACKET RCURLY_BRACKET WHILE LPAREN evaluable_condition RPAREN DOTCOMA
    | DO LCURLY_BRACKET codeLine RCURLY_BRACKET WHILE LPAREN evaluable_condition RPAREN DOTCOMA
    """


def p_evaluable_condition(p):
    """evaluable_condition : TRUE
    | FALSE
    | conditionProduction
    | invoke
    | NEG evaluable_condition
    | NEG LPAREN evaluable_condition RPAREN
    """


##########################################
###   Function operators/definitions   ###
##########################################
def p_invoke(p):
    """invoke : ID LPAREN values RPAREN
    | ID LPAREN RPAREN
    | ID METHOD LPAREN values RPAREN
    | symbol_chain DOT METHOD LPAREN RPAREN
    | symbol_chain DOT METHOD LPAREN values RPAREN
    """

def p_symbol_chain(p):
    """ symbol_chain : ID DOT ID
        | ID DOT symbol_chain
    """


def p_error(p):
    global _has_errors
    global _last_error
    global _self_test
    _has_errors = True
    _last_error = p
    if p:
        print("Error de sintaxis en token:", p.type)

        # print(f'[DEBUG] info of p: {p}')
        # sintactico.errok()
    else:
        print("Syntax error at EOF")
    if _self_test:
        print(f'The content of p: {p}')


def getError():
    global _has_errors
    global _last_error
    errflag = _has_errors
    error = _last_error if _has_errors else None
    print(f"[dbg] The error was set: {error}, the flag was: {_has_errors}")
    _has_errors = False
    return (errflag, error)



if __name__ == '__main__':
    _self_test = True
    parser = yacc.yacc()
    print("The parser was set with debug logs")
    while True:
        try:
            s = input("dart > ")
        except EOFError:
            break
        if not s:
            continue
        result = parser.parse(s)
        if result != None:
            print(result)
else:
    # Build the parser
    parserSintactico = yacc.yacc()