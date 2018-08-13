# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MyDiag.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Ui_MyDialog(object):
    def setupUi(self, Ui_MyDialog):
        Ui_MyDialog.setObjectName(_fromUtf8("Ui_MyDialog"))
        Ui_MyDialog.resize(1620, 1110)
        self.verticalLayoutWidget = QtGui.QWidget(Ui_MyDialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(410, 170, 811, 691))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.Namelabel = QtGui.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Namelabel.sizePolicy().hasHeightForWidth())
        self.Namelabel.setSizePolicy(sizePolicy)
        self.Namelabel.setObjectName(_fromUtf8("Namelabel"))
        self.horizontalLayout.addWidget(self.Namelabel)
        self.NamelineEdit = QtGui.QLineEdit(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.NamelineEdit.sizePolicy().hasHeightForWidth())
        self.NamelineEdit.setSizePolicy(sizePolicy)
        self.NamelineEdit.setObjectName(_fromUtf8("NamelineEdit"))
        self.horizontalLayout.addWidget(self.NamelineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.Companylabel = QtGui.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Companylabel.sizePolicy().hasHeightForWidth())
        self.Companylabel.setSizePolicy(sizePolicy)
        self.Companylabel.setObjectName(_fromUtf8("Companylabel"))
        self.horizontalLayout_2.addWidget(self.Companylabel)
        self.CompanylineEdit = QtGui.QLineEdit(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CompanylineEdit.sizePolicy().hasHeightForWidth())
        self.CompanylineEdit.setSizePolicy(sizePolicy)
        self.CompanylineEdit.setObjectName(_fromUtf8("CompanylineEdit"))
        self.horizontalLayout_2.addWidget(self.CompanylineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.Addresslabel = QtGui.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Addresslabel.sizePolicy().hasHeightForWidth())
        self.Addresslabel.setSizePolicy(sizePolicy)
        self.Addresslabel.setObjectName(_fromUtf8("Addresslabel"))
        self.horizontalLayout_3.addWidget(self.Addresslabel)
        self.AddresslineEdit = QtGui.QLineEdit(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AddresslineEdit.sizePolicy().hasHeightForWidth())
        self.AddresslineEdit.setSizePolicy(sizePolicy)
        self.AddresslineEdit.setObjectName(_fromUtf8("AddresslineEdit"))
        self.horizontalLayout_3.addWidget(self.AddresslineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.SaveButton = QtGui.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SaveButton.sizePolicy().hasHeightForWidth())
        self.SaveButton.setSizePolicy(sizePolicy)
        self.SaveButton.setObjectName(_fromUtf8("SaveButton"))
        self.horizontalLayout_4.addWidget(self.SaveButton)
        self.CancelButton = QtGui.QPushButton(self.verticalLayoutWidget)
        self.CancelButton.setObjectName(_fromUtf8("CancelButton"))
        self.horizontalLayout_4.addWidget(self.CancelButton)
        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.retranslateUi(Ui_MyDialog)
        QtCore.QMetaObject.connectSlotsByName(Ui_MyDialog)

    def retranslateUi(self, Ui_MyDialog):
        Ui_MyDialog.setWindowTitle(_translate("Ui_MyDialog", "Dialog", None))
        self.Namelabel.setText(_translate("Ui_MyDialog", "성명", None))
        self.Companylabel.setText(_translate("Ui_MyDialog", "회사", None))
        self.Addresslabel.setText(_translate("Ui_MyDialog", "주소", None))
        self.SaveButton.setText(_translate("Ui_MyDialog", "저장", None))
        self.CancelButton.setText(_translate("Ui_MyDialog", "취소", None))

