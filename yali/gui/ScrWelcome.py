# -*- coding: utf-8 -*-
#
# Copyright (C) 2010 TUBITAK/UEKAE
#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free
# Software Foundation; either version 2 of the License, or (at your option)
# any later version.
#
# Please read the COPYING file.
#
import gettext
_ = gettext.translation('yali', fallback=True).ugettext

from PyQt5.Qt import QWidget, pyqtSignal
import yali.context as ctx
from yali.gui import ScreenWidget
from yali.gui.Ui.welcome import Ui_WelcomeWidget

class Widget(QWidget, ScreenWidget):
    name = "welcome"

    def __init__(self):
        QWidget.__init__(self)
        self.ui = Ui_WelcomeWidget()
        self.ui.setupUi(self)

    def shown(self):
        ctx.mainScreen.disableBack()
