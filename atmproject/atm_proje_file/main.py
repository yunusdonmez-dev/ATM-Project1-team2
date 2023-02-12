from PyQt5.QtWidgets import QApplication
from account import LoginPage
import os
import sys

app =QApplication([])

pencere = LoginPage()
pencere.show()
app.exec_()

