from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication

# # from PyQt5.QtWidgets import QApplication, QtWidget
# # from ui_output import Ui_Form

from PyQt5.QtWebKitWidgets import QWebView
import sys

# # class MainWindow(QWidget, Ui_Form):
# #     def __init__(self, parent=None):
# #         super(MainWindow, self).__init__

app = QApplication(sys.argv)
view = QWebView()
view.show()
view.setUrl(QUrl("http://linuxvoice.com"))
app.exec()