from PyQt6.QtWidgets import QDialog
from PyQt6 import uic

class RunnerConfigurator(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Runner configurator')
        uic.loadUi('runner_configurator.ui', self)
    