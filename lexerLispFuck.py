import ox
import click

@click.command()
@click.argument('source', type=click.File('r'))

def get_tree(source):

    lexer = ox.make_lexer([        
        ('NUMBER', r'\d+'),
        ('NAME', r'[-a-zA-Z]+'),
        ('COMMENT', r';.*'),
        ('NEWLINE', r'\n'),
        ('SPACE', r'\s+'),
        ('RIGHT', r'right'),
        ('LEFT', r'left'),
        ('INC', r'inc'),
        ('DEC', r'dec'),
        ('ADD',r'add'),
        ('SUB',r'sub'),
        ('PRINT', r'print'),
        ('READ', r'read'),
        ('DO',r'do'),
        ('LOOP', r'loop'),
        ('DEF', r'def'),
        ('PARENTHESIS_B', r'\('),
        ('PARENTHESIS_A', r'\)')        
    ])

    tokens = ['NUMBER','INC', 'DEC','SUB', 'ADD','RIGHT', 'LEFT','PRINT','DO','NAME','LOOP',
                'READ','DEF','PARENTHESIS_A','PARENTHESIS_B']

    op = lambda op: (op)
    operator = lambda type_op: (type_op)
    

    parser = ox.make_parser([
        ('program : PARENTHESIS_B expr PARENTHESIS_A', lambda x,y,z: y),
        ('program : PARENTHESIS_B PARENTHESIS_A', lambda x,y: '()'),
        ('expr : operator expr', lambda x,y: (x,) + y),
        ('expr : operator', lambda x: (x,)),
        ('operator : program', op),
        ('operator : LOOP', operator),
        ('operator : DO', operator),
        ('operator : RIGHT', operator),
        ('operator : LEFT', operator),
        ('operator : READ', operator),
        ('operator : INC', operator),
        ('operator : DEC', operator),
        ('operator : DEF', operator),
        ('operator : PRINT', operator),
        ('operator : ADD', operator),
        ('operator : SUB', operator),
        ('operator : NAME', operator),
        ('operator : NUMBER', operator),
    ], tokens)

    program = source.read()

    tokens = lexer(program)

    parserTokens = [token for token in tokens if token.type != 'COMMENT' and token.type != 'SPACE']

    tree = parser(parserTokens)
    print(tree)

if __name__ == '__main__':
    get_tree()
