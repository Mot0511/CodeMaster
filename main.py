import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog, QTextEdit, QMessageBox
from components.editor.editor import Editor
from highlighter import Highlighter
from models.file import File
from PyQt6.QtGui import QKeySequence
from initions import initActions, initShortcuts, initTheme
import subprocess

from utils import get_tree_items

class CodeMaster(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('interface.ui', self)
        initActions(self)
        initShortcuts(self)
        initTheme(self)
        self.files = []
        self.highlighter = Highlighter()
        self.horSplitter.setStretchFactor(1, 10)
        self.vertSplitter.setStretchFactor(9, 1)
        self.treeView.clicked.connect(self.selectFile)

        path = 'D:\Pyprojs\CodeMaster\\test.py'
        with open(path, 'r') as f:
            content = f.read()
            file = File(path.split('/')[-1], path, content, ctx=self)
            self.files.append(file)
            self.tabWidget.addTab(file.textEdit, file.name)

    def runFile(self):
        index = self.tabWidget.currentIndex()
        file = self.files[index]
        path = file.path
        result = subprocess.run(['C:\\Users\\Matvey\\AppData\\Local\\Programs\\Python\\Python312\\python.exe', path], capture_output=True, text=True)              
        self.output.setText(result.stdout)

    def confRunner(self):
        pass

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
            print(index)
            self.files[index].save()
            self.tabWidget.removeTab(index)
            self.files.remove(self.files[index])

    def selectFile(self, index):
        item = self.treeModel.itemFromIndex(index)
        path = item.path
        if path:
            with open(path, 'r') as f:
                content = f.read()
                file = File(path.split('\\')[-1], path, content, ctx=self)
                self.files.append(file) 
                self.addTab(file.textEdit, file.name)

    def openFile(self):
        pathes = QFileDialog.getOpenFileNames(self, 'Select file to open', '')
        if pathes[1]:
            for path in pathes[0]:
                with open(path, 'r') as f:
                    content = f.read()
                    file = File(path.split('/')[-1], path, content, ctx=self)
                    self.files.append(file)
                    self.addTab(file.textEdit, file.name)

    def openFolder(self):
        path = QFileDialog.getExistingDirectory(self, 'Select folder to open')
        if path:
            self.folder = path
            treeModel = get_tree_items(path, self)
            self.treeModel = treeModel
            self.treeView.setModel(treeModel)

    def addTab(self, content, title):
        index = self.tabWidget.currentIndex()
        index += 1
        self.tabWidget.insertTab(index, content, title)
        self.tabWidget.setCurrentIndex(index)

    def exit(self):
        quit()

    def about(self):
        msg = QMessageBox()
        msg.setWindowTitle("About CodeMaster")
        msg.setText("CodeMaster is a simple code editor\nAuthor: MatveySuvorov")
        msg.exec()

    def enter(self):
        editor = self.files[self.tabWidget.currentIndex()].textEdit
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CodeMaster()
    ex.show()
    sys.exit(app.exec())

