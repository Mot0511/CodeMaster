import io
import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from components.runner_configurator.configurator import RunnerConfigurator
from db import getRunners
from models.file import File
from PyQt6.QtGui import QIcon
from initions import initActions, initShortcuts, initTheme
import subprocess
from interface import templete
from utils import get_tree_items, getMemoryData, initData, setMemoryData


class CodeMaster(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(templete)
        uic.loadUi(f, self)
        initActions(self)
        initShortcuts(self)
        initTheme(self)
        initData()
        self.files = []
        self.horSplitter.setStretchFactor(1, 10)
        self.vertSplitter.setStretchFactor(9, 1)
        self.treeView.clicked.connect(self.selectFile)

        memoryData = getMemoryData()
        if memoryData:
            for path in memoryData['openedFiles']:
                self.openFile(path)

            if memoryData['openedFolder']:
                self.openFolder(memoryData['openedFolder'])
        
    def updateOpenedFiles(self):
        openedFiles = [file.path for file in self.files]
        setMemoryData('openedFiles', openedFiles)

    def runFile(self):
        self.saveAll()
        index = self.tabWidget.currentIndex()
        if index == -1: return
        file = self.files[index]
        path = file.path
        runners = getRunners()
        exts = [runner[0] for runner in runners]
        if file.type in exts:
            runner = [runner[1] for runner in runners if runner[0] == file.type][0]
            process = subprocess.Popen([runner, path], stdout=subprocess.PIPE)
            output, errors = process.communicate()
            self.output.setText(output.decode('UTF-8'))
        else:
            self.confRunner()

    def runProject(self):
        if hasattr(self, 'folder'):
            with open(f'{self.folder}/.run_command') as f:
                run_command = f.read()
                result = subprocess.run(run_command.split(' '), capture_output=True, text=True)              
                self.output.setText(result.stdout)

    def confRunner(self):
        confWin = RunnerConfigurator(self.folder if hasattr(self, 'folder') else None)
        confWin.exec()

    def newFile(self):
        file = File('Untitled', '', '', ctx=self)
        self.files.append(file)
        self.tabWidget.addTab(file.textEdit, file.name)

    def saveFile(self):
        index = self.tabWidget.currentIndex()
        if not index == -1: 
            newName = self.files[index].save()
            self.tabWidget.setTabText(index, newName)
    
    def saveFileAs(self):
        index = self.tabWidget.currentIndex()
        if not index == -1: 
            newName = self.files[index].save(isAs=True)
            self.tabWidget.setTabText(index, newName)

    def saveAll(self):
        for file in self.files:
            file.save()

    def closeFile(self, index=None):
        if not index: index = self.tabWidget.currentIndex()
        if not index == -1:
            self.files[index].save()
            self.tabWidget.removeTab(index)
            self.files.remove(self.files[index])

            self.updateOpenedFiles()

    def selectFile(self, index):
        item = self.treeModel.itemFromIndex(index)
        path = item.path
        if path:
            with open(path, 'r', encoding='UTF-8') as f:
                content = f.read()
                file = File(path.split('\\')[-1], path, content, ctx=self)
                self.files.append(file) 
                self.addTab(file.textEdit, file.name)

        self.updateOpenedFiles()

    def openFile(self, path=None):
        if path:
            pathes = [[path], True]
        else:
            pathes = QFileDialog.getOpenFileNames(self, 'Выберите файл для открытия', '')

        if pathes[1]:
            for path in pathes[0]:
                with open(path, 'r', encoding='UTF-8') as f:
                    content = f.read()
                    file = File(path.split('/')[-1], path, content, ctx=self)
                    self.files.append(file)
                    self.addTab(file.textEdit, file.name)


        self.updateOpenedFiles()

    def openFolder(self, path=None):
        path = path if path else QFileDialog.getExistingDirectory(self, 'Выберите папку для открытия')

        if path:
            self.folder = path
            treeModel = get_tree_items(path, self)
            self.treeModel = treeModel
            self.treeView.setModel(treeModel)
            setMemoryData('openedFolder', path)


    def addTab(self, content, title):
        index = self.tabWidget.currentIndex()
        index += 1
        self.tabWidget.insertTab(index, content, title)
        self.tabWidget.setCurrentIndex(index)

    def exit(self):
        quit()

    def about(self):
        msg = QMessageBox()
        msg.setWindowTitle("О программе")
        msg.setText("CodeMaster - это простой редактор кода\nАвтор: MatveySuvorov")
        msg.exec()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('icon.ico'))   
    ex = CodeMaster()
    ex.show()
    sys.exit(app.exec())

