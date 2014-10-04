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

import sys, os
import argparse
import webbrowser
from PyQt4 import QtGui, QtCore, QtWebKit

BASE_PATH = os.path.dirname(os.path.realpath(__file__))

from js.login import *
from js.ads import *


class Fase(QtGui.QMainWindow):

    def _loadFinished(self):
        # ----- Remove Ads
        if self.args.no_ads:
            self.web.page().mainFrame().evaluateJavaScript(
                jsRemoveAdsById)
            #self.web.page().mainFrame().evaluateJavaScript(
            #    jsRemoveAdsByClass)
        # ----- Fill login form
        if self.args.username and self.args.password:
            self.web.page().mainFrame().evaluateJavaScript(
                jsFillLoginForm.format(username = self.args.username,
                                       password = self.args.password)
                )
            # ----- Autologin
            if self.args.auto_login:
                self.web.page().mainFrame().evaluateJavaScript(
                    jsClickLoginButton)

    def _link_clicked(self, qurl):
        url = qurl.toString()
        import re
        pat = re.compile(
            '(https|http)://(l|www).facebook.com/l.php[?]u=((.)+)&h=(.)+')
        res = pat.match(url)
        if res:
            url = res.group(3)
        # ----- Check if url is an internal facebook link
        pat = re.compile('(https|http)://www.facebook.com/.+')
        res = pat.match(url)
        # ----- Site is external: Open Link in default browser
        if not res:
            if webbrowser.open(url):
                print 'Open external URL',
            else:
                print 'Impossible to open URL',
            print url
        else:
            self.web.setUrl(QtCore.QUrl(url))

    def __init__(self, args):
        self.args = args
        # ----- Window
        QtGui.QMainWindow.__init__(self)
        self.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.resize(800, 600)
        self.setWindowState(QtCore.Qt.WindowMaximized)
        self.setWindowTitle('FASE - Facebook Separated Environment')
        self.setWindowIcon(QtGui.QIcon('%s/images/fase.png' % (BASE_PATH)))
        # ----- Content creation
        main_grid = QtGui.QGridLayout()
        self.main_grid = main_grid
        # ----- Enabled plugins (Flash Videos)
        #       "Please Flash, kill yourself!!!!!!!!!!!!"
        QtWebKit.QWebSettings.globalSettings().setAttribute(
            QtWebKit.QWebSettings.PluginsEnabled, True)
        # /TEST
        # ----- Webkit
        self.web = QtWebKit.QWebView()
        self.web.setUrl(QtCore.QUrl('https://www.facebook.com'))
        # ----- Manage Javascript scripts
        self.web.loadFinished.connect(self._loadFinished)
        # ----- Manage links
        self.web.page().setLinkDelegationPolicy(
            QtWebKit.QWebPage.DelegateAllLinks)
        self.web.linkClicked.connect(self._link_clicked)
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
    parser.add_argument('-a', '--no-ads', dest='no_ads',
                        action='store_true',
                        help='Hide Ads from Facebook pages')
    args = parser.parse_args()

    # ----- Init app
    app = QtGui.QApplication(sys.argv)
    fase_main = Fase(args)
    fase_main.show()
    sys.exit(app.exec_())
