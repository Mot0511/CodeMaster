from PyQt6.QtGui import QKeySequence, QShortcut, QFont

def initTheme(self):
    editorFont = QFont()
    editorFont.setPointSize(18)
    self.editorFont = editorFont

def initActions(self):
    self.actionNew.triggered.connect(self.newFile)
    self.actionOpen.triggered.connect(self.openFile)
    self.actionOpen_folder.triggered.connect(self.openFolder)
    self.actionSave.triggered.connect(self.saveFile)
    self.actionSave_as.triggered.connect(self.saveFileAs)
    self.actionSave_all.triggered.connect(self.saveAll)
    self.actionExit.triggered.connect(self.exit)
    self.actionClose.triggered.connect(self.closeFile)
    self.actionAbout_CodeMaster.triggered.connect(self.about)

    self.actionRun_file.triggered.connect(self.runFile)
    self.actionRun_project.triggered.connect(self.runProject)
    self.actionConfigure_runner.triggered.connect(self.confRunner)
    
    self.tabWidget.tabCloseRequested.connect(self.closeFile)

def initShortcuts(self):
    newFileSC = QShortcut(QKeySequence("Ctrl+N"), self)
    newFileSC.activated.connect(self.newFile)
    openFileSC = QShortcut(QKeySequence("Ctrl+O"), self)
    openFileSC.activated.connect(self.openFile)
    openFolderSC = QShortcut(QKeySequence("Ctrl+Shift+O"), self)
    openFolderSC.activated.connect(self.openFolder)
    saveFileSC = QShortcut(QKeySequence("Ctrl+S"), self)
    saveFileSC.activated.connect(self.saveFile)
    saveAsFileSC = QShortcut(QKeySequence("Ctrl+Shift+S"), self)
    saveAsFileSC.activated.connect(self.saveFileAs)
    saveAllFileSC = QShortcut(QKeySequence("Ctrl+Alt+N"), self)
    saveAllFileSC.activated.connect(self.saveAll)
    closeFileSC = QShortcut(QKeySequence("Ctrl+W"), self)
    closeFileSC.activated.connect(self.closeFile)
    exitFileSC = QShortcut(QKeySequence("Ctrl+Q"), self)
    exitFileSC.activated.connect(self.exit)

    runProjectSC = QShortcut(QKeySequence("F5"), self)
    runProjectSC.activated.connect(self.runProject)