import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog, QTextEdit
from models.file import File

class CodeMaster(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('interface.ui', self)
        self.actionNew.triggered.connect(self.newFile)
        self.actionOpen.triggered.connect(self.openFile)
        self.actionSave.triggered.connect(self.saveFile)
        self.actionSave_as.triggered.connect(self.saveFileAs)
        self.actionClose.triggered.connect(self.closeFile)
        self.files = []

    def newFile(self):
        textEdit = QTextEdit(self)
        file = File('Untitled', '', '', textEdit, ctx=self)
        self.files.append(file)
        self.tabWidget.addTab(file.textEdit, file.name)

    def saveFile(self):
        index = self.tabWidget.currentIndex()
        self.files[index].save()
    
    def saveFileAs(self):
        index = self.tabWidget.currentIndex()
        self.files[index].save(isAs=True)

    def closeFile(self):
        index = self.tabWidget.currentIndex()
        self.tabWidget.removeTab(index)
        self.files.remove(self.files[index])

    def openFile(self):
        path = QFileDialog.getOpenFileName(self, 'Select file to open', '')[0]
        if path:
            with open(path, 'r') as f:
                content = f.read()
                textEdit = QTextEdit(self)
                file = File(path.split('/')[-1], path, content, textEdit, ctx=self)
                self.files.append(file)
                self.tabWidget.addTab(file.textEdit, file.name)
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CodeMaster()
    ex.show()
    sys.exit(app.exec())

