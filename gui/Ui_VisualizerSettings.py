# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_VisualizerSettings.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_VisualizerSettingsForm(object):
    def setupUi(self, VisualizerSettingsForm):
        VisualizerSettingsForm.setObjectName("VisualizerSettingsForm")
        VisualizerSettingsForm.resize(604, 442)
        self.formLayout = QtWidgets.QFormLayout(VisualizerSettingsForm)
        self.formLayout.setObjectName("formLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(VisualizerSettingsForm)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.chartLineWidth = QtWidgets.QDoubleSpinBox(VisualizerSettingsForm)
        self.chartLineWidth.setMinimum(1.0)
        self.chartLineWidth.setMaximum(10.0)
        self.chartLineWidth.setObjectName("chartLineWidth")
        self.horizontalLayout.addWidget(self.chartLineWidth)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(VisualizerSettingsForm)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.chartBackground = QtWidgets.QLineEdit(VisualizerSettingsForm)
        self.chartBackground.setObjectName("chartBackground")
        self.horizontalLayout_2.addWidget(self.chartBackground)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.LabelRole, self.verticalLayout)

        self.retranslateUi(VisualizerSettingsForm)
        QtCore.QMetaObject.connectSlotsByName(VisualizerSettingsForm)

    def retranslateUi(self, VisualizerSettingsForm):
        _translate = QtCore.QCoreApplication.translate
        VisualizerSettingsForm.setWindowTitle(_translate("VisualizerSettingsForm", "Visualizer"))
        self.label.setText(_translate("VisualizerSettingsForm", "Chart line width:"))
        self.label_2.setText(_translate("VisualizerSettingsForm", "Chart background:"))
