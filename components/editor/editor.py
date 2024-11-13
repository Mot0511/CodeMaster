from PyQt6.QtWidgets import QTextEdit
from PyQt6.QtGui import QTextCharFormat, QColor, QFont
from highlighter import Highlighter
from components.editor.highlight_configs import highlight_configs
from PyQt6.QtGui import QKeySequence, QShortcut

def Editor(self, ext):
    editor = QTextEdit(self)
    editor.setFont(self.editorFont)

    self.highlighter = Highlighter()
    config = highlight_configs[ext if ext in highlight_configs else 'py']
    # Functions highlighting
    function_format = QTextCharFormat()
    function_format.setForeground(QColor(0, 111, 159))
    pattern = config['functions']
    self.highlighter.add_mapping(pattern, function_format)

    # Classes highlighting
    function_format = QTextCharFormat()
    function_format.setForeground(QColor(208, 103, 0))
    pattern = config['classes']
    self.highlighter.add_mapping(pattern, function_format)

    # 'Self' highlighting
    import_format = QTextCharFormat()
    import_format.setFontItalic(True)
    pattern = config['self']
    self.highlighter.add_mapping(pattern, import_format)

    # Keywords highlighting
    class_format = QTextCharFormat()
    class_format.setForeground(QColor(0, 81, 251))
    for word in config['keywords']:
        pattern = fr'((^|\s){word}(\s|\t))|\(|\)'
        self.highlighter.add_mapping(pattern, class_format)

    # Packages highlighting
    function_format = QTextCharFormat()
    function_format.setForeground(QColor(161, 0, 0))
    pattern = config['packages']
    self.highlighter.add_mapping(pattern, function_format)

    # Imports highlighting
    function_format = QTextCharFormat()
    function_format.setForeground(QColor(255, 0, 0))
    pattern = config['imports']
    self.highlighter.add_mapping(pattern, function_format)

    # Strings highlighting
    import_format = QTextCharFormat()
    import_format.setForeground(QColor(0, 117, 1))
    pattern = config['strings']
    self.highlighter.add_mapping(pattern, import_format)

    # Comments highlighting
    import_format = QTextCharFormat()
    import_format.setForeground(QColor(129, 129, 129))
    import_format.setFontItalic(True)
    pattern = config['comments']
    self.highlighter.add_mapping(pattern, import_format)

    
    return editor, self.highlighter
