# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PostScreen.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PostScreenDialog(object):
    def setupUi(self, PostScreenDialog):
        PostScreenDialog.setObjectName("PostScreenDialog")
        PostScreenDialog.resize(926, 831)
        self.buttonBox = QtWidgets.QDialogButtonBox(PostScreenDialog)
        self.buttonBox.setGeometry(QtCore.QRect(570, 780, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.plotWidget = PlotWidget(PostScreenDialog)
        self.plotWidget.setGeometry(QtCore.QRect(20, 20, 891, 691))
        self.plotWidget.setObjectName("plotWidget")

        self.retranslateUi(PostScreenDialog)
        self.buttonBox.accepted.connect(PostScreenDialog.accept)
        self.buttonBox.rejected.connect(PostScreenDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(PostScreenDialog)

    def retranslateUi(self, PostScreenDialog):
        _translate = QtCore.QCoreApplication.translate
        PostScreenDialog.setWindowTitle(_translate("PostScreenDialog", "Dialog"))
from pyqtgraph import PlotWidget
