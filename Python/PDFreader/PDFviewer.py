#!/usr/bin/env python

import sys
from PyQt4 import QtGui, QtCore
import popplerqt4

class Application(QtGui.QApplication):
    def __init__(self):
        QtGui.QApplication.__init__(self, sys.argv)     
        self.main = MainWindow()
        self.main.show()

    class MainWindow(QtGui.QFrame):
        def __init__(self, parent=None):
            QtGui.QWidget.__init__(self, parent)
            self.layout = QtGui.QVBoxLayout()
            self.doc = popplerqt4.Poppler.Document.load('/home/benjamin/test.pdf')
            self.page = self.doc.page(1)
# here below i entered almost random dpi, position and size, just to test really 
            self.image = self.page.renderToImage(150, 150, 0, 0, 210, 297)
            self.pixmap = QtGui.QPixmap()
            self.pixmap.fromImage(self.image)
            self.label = QtGui.QLabel(self)
            self.pixmap = QtGui.QPixmap.fromImage(self.image)
            self.layout.addWidget(self.label)
            self.setLayout(self.layout)

    if __name__ == "__main__":
            application = Application()
            sys.exit(application.exec_())