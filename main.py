import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog, QTextEdit, QMessageBox
from components.editor.editor import Editor
from components.runner_configurator.configurator import RunnerConfigurator
from highlighter import Highlighter
from models.file import File
from PyQt6.QtGui import QKeySequence
from initions import initActions, initShortcuts, initTheme
import subprocess
import asyncio
from multiprocessing import Process

from utils import get_runners, get_tree_items, getMemoryData, setMemoryData

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

        memoryData = getMemoryData()
        for path in memoryData['openedFiles']:
            self.openFile(path)

        if memoryData['openedFolder']:
            self.openFolder(memoryData['openedFolder'])
        
    def updateOpenedFiles(self):
        openedFiles = [file.path for file in self.files]
        setMemoryData('openedFiles', openedFiles)

    async def runFile(self):
        self.saveAll()
        index = self.tabWidget.currentIndex()
        if index == -1: return
        file = self.files[index]
        path = file.path
        runners = get_runners()
        if file.type in runners:
            runner = runners[file.type]
            # process = subprocess.Popen([runner, path], stdout=subprocess.PIPE)
            process = await asyncio.create_subprocess_shell(cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)

            # stdout, stderr = await proc.communicate()

            # if stdout:
            #     print(f'[stdout]\n{stdout.decode()}')
            # output, errors = process.communicate()
            # self.output.setText(output.decode('UTF-8'))
            for line in iter(process.stdout.readline, ''):
                self.output.setText(line.decode('UTF-8'))

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
        confWin.setWindowTitle('Runner configurator')
        confWin.exec()

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
            pathes = QFileDialog.getOpenFileNames(self, 'Select file to open', '')

        if pathes[1]:
            for path in pathes[0]:
                with open(path, 'r', encoding='UTF-8') as f:
                    content = f.read()
                    file = File(path.split('/')[-1], path, content, ctx=self)
                    self.files.append(file)
                    self.addTab(file.textEdit, file.name)


        self.updateOpenedFiles()

    def openFolder(self, path=None):
        path = path if path else QFileDialog.getExistingDirectory(self, 'Select folder to open')

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
        msg.setWindowTitle("About CodeMaster")
        msg.setText("CodeMaster is a simple code editor\nAuthor: MatveySuvorov")
        msg.exec()


async def run():
    app = QApplication(sys.argv)
    ex = CodeMaster()
    ex.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    asyncio.run(run())
