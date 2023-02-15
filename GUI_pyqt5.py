# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 04:04:17 2023

@author: Lucky
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QCheckBox

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Create the text field
        self.string_entry = QLineEdit(self)
        self.string_entry.setGeometry(10, 10, 200, 30)

        # Create the button
        self.print_button = QPushButton("Print", self)
        self.print_button.setGeometry(10, 50, 100, 30)
        self.print_button.clicked.connect(self.print_string)

        # Create the checkbox
        self.check_button = QCheckBox("Check", self)
        self.check_button.setGeometry(10, 90, 100, 30)

        # Set the window properties
        self.setWindowTitle("GUI")
        self.setGeometry(100, 100, 220, 130)
        self.show()

    def print_string(self):
        string = self.string_entry.text()
        print(string)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
