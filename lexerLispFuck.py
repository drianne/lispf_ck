import click
import re
from collections import namedtuple

@click.command()
@click.argument('lispf_ck',type=click.File('r'))

# O comando click usado pra obter argumentos na linha de comando

def tokenize(lispf_ck):
    source = lispf_ck.read()
    print(list(lexer(source)))

def lexer(source):
    Token = namedtuple(
    'Token', 
    ['type', 'data', 'lineno']
    )

    regex_map = [
    ('LPAR', r'\('),
    ('RPAR', r'\)'),
    ('NUMBER', r'[0-9]+(\.[0-9]*)?'),
    ('OP', r'inc|dec|print|read|loop|right|left|add|def'),
    ('SPACE', r'\s+'),
    ]

    template = r'(?P<{name}>{regex})'
    REGEX_ALL = '|'.join(
    template.format(name=name, regex=regex)
    for (name, regex) in regex_map
    )
    re_all = re.compile(REGEX_ALL)

    lineno = 1
    for m in re_all.finditer(source):
        type_ = m.lastgroup
        if type_ == 'SPACE':
            continue
        elif type_ == 'NEWLINE':
            lineno += 1
            continue 
        i, j = m.span()
        data = m.string[i:j]
        
        yield Token(type_, data, lineno)


if __name__ == "__main__":
    tokenize()
    
