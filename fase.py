#!/usr/bin/python

# ######################################################################
#
#  FaSE - Facebook Separated Environment
#
#  Copyright 2014 Francesco OpenCode Apruzzese <opencode@e-ware.org>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
# ######################################################################

import sys
from PyQt4 import QtGui, QtCore, QtWebKit


class Fase(QtGui.QMainWindow):

    def __init__(self):
        # ----- Window
        QtGui.QMainWindow.__init__(self)
        self.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.resize(800, 600)
        self.setWindowState(QtCore.Qt.WindowMaximized)
        self.setWindowTitle('FASE - Facebook Separated Environment')
        self.statusBar().showMessage(
            'Welcome to FaSE')
        # ----- Content creation
        main_grid = QtGui.QGridLayout()
        self.main_grid = main_grid
        # ----- Webkit
        web = QtWebKit.QWebView()
        web.setUrl(QtCore.QUrl('http://www.facebook.com'))
        self.setCentralWidget(web)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    fase_main = Fase()
    fase_main.show()
    sys.exit(app.exec_())
