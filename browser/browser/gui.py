# from PyQt5.QtCore import QUrl
# from PyQt5.QtWidgets import QApplication

# # from PyQt5.QtWidgets import QApplication, QtWidget
# # from ui_output import Ui_Form

# from PyQt5.QtWebKitWidgets import QWebView
# import sys

# # class MainWindow(QWidget, Ui_Form):
# #     def __init__(self, parent=None):
# #         super(MainWindow, self).__init__

# app = QApplication(sys.argv)
# view = QWebView()
# view.show()
# view.setUrl(QUrl("http://linuxvoice.com"))
# app.exec()

from tkinter import *
import urlhandler
def go():
    text.delete(1.0, END)
    conn = urlhandler.urlhandler(entry.get())
    conn.openURL()
    text.insert(INSERT, conn.getURLdata())
    conn.closeURL()
browserwindow = Tk()
browserwindow.title('tugboat')
label = Label(browserwindow, text='url:')
entry = Entry(browserwindow)
button = Button(browserwindow, text='Go', command=go)
text = Text(browserwindow)
label.pack(side=TOP)
entry.pack(side=TOP)
button.pack(side=TOP)
text.pack(side=TOP)
browserwindow.mainloop()