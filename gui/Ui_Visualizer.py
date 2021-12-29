# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_Visualizer.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_visualizerDialog(object):
    def setupUi(self, visualizerDialog):
        visualizerDialog.setObjectName("visualizerDialog")
        visualizerDialog.resize(1098, 885)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(visualizerDialog.sizePolicy().hasHeightForWidth())
        visualizerDialog.setSizePolicy(sizePolicy)
        visualizerDialog.setMinimumSize(QtCore.QSize(800, 600))
        visualizerDialog.setMaximumSize(QtCore.QSize(1920, 1080))
        visualizerDialog.setSizeGripEnabled(False)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(visualizerDialog)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.frame = QtWidgets.QFrame(visualizerDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        self.groupBox_13 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_13.setObjectName("groupBox_13")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.groupBox_13)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.frame_16 = QtWidgets.QFrame(self.groupBox_13)
        self.frame_16.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_16.setObjectName("frame_16")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_16)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.frame_15 = QtWidgets.QFrame(self.frame_16)
        self.frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_15)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_8 = QtWidgets.QLabel(self.frame_15)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_4.addWidget(self.label_8)
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.frame_15)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.horizontalLayout_4.addWidget(self.doubleSpinBox)
        self.label_9 = QtWidgets.QLabel(self.frame_15)
        self.label_9.setStyleSheet("text-align: center")
        self.label_9.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_9.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_4.addWidget(self.label_9)
        self.doubleSpinBox_2 = QtWidgets.QDoubleSpinBox(self.frame_15)
        self.doubleSpinBox_2.setObjectName("doubleSpinBox_2")
        self.horizontalLayout_4.addWidget(self.doubleSpinBox_2)
        self.horizontalLayout_6.addWidget(self.frame_15)
        self.frame_12 = QtWidgets.QFrame(self.frame_16)
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_12)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_10 = QtWidgets.QLabel(self.frame_12)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_5.addWidget(self.label_10)
        self.doubleSpinBox_3 = QtWidgets.QDoubleSpinBox(self.frame_12)
        self.doubleSpinBox_3.setObjectName("doubleSpinBox_3")
        self.horizontalLayout_5.addWidget(self.doubleSpinBox_3)
        self.horizontalLayout_6.addWidget(self.frame_12)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.verticalLayout_9.addWidget(self.frame_16)
        self.frame_17 = QtWidgets.QFrame(self.groupBox_13)
        self.frame_17.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_17.setObjectName("frame_17")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_17)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.frame_18 = QtWidgets.QFrame(self.frame_17)
        self.frame_18.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_18.setObjectName("frame_18")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_18)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_11 = QtWidgets.QLabel(self.frame_18)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_7.addWidget(self.label_11)
        self.comboBox = QtWidgets.QComboBox(self.frame_18)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout_7.addWidget(self.comboBox)
        self.horizontalLayout_8.addWidget(self.frame_18)
        spacerItem2 = QtWidgets.QSpacerItem(303, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem2)
        self.verticalLayout_9.addWidget(self.frame_17)
        self.gridLayout.addWidget(self.groupBox_13, 0, 0, 1, 1)
        self.frame_19 = QtWidgets.QFrame(self.frame)
        self.frame_19.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_19.setObjectName("frame_19")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.frame_19)
        self.verticalLayout_10.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.frame_10 = QtWidgets.QFrame(self.frame_19)
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.frame_10)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.animateButton = QtWidgets.QPushButton(self.frame_10)
        self.animateButton.setObjectName("animateButton")
        self.verticalLayout_12.addWidget(self.animateButton)
        self.closeButton = QtWidgets.QPushButton(self.frame_10)
        self.closeButton.setObjectName("closeButton")
        self.verticalLayout_12.addWidget(self.closeButton)
        self.verticalLayout_10.addWidget(self.frame_10)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem3)
        self.gridLayout.addWidget(self.frame_19, 0, 4, 1, 1)
        self.verticalLayout_11.addWidget(self.frame)
        self.groupBox_10 = QtWidgets.QGroupBox(visualizerDialog)
        self.groupBox_10.setObjectName("groupBox_10")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox_10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_5 = QtWidgets.QFrame(self.groupBox_10)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setStyleSheet("")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_4.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_2 = QtWidgets.QFrame(self.frame_5)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.nodes = QtWidgets.QTableWidget(self.frame_2)
        self.nodes.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.nodes.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.nodes.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.nodes.setObjectName("nodes")
        self.nodes.setColumnCount(4)
        self.nodes.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.nodes.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.nodes.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.nodes.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.nodes.setHorizontalHeaderItem(3, item)
        self.nodes.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.nodes)
        self.verticalLayout_4.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.frame_5)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.frame_3)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.nodeProperties = QtWidgets.QListWidget(self.frame_3)
        self.nodeProperties.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.nodeProperties.setObjectName("nodeProperties")
        self.verticalLayout_2.addWidget(self.nodeProperties)
        self.verticalLayout_4.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.frame_5)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.frame_4)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.selectedNodeProperties = QtWidgets.QListWidget(self.frame_4)
        self.selectedNodeProperties.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.selectedNodeProperties.setObjectName("selectedNodeProperties")
        self.verticalLayout_3.addWidget(self.selectedNodeProperties)
        self.verticalLayout_4.addWidget(self.frame_4)
        self.horizontalLayout.addWidget(self.frame_5)
        self.nodePlot = PlotWidget(self.groupBox_10)
        self.nodePlot.setObjectName("nodePlot")
        self.horizontalLayout.addWidget(self.nodePlot)
        self.verticalLayout_11.addWidget(self.groupBox_10)
        self.groupBox_11 = QtWidgets.QGroupBox(visualizerDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_11.sizePolicy().hasHeightForWidth())
        self.groupBox_11.setSizePolicy(sizePolicy)
        self.groupBox_11.setObjectName("groupBox_11")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox_11)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_6 = QtWidgets.QFrame(self.groupBox_11)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.frame_7 = QtWidgets.QFrame(self.frame_6)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_4 = QtWidgets.QLabel(self.frame_7)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_5.addWidget(self.label_4)
        self.edges = QtWidgets.QTableWidget(self.frame_7)
        self.edges.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.edges.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.edges.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.edges.setObjectName("edges")
        self.edges.setColumnCount(0)
        self.edges.setRowCount(0)
        self.verticalLayout_5.addWidget(self.edges)
        self.verticalLayout_8.addWidget(self.frame_7)
        self.frame_8 = QtWidgets.QFrame(self.frame_6)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_8)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_5 = QtWidgets.QLabel(self.frame_8)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_6.addWidget(self.label_5)
        self.edgeProperties = QtWidgets.QListWidget(self.frame_8)
        self.edgeProperties.setObjectName("edgeProperties")
        self.verticalLayout_6.addWidget(self.edgeProperties)
        self.verticalLayout_8.addWidget(self.frame_8)
        self.frame_9 = QtWidgets.QFrame(self.frame_6)
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_9)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_6 = QtWidgets.QLabel(self.frame_9)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_7.addWidget(self.label_6)
        self.selectedEdgeProperties = QtWidgets.QListWidget(self.frame_9)
        self.selectedEdgeProperties.setObjectName("selectedEdgeProperties")
        self.verticalLayout_7.addWidget(self.selectedEdgeProperties)
        self.verticalLayout_8.addWidget(self.frame_9)
        self.horizontalLayout_2.addWidget(self.frame_6)
        self.edgePlot = PlotWidget(self.groupBox_11)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edgePlot.sizePolicy().hasHeightForWidth())
        self.edgePlot.setSizePolicy(sizePolicy)
        self.edgePlot.setObjectName("edgePlot")
        self.horizontalLayout_2.addWidget(self.edgePlot)
        self.verticalLayout_11.addWidget(self.groupBox_11)

        self.retranslateUi(visualizerDialog)
        QtCore.QMetaObject.connectSlotsByName(visualizerDialog)

    def retranslateUi(self, visualizerDialog):
        _translate = QtCore.QCoreApplication.translate
        visualizerDialog.setWindowTitle(_translate("visualizerDialog", "Dialog"))
        self.groupBox_13.setTitle(_translate("visualizerDialog", "Parameters"))
        self.label_8.setText(_translate("visualizerDialog", "Duration:"))
        self.label_9.setText(_translate("visualizerDialog", "-"))
        self.label_10.setText(_translate("visualizerDialog", "Time scale:"))
        self.label_11.setText(_translate("visualizerDialog", "Pattern:"))
        self.animateButton.setText(_translate("visualizerDialog", "Animate"))
        self.closeButton.setText(_translate("visualizerDialog", "Close"))
        self.groupBox_10.setTitle(_translate("visualizerDialog", "Node results"))
        self.label.setText(_translate("visualizerDialog", "Nodes:"))
        item = self.nodes.horizontalHeaderItem(0)
        item.setText(_translate("visualizerDialog", "id"))
        item = self.nodes.horizontalHeaderItem(1)
        item.setText(_translate("visualizerDialog", "label"))
        item = self.nodes.horizontalHeaderItem(2)
        item.setText(_translate("visualizerDialog", "caption"))
        item = self.nodes.horizontalHeaderItem(3)
        item.setText(_translate("visualizerDialog", "description"))
        self.label_2.setText(_translate("visualizerDialog", "Properties:"))
        self.label_3.setText(_translate("visualizerDialog", "Selected Properties:"))
        self.groupBox_11.setTitle(_translate("visualizerDialog", "Edge results"))
        self.label_4.setText(_translate("visualizerDialog", "Edges:"))
        self.label_5.setText(_translate("visualizerDialog", "Properties:"))
        self.label_6.setText(_translate("visualizerDialog", "Selected Properties:"))
from pyqtgraph import PlotWidget
