import csv
from PyQt6.QtWidgets import QDialog, QHeaderView, QFileDialog, QTableWidgetItem, QMessageBox
import io
from PyQt6 import uic
from PyQt6.QtGui import QKeySequence, QShortcut
import os
from components.runner_configurator.interface import template
from db import addRunner, deleteRunner, updateExt, updateRunner, getRunners

class RunnerConfigurator(QDialog):
    def __init__(self, folder):
        super().__init__()
        self.setWindowTitle('Runner configurator')
        f = io.StringIO(template)
        # uic.loadUi('components/runner_configurator/runner_configurator.ui', self)
        uic.loadUi(f, self)

        self.runner_file = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Documents', 'CodeMaster', 'runners.json')
        
        self.folder = folder

        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(['Расширение файла (без ".")', 'Программа для запуска'])
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
        path = QFileDialog.getOpenFileName(self, 'Выберите программу для запуска вашего кода', '')
        if path[1]:
            path = path[0]
            row = self.table.rowCount() + 1
            self.table.setRowCount(row)
            self.table.setItem(row - 1, 0, QTableWidgetItem(''))
            self.table.setItem(row - 1, 1, QTableWidgetItem(path))

            self.table.itemChanged.connect(self.edit_data)
    
            addRunner('', path)

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

    def edit_data(self, item):
        column = item.column()
        row = item.row()
        ext = self.table.item(row, 0)
        runner = self.table.item(row, 1)
        if column == 0:
            updateExt(item.text(), runner.text())
        else:
            updateRunner(ext.text(), item.text())

    def delete(self):
        items = self.table.selectedItems()
        if not len(items):
            QMessageBox.information(self, 'Ни одна запись не выбрана', 'Сначала выберите удаляемую программу запуска')
        else:
            btn = QMessageBox.question(
                self,
                "Ты уверен?",
                "Ты действительно хочешь удалить программу запуска?"
            )

            if btn == QMessageBox.StandardButton.Yes:
                item = items[0]
                row = item.row()
                ext = self.table.item(row, 0)
                runner = self.table.item(row, 1)
                deleteRunner(ext.text(), runner.text())
                self.table.removeRow(row)
            else:
                pass
            
    def save_data(self):
        if self.runCommand.text() and self.folder:
            with open(f'{self.folder}/.run_command', 'w') as f:
                f.write(self.runCommand.text())