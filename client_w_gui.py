import sys
from PyQt5 import QtWidgets
import client_gui

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
ui = client_gui.Ui_ClientWidget()
ui.setupUi(window)

window.show()
sys.exit(app.exec_())
