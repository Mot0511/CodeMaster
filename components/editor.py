from PyQt6.QtWidgets import QTextEdit
from PyQt6.QtGui import QTextCharFormat, QColor, QFont
from highlighter import Highlighter

def Editor(self):
    editor = QTextEdit(self)
    editor.setFont(self.editorFont)

    

    # Functions highlighting
    function_format = QTextCharFormat()
    function_format.setForeground(QColor(0, 111, 159))
    pattern = r'\w+\(.*\)'
    self.highlighter.add_mapping(pattern, function_format)

    # Classes highlighting
    function_format = QTextCharFormat()
    function_format.setForeground(QColor(208, 103, 0))
    pattern = r'((^|\s)class(\s|\t)\w+)|\w+\.'
    self.highlighter.add_mapping(pattern, function_format)

    # 'Self' highlighting
    import_format = QTextCharFormat()
    import_format.setFontItalic(True)
    pattern = r'\Wself\W'
    self.highlighter.add_mapping(pattern, import_format)

    # Keywords highlighting
    keywords = ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await',
 'break', 'class', 'continue', 'def', 'del', 'elif', 'else',
 'except', 'finally', 'for', 'from', 'global', 'if', 'import',
 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise',
 'return', 'try', 'while', 'with', 'yield']

    class_format = QTextCharFormat()
    class_format.setForeground(QColor(0, 81, 251))
    for word in keywords:
        pattern = fr'((^|\s){word}(\s|\t))|\(|\)'
        self.highlighter.add_mapping(pattern, class_format)

    

    # Packages highlighting
    function_format = QTextCharFormat()
    function_format.setForeground(QColor(161, 0, 0))
    pattern = r'^import\s.+|^from\s.+'
    self.highlighter.add_mapping(pattern, function_format)

    # Imports highlighting
    function_format = QTextCharFormat()
    function_format.setForeground(QColor(255, 0, 0))
    pattern = r'^from\s|^import\s|\simport\s'
    self.highlighter.add_mapping(pattern, function_format)

    # Strings highlighting
    import_format = QTextCharFormat()
    import_format.setForeground(QColor(0, 117, 1))
    pattern = r'\'.*\'|\".*\"'
    self.highlighter.add_mapping(pattern, import_format)

    

    # Comments highlighting
    import_format = QTextCharFormat()
    import_format.setForeground(QColor(129, 129, 129))
    import_format.setFontItalic(True)
    pattern = r'#.*'
    self.highlighter.add_mapping(pattern, import_format)


    self.highlighter.setDocument(editor.document())
    return editor