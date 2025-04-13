# src/lexer.py
import ply.lex as lex

tokens = [
    'ID', 'NUMBER', 'STRING',
    'ASSIGN', 'ADD', 'SUB', 'MUL', 'DIV',
    'GT', 'LT', 'EQ',
    'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE', 'SEMI', 'COMMA', 'PRINT', 'EQUALS'
]

reserved = {
    'rakho': 'ASSIGN',
    'bolBhai': 'PRINT',
    'agar': 'IF',
    'toh': 'THEN',
    'nahiToh': 'ELSE',
    'jabTak': 'WHILE',
    'baarBaar': 'FOR',
    'jodo': 'ADD',
    'ghatao': 'SUB',
    'guna': 'MUL',
    'bhaag': 'DIV',
    'badaHai': 'GT',
    'chhotaHai': 'LT',
    'barabarHai': 'EQ',
}

t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_SEMI = r';'
t_COMMA = r','
t_EQUALS = r'='

def t_STRING(t):
    r'"[^"]*"'
    t.value = t.value[1:-1]
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')
    return t

t_ignore = ' \t\n'

def t_error(t):
    print(f"Illegal character: {t.value[0]}")
    t.lexer.skip(1)

lexer = lex.lex()
