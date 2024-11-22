import csv
import os
import sqlite3
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6.QtGui import QColor, QFont
import json
import os

def initData():
    memory_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Documents', 'CodeMaster')
    if not os.path.isdir(memory_path):
        os.mkdir(memory_path)
        memory_file = os.path.join(memory_path, 'memory.json')
        if not os.path.exists(memory_file):
            with open(memory_file, 'w') as f:
                f.write('{"openedFolder": "","openedFiles": []}')
            
        
        runners_file = os.path.join(memory_path, 'runners.db')
        if not os.path.exists(runners_file):
            conn = sqlite3.connect(runners_file)
            cur = conn.cursor()
            query_runners = """CREATE TABLE runners 
                        (
                        ext VARCHAR(255),
                        runner VARCHAR(255)
                        );
            """
            query_logs = """CREATE TABLE logs 
                        (
                        message VARCHAR(255),
                        datetime VARCHAR(255)
                        );
            """
            cur.execute(query_runners)
            cur.execute(query_logs)
            conn.commit()
            conn.close()
            

def setMemoryData(field, value):
    memory_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Documents', 'CodeMaster', 'memory.json')
    with open(memory_path, 'r') as f:
        data = json.load(f)

    data[field] = value
    with open(memory_path, 'w') as f:
        json.dump(data, f)


def getMemoryData():
    memory_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Documents', 'CodeMaster', 'memory.json')
    try:
        with open(memory_path, 'r') as f:
            data = json.load(f)
        
        return data
    except FileNotFoundError:
        return None

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

    if len(list(dirs.values())):
        first_dir = list(dirs.values())[0]
        rootNode.appendRow(first_dir)

        return treeModel

    return None