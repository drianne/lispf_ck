import ox
import click

@click.command()
@click.argument('source', type=click.File('r'))

def make_tree(source):
    program = source.read()

    lexer_rules = [
        ('NAME', r'[a-zA-Z]+'),
        ('NUMBER', r'\d+'),
        ('RIGHT', r'right'),
        ('LEFT', r'left'),
        ('OPEN_PAREN', r'\('),
        ('CLOSE_PAREN', r'\)'),
        ('INCR', r'incr'),
        ('COMMA', r'\,'),
        ('SPACE', r'\s+'),
        ('NEWLINE', r'\n'),
        ('DEF', r'def'),
        ('DO',r'do'),
        ('SEMICOLON',r';')
    ]

    lexer = ox.make_lexer(lexer_rules)
    
    tokens = lexer(program)

    operator = lambda type_op: type_op

    op = lambda op: op
    opr = lambda op, num: (op, num)

    parser_rules = [
        ('program : OPEN_PAREN expr CLOSE_PAREN', lambda x,y,z: y),
        ('program : OPEN_PAREN CLOSE_PAREN', lambda x,y: '()'),
        ('expr : operator expr', lambda x,y: (x,) + y),
        ('expr : operator', lambda x: (x,)),
        ('operator : program', op),
        ('operator : DO', operator),
        ('operator : RIGHT', operator),
        ('operator : LEFT', operator),
        ('operator : INC', operator),
        ('operator : PRINT', operator),
        ('operator : ADD', operator),
        ('operator : NUMBER', operator),
    ]

    
if __name__ == '__main__':
    make_tree()
