from PyQt5 import QtCore, QtGui,QtWidgets
import json

from ui import  ui_MainWindow


class NoteWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow
        self.ui.setupUi(self)
        self.notes = {}

        self.ui.pushButton.cliced.connect(self.add_note)
        self.ui.listWidget.itemCliked.connect(self.save_note)
        self.ui.pushButton_3.cliced.conect(self.save_note)
        self.ui.pushButton_4.cliced.conect
        self.ui.pushButton_5.cliced.conect(self.del_tag)
        self.ui.pushButton_6.cliced.conect(self.search_tag)

        self.load_notes()

        def load_notes(self):
            try:
                with open("notes_data.json", "r", encoding)
                    self.notes = _json.load(file)
                self.ui.listWidget.addItems(self.notes)
            e

