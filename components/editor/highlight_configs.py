highlight_configs = {
    'py': {
        'keywords': ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await',
                    'break', 'class', 'continue', 'def', 'del', 'elif', 'else',
                    'except', 'finally', 'for', 'from', 'global', 'if', 'import',
                    'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise',
                    'return', 'try', 'while', 'with', 'yield'
                    ],
        'functions': r'\w+\(.*\)',
        'classes': r'((^|\s)class(\s|\t)\w+)|\w+\.',
        'self': r'\Wself\W',
        'packages': r'^import\s.+|^from\s.+',
        'imports': r'^from\s|^import\s|\simport\s',
        'strings': r'\'.*\'|\".*\"',
        'comments': r'#.*',
    },
    'js': {
        'keywords': ['var', 'let', 'const', 'function', 'return', 'class', 'if', 'else', 
                     'switch', 'case', 'default', 'break', 'continue', 'for', 'while', 'do', 
                     'try', 'catch', 'finally', 'debugger', 'delete', 'export', 'extends', 'import', 
                     'in', 'instanceof', 'new', 'null', 'super', 'this', 'throw', 'typeof'
                    ],
        'functions': r'\w+\(.*\)',
        'classes': r'((^|\s)class(\s|\t)\w+)|\w+\.',
        'self': r'\Wthis\W',
        'packages': r'^import\s.+|^from\s.+',
        'imports': r'^from\s|^import\s|\simport\s',
        'strings': r'\'.*\'|\".*\"',
        'comments': r'#.*',
    },
    'ts': {
        'keywords': ['var', 'let', 'const', 'function', 'return', 'class', 'if', 'else', 
                     'switch', 'case', 'default', 'break', 'continue', 'for', 'while', 'do', 
                     'try', 'catch', 'finally', 'debugger', 'delete', 'export', 'extends', 'import', 
                     'in', 'instanceof', 'new', 'null', 'super', 'this', 'throw', 'typeof'
                    ],
        'functions': r'\w+\(.*\)',
        'classes': r'((^|\s)class(\s|\t)\w+)|\w+\.',
        'self': r'\Wthis\W',
        'packages': r'^import\s.+|^from\s.+',
        'imports': r'^from\s|^import\s|\sfrom\s',
        'strings': r'\'.*\'|\".*\"',
        'comments': r'//.*',
    }
}