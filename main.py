import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog, QTextEdit, QMessageBox
from components.editor.editor import Editor
from highlighter import Highlighter
from models.file import File
from PyQt6.QtGui import QKeySequence
from initions import initActions, initShortcuts, initTheme
import subprocess

class CodeMaster(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('interface.ui', self)
        initActions(self)
        initShortcuts(self)
        initTheme(self)
        self.files = []
        self.highlighter = Highlighter()

        path = 'D:\Pyprojs\CodeMaster\main.py'
        with open(path, 'r') as f:
            content = f.read()
            file = File(path.split('/')[-1], path, content, ctx=self)
            self.files.append(file)
            self.tabWidget.addTab(file.textEdit, file.name)


    def fontsizeUp(self):
        print(1)
        size = self.editorFont.pixelSize()
        size += 2
        self.editorFont.setPointSize(size)

    def fontsizeDown(self):
        size = self.editorFont.pixelSize()
        size -= 2
        self.editorFont.setPointSize(size)

    def newFile(self):
        file = File('Untitled', '', '', ctx=self)
        self.files.append(file)
        self.tabWidget.addTab(file.textEdit, file.name)

    def saveFile(self):
        index = self.tabWidget.currentIndex()
        if not index == -1: self.files[index].save()
    
    def saveFileAs(self):
        index = self.tabWidget.currentIndex()
        if not index == -1: self.files[index].save(isAs=True)

    def saveAll(self):
        for file in self.files:
            file.save()

    def closeFile(self, index=None):
        if not index: index = self.tabWidget.currentIndex()
        if not index == -1:
            self.files[index].save()
            self.tabWidget.removeTab(index)
            self.files.remove(self.files[index])

    def openFile(self):
        pathes = QFileDialog.getOpenFileNames(self, 'Select file to open', '')
        if pathes[1]:
            for path in pathes[0]:
                with open(path, 'r') as f:
                    content = f.read()
                    file = File(path.split('/')[-1], path, content, ctx=self)
                    self.files.append(file)
                    self.tabWidget.addTab(file.textEdit, file.name)

    def exit(self):
        quit()

    def about(self):
        msg = QMessageBox()
        msg.setWindowTitle("About CodeMaster")
        msg.setText("CodeMaster is a simple code editor\nAuthor: MatveySuvorov")
        msg.exec()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CodeMaster()
    ex.show()
    sys.exit(app.exec())

