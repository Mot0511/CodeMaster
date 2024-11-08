import csv
import os
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6.QtGui import QColor, QFont
import json

def setMemoryData(field, value):
    with open('data/memory.json', 'r') as f:
        data = json.load(f)
    data[field] = value
    with open('data/memory.json', 'w') as f:
        json.dump(data, f)

def getMemoryData():
    with open('data/memory.json', 'r') as f:
        data = json.load(f)
    
    return data

class StandardItem(QStandardItem):
    def __init__(self, text='', path='', set_bold=False, color=QColor(0, 0, 0)):
        super().__init__()

        self.path = path
        fnt = QFont('Open Sans', 14)
        fnt.setBold(set_bold)

        self.setEditable(False)
        self.setForeground(color)
        self.setFont(fnt)
        self.setText(text)

def get_tree_items(path, self):
    treeModel = QStandardItemModel()
    rootNode = treeModel.invisibleRootItem()

    dirs = {}
    for dirname, dirnames, filenames in os.walk(path):
        folder_name = dirname.split('\\')[-1]
        folder = StandardItem(folder_name, None, True, QColor(0, 0, 0))
        for file in filenames:
            file_item = StandardItem(file, dirname+'\\'+file, False, QColor(0, 0, 0))
            folder.insertRow(0, file_item)

        dirs[dirname] = folder

        parent_name = dirname.removesuffix(f'\\{folder_name}')
        if parent_name in dirs and not folder_name == parent_name:
            dirs[parent_name].insertRow(0, folder)

    first_dir = list(dirs.values())[0]
    rootNode.appendRow(first_dir)

    return treeModel

def get_csv_data(name):
    with open(f'data/{name}.csv', encoding='UTF-8') as f:
        reader = csv.reader(f, delimiter=';')
        return list(reader)
    
def get_runners():
    res = {}
    data = get_csv_data('runners')
    for row in data:
        res[row[0]] = row[1]

    return res