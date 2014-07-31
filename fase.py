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
import argparse
from PyQt4 import QtGui, QtCore, QtWebKit

jsFillLoginForm = """ 
    document.getElementById('email').value='{username}';
    document.getElementById('pass').value='{password}';
    """
jsClickLoginButton = """
    document.getElementById('u_0_l').click(); void(0);
    """


class Fase(QtGui.QMainWindow):

    def _loadFinished(self):
        if self.args.username and self.args.password:
            self.web.page().mainFrame().evaluateJavaScript(
                jsFillLoginForm.format(username = self.args.username,
                                       password = self.args.password)
                )
            if self.args.auto_login:
                self.web.page().mainFrame().evaluateJavaScript(
                    jsClickLoginButton)

    def __init__(self, args):
        self.args = args
        # ----- Window
        QtGui.QMainWindow.__init__(self)
        self.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.resize(800, 600)
        self.setWindowState(QtCore.Qt.WindowMaximized)
        self.setWindowTitle('FASE - Facebook Separated Environment')
        # ----- Content creation
        main_grid = QtGui.QGridLayout()
        self.main_grid = main_grid
        # ----- Webkit
        self.web = QtWebKit.QWebView()
        self.web.setUrl(QtCore.QUrl('http://www.facebook.com'))
        self.web.loadFinished.connect(self._loadFinished)
        self.setCentralWidget(self.web)


if __name__ == "__main__":

    # ----- Parse terminal arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--username', dest='username',
                        help='Set username')
    parser.add_argument('-p', '--password', dest='password',
                        help='Set password')
    parser.add_argument('-l', '--auto-login', dest='auto_login',
                        action='store_true',
                        help='Autologin in Facebook')
    args = parser.parse_args()

    # ----- Init app
    app = QtGui.QApplication(sys.argv)
    fase_main = Fase(args)
    fase_main.show()
    sys.exit(app.exec_())
