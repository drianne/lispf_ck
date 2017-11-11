import tokenize

st = "(do read inc (loop print dec))"

def make_line_getter(code):
    lines = code.splitlines()    
    def getter():
        if lines:
            line = lines.pop(0)            
            return line.encode('utf-8')
        else:
            return b''
    return getter

for tok in tokenize.tokenize(make_line_getter(st)):
    print(tok)