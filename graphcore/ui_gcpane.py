# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gcpane.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_GCPane(object):
    def setupUi(self, GCPane):
        GCPane.setObjectName("GCPane")
        GCPane.resize(855, 720)
        self.gridLayout = QtWidgets.QGridLayout(GCPane)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(GCPane)
        self.tabWidget.setObjectName("tabWidget")
        self.tab2d = QtWidgets.QWidget()
        self.tab2d.setObjectName("tab2d")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab2d)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.graphicsView = QtWidgets.QGraphicsView(self.tab2d)
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout_2.addWidget(self.graphicsView, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab2d, "")
        self.tab3d = QtWidgets.QWidget()
        self.tab3d.setObjectName("tab3d")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab3d)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.openGLWidget = QtWidgets.QOpenGLWidget(self.tab3d)
        self.openGLWidget.setObjectName("openGLWidget")
        self.gridLayout_3.addWidget(self.openGLWidget, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab3d, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.retranslateUi(GCPane)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(GCPane)

    def retranslateUi(self, GCPane):
        _translate = QtCore.QCoreApplication.translate
        GCPane.setWindowTitle(_translate("GCPane", "GCPane"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab2d), _translate("GCPane", "2D Pane"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab3d), _translate("GCPane", "3D Pane"))