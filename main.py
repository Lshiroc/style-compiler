from ply import lex
import ply.yacc as yacc

tokens = ('PACKAGE_NAME', 'LPAREN', 'RPAREN', 'STRING', 'CLASS', 'NUMBER', 'CONTENT')

t_ignore = ' \t'

t_LPAREN = r'\('
t_RPAREN = r'\)'
t_STRING = r'[a-zA-Z_][a-zA-Z0-9_]'
# t_COMPONENT = r'\@'

def t_CONTENT(t):
    r'.+'
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_ignore_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count('\n')

def t_error(t):
    print(f'Illegal character {t.value[0]!r}')
    t.lexer.skip(1)

lexer = lex.lex()

# Parsing

def p_expression(p):
    '''
    expression : term
    '''
    p[0] = p[1]

def p_term_factor(p):
    '''
    term : factor
    '''
    p[0] = p[1]

def p_factor_grouped(p):
    '''
    factor : LPAREN expression RPAREN
    '''
    p[0] = ('grouped', p[2])

def p_error(p):
    print(f"Syntax error at {p.value!r}")

parser = yacc.yacc(debug=True)
ast = parser.parse(input="7", lexer=lexer)
# print(ast)
