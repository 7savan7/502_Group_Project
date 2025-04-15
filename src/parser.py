import ply.yacc as yacc
from lexer import tokens

parse_tree = []

def p_program(p):
    '''program : statement_list'''
    p[0] = ('program', p[1])
    global parse_tree
    parse_tree = p[0]

def p_statement_list(p):
    '''statement_list : statement_list statement
                      | statement'''
    if len(p) == 3:
        p[0] = p[1] + [p[2]]
    else:
        p[0] = [p[1]]

def p_statement_declaration(p):
    'statement : TYPE ID SEMI'
    p[0] = ('declare', p[1], p[2])

def p_statement_assignment(p):
    'statement : ASSIGN ID ASSIGN_OP expression SEMI'
    p[0] = ('assign', p[2], p[4])

def p_assignment(p):
    'assignment : ID ASSIGN_OP expression'
    p[0] = ('assign', p[1], p[3])

def p_statement_print(p):
    'statement : PRINT LPAREN expression RPAREN SEMI'
    p[0] = ('print', p[3])

def p_expression_ternary(p):
    'expression : expression QMARK expression COLON expression'
    p[0] = ('ternary', p[1], p[3], p[5])

def p_expression_logical(p):
    '''expression : expression AND expression
                  | expression OR expression'''
    p[0] = ('logical_op', p[2], p[1], p[3])

def p_expression_relational(p):
    '''expression : expression GT expression
                  | expression LT expression
                  | expression EQ expression'''
    p[0] = ('relational_op', p[2], p[1], p[3])

def p_expression_arithmetic(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression'''
    p[0] = ('binary_op', p[2], p[1], p[3])

def p_expression_increment(p):
    '''expression : ID INCR
                  | ID DECR'''
    p[0] = ('unary_op', p[2], p[1])

def p_expression_group(p):
    'expression : LPAREN expression RPAREN'
    p[0] = p[2]

def p_expression_number(p):
    'expression : NUMBER'
    p[0] = ('number', p[1])

def p_expression_string(p):
    'expression : STRING'
    p[0] = ('string', p[1])

def p_expression_bool(p):
    'expression : BOOL'
    p[0] = ('bool', p[1])

def p_statement_if_else(p):
    '''statement : AGAR LPAREN expression RPAREN TOH LBRACE statement_list RBRACE NAHITOH LBRACE statement_list RBRACE'''
    p[0] = ('if_else', p[3], p[7], p[11])

def p_statement_while(p):
    '''statement : JABTAK LPAREN expression RPAREN LBRACE statement_list RBRACE'''
    p[0] = ('while', p[3], p[6])

def p_statement_for(p):
    '''statement : BAARBAAR LPAREN statement expression SEMI assignment RPAREN LBRACE statement_list RBRACE'''
    p[0] = ('for', p[3], p[4], p[6], p[9])


def p_expression_variable(p):
    'expression : ID'
    p[0] = ('var', p[1])

def p_error(p):
    if p:
        print(f"Syntax error at '{p.value}'")
    else:
        print("Syntax error at EOF")

parser = yacc.yacc()
