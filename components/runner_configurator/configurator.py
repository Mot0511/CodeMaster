import csv
from PyQt6.QtWidgets import QDialog, QHeaderView, QFileDialog, QTableWidgetItem
from PyQt6 import uic
from PyQt6.QtGui import QKeySequence, QShortcut, QFont
import os

from db import updateRunners, getRunners

class RunnerConfigurator(QDialog):
    def __init__(self, folder):
        super().__init__()
        self.setWindowTitle('Runner configurator')
        uic.loadUi('components/runner_configurator/runner_configurator.ui', self)

        self.runner_file = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Documents', 'CodeMaster', 'runners.json')
        
        self.folder = folder

        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(['Extension of file (without ".")', 'Runner'])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.init_runners_data()
        self.table.itemChanged.connect(self.edit_data)

        self.init_run_command()

        delSC = QShortcut(QKeySequence("Del"), self)
        delSC.activated.connect(self.delete)

        self.addBtn.clicked.connect(self.select_runner)
        self.buttonBox.accepted.connect(self.save_data)

    def select_runner(self):
        self.table.itemChanged.disconnect()
        path = QFileDialog.getOpenFileName(self, 'Select runner of your language', '')
        if path[1]:
            path = path[0]
            row = self.table.rowCount() + 1
            self.table.setRowCount(row)
            self.table.setItem(row - 1, 0, QTableWidgetItem(''))
            self.table.setItem(row - 1, 1, QTableWidgetItem(path))

            self.table.itemChanged.connect(self.edit_data)
    
        self.edit_data()

    def init_run_command(self):
        if self.folder and os.path.exists(f'{self.folder}/.run_command'):
            with open(f'{self.folder}/.run_command', 'r') as f:
                self.runCommand.setText(f.read())

    def init_runners_data(self):
        runners = getRunners()
        for i, row in enumerate(runners):
            self.table.setRowCount(i + 1)
            for j, elem in enumerate(row):
                self.table.setItem(i, j, QTableWidgetItem(elem))

        self.runners = runners

    def edit_data(self):
        runners = []
        for i in range(self.table.rowCount()):
            ext = self.table.item(i, 0).text()
            path = self.table.item(i, 1).text()
            runners.append([ext, path])

        self.runners = runners        

    def delete(self):
        row = self.table.currentRow()
        if row > -1:
            self.table.removeRow(row)

        self.edit_data()

    def save_data(self):
        updateRunners(self.runners)

        if self.runCommand.text() and self.folder:
            with open(f'{self.folder}/.run_command', 'w') as f:
                f.write(self.runCommand.text())