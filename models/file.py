from PyQt6.QtWidgets import QFileDialog

from components.editor.editor import Editor

class File:
    def __init__(self, name, path, content, ctx):
        self.path = path
        self.name = name
        self.type = path.split('.')[-1]
        self.ctx = ctx
        self.content = content
        self.textEdit = Editor(ctx, self.type)
        self.textEdit.setText(content)

    def save(self, isAs=False):
        content = self.textEdit.toPlainText()

        if not self.path or isAs:
            dialog = QFileDialog.getSaveFileName(self.ctx, 'Select folder to save file', '')
            if dialog[1]:
                self.path = dialog[0]
                self.name = self.path.split('/')[-1]

        if self.path:
            with open(self.path, 'w') as f:
                f.write(content)