# src/parser.py
import ply.yacc as yacc
from lexer import tokens

variables = {}

def p_program(p):
    '''program : program statement
               | statement'''
    if len(p) == 3:
        p[0] = ['program', p[1], p[2]]
    else:
        p[0] = ['program', p[1]]

def p_statement_assign(p):
    'statement : ASSIGN ID EQUALS expression SEMI'
    p[0] = ['assign', p[2], p[4]]

def p_statement_print(p):
    'statement : PRINT LPAREN expression RPAREN SEMI'
    p[0] = ['print', p[3]]

def p_expression_binop(p):
    '''expression : expression ADD expression
                  | expression SUB expression
                  | expression MUL expression
                  | expression DIV expression'''
    ops = {'jodo': '+', 'ghatao': '-', 'guna': '*', 'bhaag': '/'}
    p[0] = ['binop', ops[p[2]], p[1], p[3]]

def p_expression_group(p):
    'expression : LPAREN expression RPAREN'
    p[0] = ['group', p[2]]

def p_expression_number(p):
    'expression : NUMBER'
    p[0] = ['number', p[1]]

def p_expression_string(p):
    'expression : STRING'
    p[0] = ['string', p[1]]

def p_expression_variable(p):
    'expression : ID'
    p[0] = ['variable', p[1]]

def p_error(p):
    print("Syntax error", p)

parser = yacc.yacc()
